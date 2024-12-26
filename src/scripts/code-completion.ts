import * as vscode from 'vscode';

import * as fs from 'fs';

import * as logging from '../modules/logging';
import * as utils from '../modules/utils';


const PYTHON_CONFIG = "python";
const EXTRA_PATHS_CONFIG = "analysis.extraPaths";

const GITHUB_API_URL = "https://api.github.com/repos";
const GITHUB_API_HEADERS = {
    'User-Agent': 'VSCode-MotionBuilder-Extension'  // eslint-disable-line @typescript-eslint/naming-convention
};

const REPOSITORY_URL = "nils-soderman/pyfbsdk-stub-generator";
const REPOSITORY_GENERATED_FILES_DIR = "generated-stub-files";


/* eslint-disable @typescript-eslint/naming-convention */
interface IGitHubApiContent {
    name: string;
    path: string;
    sha: string;
    size: number;
    url: string;
    git_url: string;
    download_url: string;
    type: string;
    _links: {
        self: string;
        git: string;
        html: string;
    };
}
/* eslint-enable @typescript-eslint/naming-convention */


interface IVersionQuickPick {
    label: string;
    path: string;
}


/**
 * Make sure that the file at the given path is writable
 */
function ensureWritable(uri: vscode.Uri) {
    if (fs.existsSync(uri.fsPath))
        try {
            fs.chmodSync(uri.fsPath, 0o600);
        } catch (error) {
            logging.showErrorMessage(`Failed to set writable permissions for ${uri.fsPath}`, error as Error);
        }
}


/**
 * Parse the data from the GitHub API into an array of IGitHubApiContent objects.
 */
function parseGitHubApiContent(data: string): Array<IGitHubApiContent> {
    try {
        return JSON.parse(data) as Array<IGitHubApiContent>;
    }
    catch (error) {
        logging.log(data);
        logging.showErrorMessage("Failed to parse available versions", error as Error);
        throw error;
    }
}


/**
 * Get the available versions of the stub files from the GitHub repository.
 * @returns A QuickPick friendly array of available versions
 */
async function getAvailableVersions(): Promise<Array<IVersionQuickPick>> {
    const url = `${GITHUB_API_URL}/${REPOSITORY_URL}/contents/${REPOSITORY_GENERATED_FILES_DIR}`;

    let data: string;

    try {
        data = await utils.getRequest(url, { headers: GITHUB_API_HEADERS, timeout: 10_000 });
    }
    catch (error) {
        logging.showErrorMessage("Failed to fetch available versions", error as Error);
        throw error;
    }

    const parsedData = parseGitHubApiContent(data);

    return parsedData
        .filter(content => content.type === "dir")
        .map(content => ({
            label: content.name.split("-")[1],
            path: content.path
        })).reverse();
}


/**
 * Download the stub files for a specific version from the GitHub repository.
 * @param version The version to download
 * @param destination The destination folder to save the files to
 * @returns An array of downloaded files
 */
async function downloadStubFiles(version: IVersionQuickPick, destination: vscode.Uri) {
    const url = `${GITHUB_API_URL}/${REPOSITORY_URL}/contents/${version.path}`;

    let data: string;

    try {
        data = await utils.getRequest(url, { headers: GITHUB_API_HEADERS, timeout: 10_000 });
    } catch (error) {
        logging.showErrorMessage(`Failed to fetch stub file for ${version.label}`, error as Error);
        throw error;
    }

    const parsedData = parseGitHubApiContent(data);

    let downloadedFiles = [];
    for (const file of parsedData) {
        if (file.type !== "file")
            continue;

        const filename = vscode.Uri.joinPath(destination, file.name);

        try {
            const fileData = await utils.getRequest(file.download_url, { headers: GITHUB_API_HEADERS, timeout: 10_000 });

            if (await utils.uriExists(filename))
                ensureWritable(filename);

            await vscode.workspace.fs.writeFile(filename, Buffer.from(fileData));
            downloadedFiles.push(filename);

            logging.log(`Downloaded "${filename.fsPath}"`);
        }
        catch (error) {
            logging.showErrorMessage(`Failed to download file ${file.name}`, error as Error);
        }
    }

    return downloadedFiles;
}


/**
 * Ensure that the given .pyi files has a corresponding .py file in the same directory
 * If not generate an empty .py file.
 */
async function ensurePyFilesExist(files: vscode.Uri[]) {
    for (const file of files) {
        if (!file.path.endsWith(".pyi")) {
            continue;
        }
        const pyFile = file.with({ path: file.path.replace(".pyi", ".py") });
        if (!await utils.uriExists(pyFile)) {
            try {
                await vscode.workspace.fs.writeFile(pyFile, Buffer.from(""));
            }
            catch (error) {
                logging.showErrorMessage(`Failed to create .py file for ${file.fsPath}`, error as Error);
                continue;
            }
        }
    }
}


/**
 * Add a path to the `python.analysis.extraPaths` configuration.
 * @param pathToAdd The path to add
 * @returns "add" if the path was added, "exists" if the path already exists, false if the path could not be added
 */
