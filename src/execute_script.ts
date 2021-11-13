import * as vscode from 'vscode';
import * as motionBuilderConsole from './motionbuilder-console';
import * as fs from "fs";
import * as os from "os";
import * as path from "path";


function saveTempFile(text: string) {
    const filepath = path.join(os.tmpdir(), "VSCode-MotionBuilder-Exec");
    fs.writeFileSync(filepath, text);
    return filepath;
}


export async function execute() {

    if (!vscode.window.activeTextEditor?.document) {
        return;
    }

    let fileToExecute = "";

    let selectionText = "";
    for (let selection of vscode.window.activeTextEditor.selections) {
        if (!selection.isEmpty) {
            selectionText += vscode.window.activeTextEditor.document.getText(selection) + "\n";
        }
    }

    if (selectionText) {
        fileToExecute = saveTempFile(selectionText);
    }
    else if (vscode.window.activeTextEditor.document.isDirty) {
        // File is dirty, save a copy in temp
        fileToExecute = saveTempFile(vscode.window.activeTextEditor.document.getText());
    }
    else {
        fileToExecute = vscode.window.activeTextEditor.document.uri.fsPath;
    }

    // TODO: This can fail if file is currently saving
    motionBuilderConsole.runCommand(`with open(r'${fileToExecute}', 'r') as f:exec(f.read())\n`);
}

