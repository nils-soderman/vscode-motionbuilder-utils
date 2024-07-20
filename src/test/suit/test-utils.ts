/**
 * Code that needs to be run before the tests are run
 */
import * as vscode from 'vscode';

import * as path from 'path';

import * as utils from '../../modules/utils';


export function initializeExtension() {
    const extensionDir = path.join(__dirname, '..', '..', '..');
    utils.setExtensionUri(vscode.Uri.file(extensionDir));
}

export function getPythonTestFilepath(filename: string): vscode.Uri {
    return vscode.Uri.joinPath(utils.getPythonDir(), "test", filename);
}

export async function uriExists(uri: vscode.Uri): Promise<boolean> {
    try {
        await vscode.workspace.fs.stat(uri);
        return true;
    } catch (error) {
        return false;
    }
}