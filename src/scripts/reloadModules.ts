import * as vscode from 'vscode';

import * as path from 'path';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as utils from '../modules/utils';

export async function main() {
    const ignorePatterns = utils.getExtensionConfig().get<Array<string>>("reload.ignore");

    const disposableStatusMessage = vscode.window.setStatusBarMessage("$(sync~spin) Reloading modules...", 10000);

    const reloadScriptPath = path.join(utils.getPythonDir(), "reload.py");
    const response = await motionBuilderConsole.executeFile(
        reloadScriptPath,
        {
            "vsc_reload_ignore": ignorePatterns  // eslint-disable-line @typescript-eslint/naming-convention
        }
    );

    disposableStatusMessage.dispose();

    if (!response)
        return;

    // Parse the response
    const [reloadInfo, reloadedPaths] = response.split("-", 2);
    const [numReloads, time] = reloadInfo.split(",", 2);

    // Show info regarding the reloaded modules in the status bar
    const status = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 0);
    status.text = `Reloaded ${numReloads} modules in ${time} seconds`;

    // Show the reloaded modules if the user clicks on the status bar message
    const commandId = "motionbuilder.reloadModulesShowInfo";
    const command = vscode.commands.registerCommand(commandId, async () =>{
        // Create a new document and show reloaded modules
        const reloadedPathsStr = reloadedPaths.replace(/,/g, "\n"); 
        const document = await vscode.workspace.openTextDocument({
            language: "text",
            content: `Reloaded modules in ${time} seconds\n\n${reloadedPathsStr}`
        });
        vscode.window.showTextDocument(document);

        status.dispose();
        command.dispose();
    });
    status.command = commandId;
    
    setTimeout(() => {
        status.dispose();
        command.dispose();
    }, 5000);

    status.show();
}