export async function addPythonAnalysisPath(pathToAdd: string): Promise<false | "add" | "exists"> {
    const fullConfigName = `${PYTHON_CONFIG}.${EXTRA_PATHS_CONFIG}`;

    const activeWorkspaceFolder = utils.getActiveWorkspaceFolder();
    const pythonConfig = vscode.workspace.getConfiguration(PYTHON_CONFIG, activeWorkspaceFolder?.uri);

    const bHasWorkspaceFileOpen = vscode.workspace.workspaceFile !== undefined;

    let extraPathsConfig = pythonConfig.inspect<string[]>(EXTRA_PATHS_CONFIG);
    if (!extraPathsConfig) {
        logging.showErrorMessage(`Failed to get the config '${fullConfigName}'`, new Error(`Failed to inspect config: '${fullConfigName}'`));
        return false;
    }

    // Use the global scope as default
    let settingsInfo = {
        niceName: "User",
        paths: extraPathsConfig.globalValue,
        scope: vscode.ConfigurationTarget.Global,
        openSettingsCommand: "workbench.action.openSettings"
    };

    // Search through the different scopes to find the first one that has a custom value
    const valuesToCheck = [
        {
            niceName: "Folder",
            paths: extraPathsConfig.workspaceFolderValue,
            scope: vscode.ConfigurationTarget.WorkspaceFolder,
            openSettingsCommand: bHasWorkspaceFileOpen ? "workbench.action.openFolderSettings" : "workbench.action.openWorkspaceSettings"
        },
        {
            niceName: "Workspace",
            paths: extraPathsConfig.workspaceValue,
            scope: vscode.ConfigurationTarget.Workspace,
            openSettingsCommand: "workbench.action.openWorkspaceSettings"
        }
    ];

    for (const value of valuesToCheck) {
        if (value.paths && value.paths !== extraPathsConfig.defaultValue) {
            settingsInfo = value;
            break;
        }
    }

    // Create a new list that will contain the old paths and the new one
    let newPathsValue = settingsInfo.paths ? [...settingsInfo.paths] : [];

    // Check if the path already exists
    if (newPathsValue.some(path => utils.isPathsSame(path, pathToAdd))) {
        logging.log(`Path "${pathToAdd}" already exists in '${fullConfigName}' in ${settingsInfo.niceName} settings.`);
        return "exists";
    }

    // Add the new path and update the configuration
    newPathsValue.push(pathToAdd);
    try {
        await pythonConfig.update(EXTRA_PATHS_CONFIG, newPathsValue, settingsInfo.scope);
    }
    catch (error) {
        const err = error as Error;

        if (err.name === "CodeExpectedError" && err.message.includes("is not a registered configuration")) {
            logging.log(err.message);

            vscode.window.showErrorMessage(
                `[ms-python.vscode-pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) not installed. Could not update the 'python.analysis.extraPaths' setting.`,
                "Show Pylance"
            ).then((value) => {
                if (value === "Show Pylance")
                    vscode.env.openExternal(vscode.Uri.parse(`${vscode.env.uriScheme}:extension/ms-python.vscode-pylance`));
            });
        }
        else
            logging.showErrorMessage(`Failed to update '${fullConfigName}' in ${settingsInfo.niceName} settings.`, err);

        return false;
    }

    // Show a message to the user
    logging.log(`Added path "${pathToAdd}" to '${fullConfigName}' in ${settingsInfo.niceName} settings.`);

    vscode.window.showInformationMessage(`Updated '${fullConfigName}' in ${settingsInfo.niceName} settings.`, "Show Setting").then(
        (value) => {
            if (value === "Show Setting") {
                vscode.commands.executeCommand(settingsInfo.openSettingsCommand, `${fullConfigName}`);
            }
        }
    );

    return "add";
}


async function selectDestination(defaultDestination: vscode.Uri, title: string): Promise<vscode.Uri | undefined> {
    const selectedDestination = await vscode.window.showQuickPick(
        [
            {
                label: `$(extensions) ${defaultDestination.fsPath}`,
                index: 0
            },
            {
                label: "$(folder) Choose custom location...",
                index: 1
            }
        ],
        {
            placeHolder: "Select where to place the stub files",
            title: title
        }
    );

    if (!selectedDestination)
        return undefined;

    if (selectedDestination.index === 1) {
        const result = await vscode.window.showOpenDialog({
            canSelectFiles: false,
            canSelectFolders: true,
            canSelectMany: false,
            openLabel: "Select"
        });

        if (!result || result.length === 0)
            return undefined;

        return result[0];

    }

    return defaultDestination;
}


async function selectVersion(title: string): Promise<IVersionQuickPick | undefined> {
    const availableVersions = await getAvailableVersions();
    return vscode.window.showQuickPick(availableVersions, {
        placeHolder: "Select the MotionBuilder version to use for code completion",
        title: title
    });
}


export async function main(context: vscode.ExtensionContext) {
    const defaultDestination = vscode.Uri.joinPath(context.globalStorageUri, "stubs");
    const title = "MotionBuilder Code Completion Setup";

    const destination = await selectDestination(defaultDestination, `${title} (1/2)`);
    if (!destination)
        return;

    if (!await utils.createDirectoryIfNotExists(destination))
        return;

    const selectedVersion = await selectVersion(`${title} (2/2)`);
    if (!selectedVersion)
        return;

    logging.log(`Placing stub files in: "${destination.fsPath}"`);

    const downloadedFiles = await downloadStubFiles(selectedVersion, destination);
    if (downloadedFiles.length === 0) {
        logging.log("No stub files were downloaded.");
        return;
    }

    await ensurePyFilesExist(downloadedFiles);

    const result = await addPythonAnalysisPath(destination.fsPath);
    if (result === "exists") {
        vscode.window.showInformationMessage(`Updated stub files in '${destination.fsPath}'`);
    }
}