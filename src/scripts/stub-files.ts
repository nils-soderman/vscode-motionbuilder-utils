import * as vscode from 'vscode';

import * as path from 'path';
import * as fs   from 'fs';

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
 * @param version MotionBuilder version
 */
function getSourceStubFileDirectory(version: number) {
    return path.join(utils.EXTENSION_RESOURCES_DIR, STUB_FILES_FOLDER_NAME, version.toString());
}


/**
 * Get the absolute path to where the motionbuilder stub files should be placed. 
 * (as defined by the configuration `motionbuilder.bystubFiles.copyPath`)
 * @param bEnsureExists If folder doesn't exist, create it.
 */
function getCopyDestinationPath(bEnsureExists = true) {
    // See if there is a custom path defined in the user's settings
    const customPath: string | undefined = utils.getExtensionConfig().get("stubFiles.copyPath");
    if (customPath) {
        // Expand environment variables
        const absPath = utils.ensureForwardSlashes(utils.expandPath(customPath));

        // Make sure folder exists
        if (bEnsureExists && !fs.existsSync(absPath)) {
            fs.mkdirSync(absPath, { recursive: true });
        }

        return absPath;
    }

    // No custom path was found, use the default one under AppData
    const folderPath = utils.ensureForwardSlashes(path.join(utils.getExtensionAppdataFolder(), "mobu-sdk"));
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
function copyStubFiles(version:number, targetDirectory: string, bForceCopy = false) {
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
    const destination = getCopyDestinationPath();
    
    // Copy stub files
    if (utils.getExtensionConfig().get("stubFiles.copyOnStartup")) {
        const version = utils.getMotionBuilderVersion();
        copyStubFiles(version, destination, bForceCopy);
    }

    // Add path to user startup
    if (utils.getExtensionConfig().get("stubFiles.patchPythonPathConfig")) {
        addPythonAnalysisPath(destination);
    }
}
