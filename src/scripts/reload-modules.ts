import * as vscode from 'vscode';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as logging from '../modules/logging';
import * as utils from '../modules/utils';


interface IReloadModulesResponse {
    time: number;
    num_reloads: number;
    num_failed: number;
}

let isCommandRegistered = false;

export async function main() {
    const disposableStatusMessage = vscode.window.setStatusBarMessage("$(sync~spin) Reloading modules...", 5000);

    // Get workspace folders
    const workspaceFolders = vscode.workspace.workspaceFolders?.map(folder => folder.uri.fsPath) || [];

    const reloadScriptPath = vscode.Uri.joinPath(utils.getPythonDir(), "reload_modules.py");
    const response = await motionBuilderConsole.evaluateFunction<IReloadModulesResponse>(
        reloadScriptPath,
        "reload",
        {
            "workspace_folders": workspaceFolders  // eslint-disable-line @typescrip6t-eslint/naming-convention
        }
    );

    disposableStatusMessage.dispose();

    if (!response)
        return;

    if (response.num_failed <= 0) {
        vscode.window.setStatusBarMessage(`$(check) Reloaded ${response.num_reloads} modules in ${response.time} ms`, 3500);
    }
    else if (!isCommandRegistered) {
        const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 5);
        statusBarItem.text = `$(error) Failed to reload ${response.num_failed} module${response.num_failed === 1 ? '' : 's'}`;
        statusBarItem.command = "ue-python.showReloadErrorMessage";
        statusBarItem.color = new vscode.ThemeColor('errorForeground');

        const timeout = setTimeout(() => {
            dispose();
        }, 5000);

        const commandDisposable = vscode.commands.registerCommand(statusBarItem.command, () => {
            logging.getOutputChannel().show();
            clearTimeout(timeout);
            dispose();
        });

        const dispose = () => {
            statusBarItem.dispose();
            commandDisposable.dispose();
            isCommandRegistered = false;
        }

        statusBarItem.show();

        isCommandRegistered = true;
    }
}
