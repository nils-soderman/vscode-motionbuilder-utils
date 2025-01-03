import * as vscode from 'vscode';

import * as fs from 'fs';

import * as logging from '../modules/logging';
import * as utils from '../modules/utils';


const CONFIG_PYTHON = "python";
const CONFIG_KEY_EXTRA_PATHS = "analysis.extraPaths";

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


interface IExtraPathsScopeConfigDetails {
    scopeName: string;
    paths: string[] | undefined;
    scope: vscode.ConfigurationTarget;
    openSettingsCommand: string;
}


interface IExtraPathsConfig {
    workspaceFolderValue?: string[];
    workspaceValue?: string[];
    globalValue?: string[];
    defaultValue?: string[];
}


/**
 * Make sure that the file at the given path is writable
 */
function ensureWritable(uri: vscode.Uri) {
    if (fs.existsSync(uri.fsPath)) {
        try {
            fs.chmodSync(uri.fsPath, 0o600);
        } catch (error) {
            logging.showErrorMessage(`Failed to set writable permissions for ${uri.fsPath}`, error as Error);
        }
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
 * Check if the 'ms-python.vscode-pylance' extension is installed, and if not prompt the user to install it.
 * @returns 
 */
function validatePylanceExtension(): boolean {
    const PYLANCE_EXTENSION_ID = "ms-python.vscode-pylance";
    const PYLANCE_EXTENSION_URL = "https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance";
    const SHOW_PYLANCE = "Show Pylance";

    // Pylance is the extension that provides the 'python.analysis.extraPaths' setting
    const pylanceExtension = vscode.extensions.getExtension(PYLANCE_EXTENSION_ID);
    if (!pylanceExtension) {
        vscode.window.showErrorMessage(
            `[${PYLANCE_EXTENSION_ID}](${PYLANCE_EXTENSION_URL}) not installed. Could not update the '${CONFIG_PYTHON}.${CONFIG_KEY_EXTRA_PATHS}' setting.`,
            SHOW_PYLANCE
        ).then((value) => {
            if (value === SHOW_PYLANCE)
                vscode.commands.executeCommand("extension.open", PYLANCE_EXTENSION_ID);
        });

        return false;
    }

    return true;
}


/**
 * Get the settings info for the `python.analysis.extraPaths` configuration.
 * This function will figure out wich scope to use and the current value of the configuration (in that scope).
 * @param extraPathsConfig 
 * @returns 
 */
function getConfigForCurrentScope(extraPathsConfig: IExtraPathsConfig): IExtraPathsScopeConfigDetails {
    // Search through the different scopes to find the first one that has a custom value
    const bHasWorkspaceFileOpen = vscode.workspace.workspaceFile !== undefined;

    const valuesToCheck = [
        {
            scopeName: "Folder",
            paths: extraPathsConfig.workspaceFolderValue,
            scope: vscode.ConfigurationTarget.WorkspaceFolder,
            openSettingsCommand: bHasWorkspaceFileOpen ? "workbench.action.openFolderSettings" : "workbench.action.openWorkspaceSettings"
        },
        {
            scopeName: "Workspace",
            paths: extraPathsConfig.workspaceValue,
            scope: vscode.ConfigurationTarget.Workspace,
            openSettingsCommand: "workbench.action.openWorkspaceSettings"
        }
    ];

    for (const value of valuesToCheck) {
        if (value.paths && value.paths !== extraPathsConfig.defaultValue) {
            return value;
        }
    }

    return {
        scopeName: "User",
        paths: extraPathsConfig.globalValue,
        scope: vscode.ConfigurationTarget.Global,
        openSettingsCommand: "workbench.action.openSettings"
    };
}


/**
 * Add a path to the `python.analysis.extraPaths` configuration.
 * @param pathToAdd The path to add
 * @returns "add" if the path was added, "exists" if the path already exists, false if the path could not be added
 */
export async function addPythonAnalysisPath(pathToAdd: string): Promise<false | "add" | "exists"> {
    if (!validatePylanceExtension())
        return false;

    const extraPathsConfigName = `${CONFIG_PYTHON}.${CONFIG_KEY_EXTRA_PATHS}`;

    const activeWorkspaceFolder = utils.getActiveWorkspaceFolder();
    const pythonConfig = vscode.workspace.getConfiguration(CONFIG_PYTHON, activeWorkspaceFolder?.uri);

    const extraPathsConfig = pythonConfig.inspect<string[]>(CONFIG_KEY_EXTRA_PATHS);
    if (!extraPathsConfig) {
        logging.showErrorMessage(`Failed to get the config '${extraPathsConfigName}'`, new Error(`Failed to inspect config: '${extraPathsConfigName}'`));
        return false;
    }

    // Get the config from current scope
    const currentScopeConfig = getConfigForCurrentScope(extraPathsConfig);

    // Create a new list that will contain the old paths and the new one
    let newExtraPathsValue = currentScopeConfig.paths ? [...currentScopeConfig.paths] : [];

    // Check if the path already exists
    if (newExtraPathsValue.some(path => utils.isPathsSame(path, pathToAdd))) {
        logging.log(`Path "${pathToAdd}" already exists in '${extraPathsConfigName}' in ${currentScopeConfig.scopeName} settings.`);
        return "exists";
    }

    // Add the new path and update the configuration
    newExtraPathsValue.push(pathToAdd);
    try {
        await pythonConfig.update(CONFIG_KEY_EXTRA_PATHS, newExtraPathsValue, currentScopeConfig.scope);
    }
    catch (error) {
        logging.showErrorMessage(`Failed to update '${extraPathsConfigName}' in ${currentScopeConfig.scopeName} settings.`, error as Error);
        return false;
    }

    // Show a message to the user
    logging.log(`Added path "${pathToAdd}" to '${extraPathsConfigName}' in ${currentScopeConfig.scopeName} settings.`);

    vscode.window.showInformationMessage(`Updated '${extraPathsConfigName}' in ${currentScopeConfig.scopeName} settings.`, "Show Setting").then(
        (value) => {
            if (value === "Show Setting") {
                vscode.commands.executeCommand(currentScopeConfig.openSettingsCommand, `${extraPathsConfigName}`);
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