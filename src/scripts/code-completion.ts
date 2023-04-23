import * as vscode from 'vscode';

import * as path from 'path';
import * as fs from 'fs';

import * as utils from '../modules/utils';


const PYTHON_CONFIG = "python";
const EXTRA_PATHS_CONFIG = "analysis.extraPaths";
const STUB_FILES_FOLDER_NAME = "stub-files";


/**
 * Get the configuration for the python extension
 */
function getPythonConfig() {
    return vscode.workspace.getConfiguration(PYTHON_CONFIG);
}


/**
 * Get the path to where the stub files provided by this extension are located.  
 * This is the source path and no configurations should point to this path!
 * Instead the files located here can be copied elsewhere on disk.
 * @param version MotionBuilder version, if version is undefined the folder containing all versions will be returned.
 */
function getSourceStubFileDirectory(version?: number) {
    if (version == null) {
        return path.join(utils.EXTENSION_RESOURCES_DIR, STUB_FILES_FOLDER_NAME);
    }
    return path.join(utils.EXTENSION_RESOURCES_DIR, STUB_FILES_FOLDER_NAME, version.toString());
}


/**
 * Get the absolute path to where the motionbuilder stub files should be placed. 
 * @param bEnsureExists If folder doesn't exist, create it.
 */
function getCopyDestinationPath(bEnsureExists = true) {
    // No custom path was found, use the default one under AppData
    const folderPath = utils.ensureForwardSlashes(path.join(utils.getExtensionAppdataFolder(), "stubs"));
    if (bEnsureExists && !fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath);
    }
    return folderPath;
}


/**
 * Copy stub files from 'resources/stub-files/XXXX/' -> `targetDirectory`
 * @param version MotionBuilder version of stub files to copy
 * @param targetDirectory The directory to copy the files into
 * @param bForceCopy Copy files even if they already exist & we don't have a newer version to copy 
 */
function copyStubFiles(version: number, targetDirectory: string, bForceCopy = false) {
    const stubFilesSourceDirectory = getSourceStubFileDirectory(version);

    // Loop through all of the files under the 'stub-files/XXXX/' folder
    for (const filepath of fs.readdirSync(stubFilesSourceDirectory)) {
        const targetFilepath = path.join(targetDirectory, filepath);
        const sourceFilepath = path.join(stubFilesSourceDirectory, filepath);

        if (!bForceCopy && fs.existsSync(targetFilepath)) {
            // if file already exists, check if there if the source is a newer version
            if (fs.statSync(sourceFilepath).mtime > fs.statSync(targetFilepath).mtime) {
                fs.chmodSync(targetFilepath, 0o600); // Make sure file is writeable
                fs.copyFile(sourceFilepath, targetFilepath, () => { });
            }
        }
        else {
            fs.copyFile(sourceFilepath, targetFilepath, () => { });
        }
    }
}


/**
 * Add a path to the `pyhon.analysis.extraPaths` configuration.
 * @param pathToAdd The path to add
 */
function addPythonAnalysisPath(pathToAdd: string) {
    const pythonConfig = getPythonConfig();
    let extraPaths: Array<string> | undefined = pythonConfig.get(EXTRA_PATHS_CONFIG);
    if (extraPaths) {
        for (const path of extraPaths) {
            if (utils.isPathsSame(path, pathToAdd)) {
                return;
            }
        }

        // Add the path to extraPaths
        extraPaths.push(pathToAdd);
        pythonConfig.update(EXTRA_PATHS_CONFIG, extraPaths, true);
    }
}


export async function setup(bForceCopy = false) {
    let destination = "";

    const selected = await vscode.window.showQuickPick([".../AppData/Roaming/VSCode-MotionBuilder-Utils/stubs/", "Choose custom location..."], {
        placeHolder: "Select where to place the stub files"
    });
    if (!selected) {
        return;
    }

    if (selected === "Choose custom location...") {
        const result = await vscode.window.showOpenDialog({
            canSelectFiles: false,
            canSelectFolders: true,
            canSelectMany: false,
            openLabel: "Select"
        });

        if (result && result.length > 0) {
            destination = result[0].fsPath;
        }
    }
    else {
        destination = getCopyDestinationPath();
    }

    // Ask user to select a version
    // Get available versions by looking in the resources/stub-files folder
    const availableVersions = fs.readdirSync(getSourceStubFileDirectory());
    const selectedVersion = await vscode.window.showQuickPick(availableVersions);
    if (!selectedVersion) {
        return;
    }

    // Copy stub files
    // Convert string to number
    const version = parseInt(selectedVersion);
    copyStubFiles(version, destination, bForceCopy);

    // Add path to user startup
    addPythonAnalysisPath(destination);
}