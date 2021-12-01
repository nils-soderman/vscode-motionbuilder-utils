import * as vscode from 'vscode';

import * as path from "path";
import * as fs from 'fs';

import * as utils from "./utils";


const PYTHON_CONFIG = "python";
const EXTRA_PATHS_CONFIG = "analysis.extraPaths";


function getPythonConfig() {
    return vscode.workspace.getConfiguration(PYTHON_CONFIG);
}


function getSourceAutocompletionDirectory() {
    return path.join(path.dirname(__dirname), "auto-completion");
}


function getAutocompletionDirectory(bEnsureExists = true) {
    // See if there is a custom path defined in the user's settings
    const customPath: string | undefined = utils.getExtensionConfig().get("autocompletion.sdkCopyPath");
    if (customPath) {
        if (bEnsureExists && !fs.existsSync(customPath)) {
            fs.mkdirSync(customPath, {recursive: true});
        }
        return customPath;
    }

    // No custom path was found, use the default one under AppData
    const folderPath = path.join(utils.getExtensionAppdataFolder(), "mobu-sdk");
    if (bEnsureExists && !fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath);
    }
    return folderPath;
}


function copySDKFiles(targetDirectory: string) {
    const sdkSourceDirectory = getSourceAutocompletionDirectory();

    // loop through all of the files under the auto_completion folder
    for (const filepath of fs.readdirSync(sdkSourceDirectory)) {
        const targetFilepath = path.join(targetDirectory, filepath);
        const sourceFilepath = path.join(sdkSourceDirectory, filepath);

        if (fs.existsSync(targetFilepath)) {
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


function addPythonAnalysisPath(pathToAdd: string) {
    const pythonConfig = getPythonConfig();
    let extraPaths: Array<string> | undefined = pythonConfig.get(EXTRA_PATHS_CONFIG);
    if (extraPaths) {
        // Check if 'python.analysis.extraPaths' contains the completion path
        if (!extraPaths.includes(pathToAdd)) {

            // Add the path to extraPaths
            extraPaths.push(pathToAdd);
            pythonConfig.update(EXTRA_PATHS_CONFIG, extraPaths, true);
        }
    }
}


export async function setupAutocompletion() {
    const sdkDirectory = getAutocompletionDirectory();

    // Make sure the files exists
    copySDKFiles(sdkDirectory);

    // Add path to user startup
    addPythonAnalysisPath(sdkDirectory);
}
