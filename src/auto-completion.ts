import * as vscode from 'vscode';

import * as path from "path";

const PYTHON_CONFIG = "python";
const EXTRA_PATHS_CONFIG = "analysis.extraPaths";


function getPythonConfig() {
    return vscode.workspace.getConfiguration(PYTHON_CONFIG);
}


function getMoBuAutocompletionDirectory() {
    return path.join(path.dirname(__dirname), "auto_completion");
}


export function setupAutocompletion() {
    const pythonConfig = getPythonConfig();
    let extraPaths: Array<string> | undefined = pythonConfig.get(EXTRA_PATHS_CONFIG);
    if (extraPaths) {
        const completionPath = getMoBuAutocompletionDirectory();

        // Check if 'python.analysis.extraPaths' contains the completion path
        if (!extraPaths.includes(completionPath)) {

            // Add the path to extraPaths
            extraPaths.splice(0, 0, completionPath);
            pythonConfig.update(EXTRA_PATHS_CONFIG, extraPaths, true);
        }
    }
}