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

    // Show a status bar message with the result
    const [numReloads, time] =  response.split(",");
    const message = `Reloaded ${numReloads} modules in ${time} seconds`;
    vscode.window.setStatusBarMessage(message, 5000);
}