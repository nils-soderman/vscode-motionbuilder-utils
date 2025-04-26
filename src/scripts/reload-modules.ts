import * as vscode from 'vscode';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as utils from '../modules/utils';


interface IReloadModulesResponse {
    time: number;
    num_reloads: number;
    num_failed: number;
}


export async function main() {
    const disposableStatusMessage = vscode.window.setStatusBarMessage("$(sync~spin) Reloading modules...", 5000);

    // Get workspace folders
    const workspaceFolders = vscode.workspace.workspaceFolders?.map(folder => folder.uri.fsPath) || [];

    const reloadScriptPath = vscode.Uri.joinPath(utils.getPythonDir(), "reload_modules.py");
    const response = await motionBuilderConsole.evaluateFunction<IReloadModulesResponse>(
        reloadScriptPath,
        "reload",
        {
            "workspace_folders": workspaceFolders  // eslint-disable-line @typescript-eslint/naming-convention
        }
    );

    disposableStatusMessage.dispose();

    if (!response)
        return;

    const statusBarItemIcon = response.num_failed > 0 ? "$(error)" : "$(check)";
    vscode.window.setStatusBarMessage(`${statusBarItemIcon} Reloaded ${response.num_reloads} modules in ${response.time} ms`, 3500);
}
