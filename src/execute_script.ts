import * as vscode from 'vscode';
import * as console from './motionbuilder-console';


export async function execute() {

    if (!vscode.window.activeTextEditor?.document)
        return;

    let fileToExecute = "";
    if (vscode.window.activeTextEditor.document.isDirty) {
        // File is dirty, save a copy in temp
    }
    else {
        fileToExecute = vscode.window.activeTextEditor.document.uri.fsPath;
    }
    
    // TODO: This can fail if file is currently saving
    console.runCommand(`with open(r'${fileToExecute}', 'r') as f:exec(f.read())\n`);
}

