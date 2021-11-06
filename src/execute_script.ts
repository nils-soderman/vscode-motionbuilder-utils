import * as vscode from 'vscode';

const Telnet = require('telnet-client');

const DEFAULT_IP = '127.0.0.1';
const DEFAULT_PORT = 4242;

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
    console.log("fileToExecute: " + fileToExecute);
    


    let connection = new Telnet();

    let params = {
        host: DEFAULT_IP,
        port: DEFAULT_PORT,
        negotiationMandatory: false,
        timeout: 1500
    };

    try {
        await connection.connect(params);
    } catch (error) {
        // handle the throw (timeout)
        console.log("Could not connect");
        return;
    }
    
    connection.exec(`with open(r'${fileToExecute}', 'r') as f:exec(f.read())`);

}