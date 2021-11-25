import * as vscode from 'vscode';

import * as path from 'path';

import * as motionBuilderConsole from './motionbuilder-console';
import * as utils from './utils';


const TEMP_FILENAME = "VSCode-MotionBuilder-Exec";
const TEMP_EXECDATA_FILENAME = "vscode-exec.json";
const PYTHON_ENTER_FILE = path.join(__dirname, "..", "python", "mb-execute.py");


/**
 * Write a json temp file that can be read by MotionBuilder, to know what script to execute etc.
 * @param fileToExecute The abs filepath to the .py file that should be executed
 * @param originalFilepath The abs filepath to the source filepath, will be used to set the python var `__file__`
 */
function writeDataFile(fileToExecute: string, originalFilepath: string) {
    let data: any = {};
    data["file"] = fileToExecute;
    data["__file__"] = originalFilepath;
    utils.saveTempFile(TEMP_EXECDATA_FILENAME, JSON.stringify(data));
}


export async function execute() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const activeDocuemt = vscode.window.activeTextEditor.document;
    let selectionText = "";

    // Combine all user selections into a single string
    for (let selection of vscode.window.activeTextEditor.selections) {
        if (!selection.isEmpty) {
            selectionText += activeDocuemt.getText(selection) + "\n";
        }
    }

    let fileToExecute = "";
    // If user had any selected text, save the selection as a temp file to execute
    if (selectionText) {
        fileToExecute = utils.saveTempFile(TEMP_FILENAME, selectionText);
    }

    else if (activeDocuemt.isDirty) {
        // File is dirty, save a copy of the currenet text in temp
        fileToExecute = utils.saveTempFile(TEMP_FILENAME, activeDocuemt.getText());
    }

    else {
        fileToExecute = activeDocuemt.uri.fsPath;
    }

    // File an info file telling mb what script to run, etc.
    writeDataFile(fileToExecute, activeDocuemt.uri.fsPath);

    motionBuilderConsole.runCommand(`with open(r'${PYTHON_ENTER_FILE}','r')as f:exec(f.read())\n`);

}

