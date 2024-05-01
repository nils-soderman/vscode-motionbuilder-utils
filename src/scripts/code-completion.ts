import * as vscode from 'vscode';

import * as path from 'path';
import * as fs from 'fs';

import * as logging from '../modules/logging';
import * as utils from '../modules/utils';


const PYTHON_CONFIG = "python";
const EXTRA_PATHS_CONFIG = "analysis.extraPaths";
const RESOURCES_STUBS_FOLDER_NAME = "stub-files";

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
function ensureWritable(path: string) {
    if (fs.existsSync(path))
        fs.chmodSync(path, 0o600);
}


/**
 * Get the path to where the stub files provided by this extension are located.  
 * This is the source path and no configurations should point to this path!
 * Instead the files located here can be copied elsewhere on disk.
 * @param version MotionBuilder version, if version is undefined the folder containing all versions will be returned.
 */
function getSourceStubFileDirectory() {
    return path.join(utils.getResourcesDir(), RESOURCES_STUBS_FOLDER_NAME);
}


/**
 * Parse the data from the GitHub API into an array of IGitHubApiContent objects.
 */
function parseGitHubApiContent(data: string): Array<IGitHubApiContent> {
    try {
        return JSON.parse(data) as Array<IGitHubApiContent>;
    }
    catch (error) {
        const err = error as Error;
        logging.showErrorMessage("Failed to parse available versions", `${err.message}\nJSON:\n${data}`);
        throw err;
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
        data = await utils.getRequest(url, GITHUB_API_HEADERS);
    }
    catch (error) {
        const err = error as Error;
        logging.showErrorMessage("Failed to fetch available versions", err.message);
        throw err;
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
async function downloadStubFiles(version: IVersionQuickPick, destination: string) {
    const url = `${GITHUB_API_URL}/${REPOSITORY_URL}/contents/${version.path}`;

    let data: string;

    try {
        data = await utils.getRequest(url, GITHUB_API_HEADERS);
    } catch (error) {
        const err = error as Error;
        logging.showErrorMessage(`Failed to fetch stub file for ${version.label}`, err.message);
        throw err;
    }

    const parsedData = parseGitHubApiContent(data);

    let downloadedFiles = [];
    for (const file of parsedData) {
        if (file.type !== "file")
            continue;

        const filename = path.join(destination, file.name);

        try {
            const fileData = await utils.getRequest(file.download_url, GITHUB_API_HEADERS);

            if (fs.existsSync(filename))
                ensureWritable(filename);

            fs.writeFileSync(filename, fileData);
            downloadedFiles.push(filename);

            logging.log(`Downloaded "${filename}"`);
        }
        catch (error) {
            const err = error as Error;
            logging.showErrorMessage(`Failed to download file ${file.name}`, err.message);
        }
    }

    return downloadedFiles;
}


/**
 * Copy local stub files that comes with the extension from 'resources/stub-files/' -> `targetDirectory`
 * @param targetDirectory The directory to copy the files into
 */
function copyLocalStubFiles(targetDirectory: string): string[] {
    const stubFilesSourceDirectory = getSourceStubFileDirectory();

    const filesCopied: string[] = [];

    // Loop through all of the files under the 'stub-files/XXXX/' folder
    for (const filepath of fs.readdirSync(stubFilesSourceDirectory)) {
        const targetFilepath = path.join(targetDirectory, filepath);
        const sourceFilepath = path.join(stubFilesSourceDirectory, filepath);

        if (fs.existsSync(targetFilepath)) {
            // Check if the stub file we're about to copy is newer than the one we already have
            if (fs.statSync(sourceFilepath).mtime <= fs.statSync(targetFilepath).mtime) {
                logging.log(`"${targetFilepath}" already exists and is up to date`);
                continue;
            }

            ensureWritable(targetFilepath);
        }

        try {
            fs.copyFileSync(sourceFilepath, targetFilepath);
        }
        catch (error) {
            const err = error as Error;
            logging.showErrorMessage(`Failed to copy file ${filepath}`, err.message);
            continue;
        }

        filesCopied.push(targetFilepath);

        logging.log(`Copied ${filepath} to ${targetFilepath}`);
    }

    return filesCopied;
}


/**
 * Ensure that the given .pyi files has a corresponding .py file in the same directory
 * If not generate an empty .py file.
 */
function ensurePyFilesExist(files: string[]) {
    for (const file of files) {
        if (!file.endsWith(".pyi")) {
            continue;
        }
        const pyFile = file.replace(".pyi", ".py");
        if (!fs.existsSync(pyFile)) {
            try {
                fs.writeFileSync(pyFile, "");
            }
            catch (error) {
                const err = error as Error;
                logging.showErrorMessage(`Failed to create .py file for ${file}`, err.message);
                continue;
            }
        }
    }
}


/**
 * Add a path to the `python.analysis.extraPaths` configuration.
 * @param pathToAdd The path to add
 */
function addPythonAnalysisPath(pathToAdd: string) {
    const fullConfigName = `${PYTHON_CONFIG}.${EXTRA_PATHS_CONFIG}`;

    const activeWorkspaceFolder = utils.getActiveWorkspaceFolder();
    const pythonConfig = vscode.workspace.getConfiguration(PYTHON_CONFIG, activeWorkspaceFolder?.uri);

    let extraPathsConfig = pythonConfig.inspect<string[]>(EXTRA_PATHS_CONFIG);
    if (!extraPathsConfig) {
        return;
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
            openSettingsCommand: "workbench.action.openFolderSettings"
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
        return;
    }

    // Add the new path and update the configuration
    newPathsValue.push(pathToAdd);
    pythonConfig.update(EXTRA_PATHS_CONFIG, newPathsValue, settingsInfo.scope);

    // Show a message to the user
    logging.log(`Added path "${pathToAdd}" to '${fullConfigName}' in ${settingsInfo.niceName} settings.`);

    vscode.window.showInformationMessage(`Updated '${fullConfigName}' in ${settingsInfo.niceName} settings.`, "Show Settings").then(
        (value) => {
            if (value === "Show Settings") {
                vscode.commands.executeCommand(settingsInfo.openSettingsCommand, `${fullConfigName}`);
            }
        }
    );
}


export async function main(context: vscode.ExtensionContext) {
    const defaultDestination = path.join(context.globalStorageUri.fsPath, "stubs");

    const title = "MotionBuilder Code Completion Setup";

    const selectedDestination = await vscode.window.showQuickPick(
        [
            {
                label: `$(extensions) ${defaultDestination}`,
                index: 0
            },
            {
                label: "$(folder) Choose custom location...",
                index: 1
            }
        ],
        {
            placeHolder: "Select where to place the stub files",
            title: `${title} (1/2)`,
        }
    );
    if (!selectedDestination)
        return;

    let destination = "";
    if (selectedDestination.index === 1) {
        const result = await vscode.window.showOpenDialog({
            canSelectFiles: false,
            canSelectFolders: true,
            canSelectMany: false,
            openLabel: "Select"
        });

        if (!result || result.length == 0) {
            return;
        }

        destination = result[0].fsPath;
    }
    else {
        destination = defaultDestination;
    }

    if (!fs.existsSync(destination)) {
        try {
            fs.mkdirSync(destination, { recursive: true });
        } catch (error) {
            const err = error as Error;
            logging.showErrorMessage(`Failed to create directory ${destination}`, err.message);
            return;
        }
    }

    // Ask user to select a version
    const availableVersions = await getAvailableVersions();
    const selectedVersion = await vscode.window.showQuickPick(availableVersions, {
        placeHolder: "Select the MotionBuilder version to use for code completion",
        title: `${title} (2/2)`,
    });
    if (!selectedVersion)
        return;

    logging.log(`Placing stub files in: "${destination}"`);

    // Download the stub files
    const downloadedFiles = await downloadStubFiles(selectedVersion, destination);
    if (downloadedFiles.length === 0) {
        logging.log("No stub files were downloaded.");
        return;
    }

    // Copy stub files
    const copiedFiles = copyLocalStubFiles(destination);

    // Ensure that the .py files exists
    // These are needed for the python extension to not throw warnings
    ensurePyFilesExist([...downloadedFiles, ...copiedFiles]);

    // Add path to python analysis
    addPythonAnalysisPath(destination);
}