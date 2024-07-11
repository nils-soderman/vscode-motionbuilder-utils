import * as vscode from 'vscode';

import * as path from 'path';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as logging from '../modules/logging';
import * as utils from '../modules/utils';

export async function main() {
    const ignorePatterns = utils.getExtensionConfig().get<Array<string>>("reload.ignore") || [];

    const disposableStatusMessage = vscode.window.setStatusBarMessage("$(sync~spin) Reloading modules...", 10000);

    const reloadScriptPath = path.join(utils.getPythonDir(), "reload_modules.py");
    const response = await motionBuilderConsole.executeFile(
        reloadScriptPath,
        {
            "vsc_reload_ignore": ignorePatterns  // eslint-disable-line @typescript-eslint/naming-convention
        }
    );

    disposableStatusMessage.dispose();

    if (!response)
        return;

    if (response.startsWith("Traceback")) {
        logging.showErrorMessage(
            "Failed to reload modules, ran into an unexpected error.",
            `${reloadScriptPath}\n${response}`
        );
        return;
    }

    // Parse the response
    const [reloadTimeRaw, reloadedPathsRaw, failedPathsRaw] = response.split("|");

    const reloadTime = parseFloat(reloadTimeRaw);
    const reloadedPaths = reloadedPathsRaw.split(",");
    const failedPaths = failedPathsRaw ? failedPathsRaw.split(",") : [];

    const statusBarItemIcon = failedPaths.length > 0 ? "$(error)" : "$(check)";

    // Show info regarding the reloaded modules in the status bar
    const status = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 0);
    status.text = `${statusBarItemIcon} Reloaded ${reloadedPaths.length} modules in ${reloadTime} ms`;

    // Command to show more info about the reload
    const commandId = "motionbuilder.reloadModulesShowInfo";
    const command = vscode.commands.registerCommand(commandId, () => {
        // Create a new document and show reloaded modules
        showReloadInfo(reloadTimeRaw, reloadedPaths, failedPaths, ignorePatterns);

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


/**
 * Log the reload info and show it to the user
 * @param time Total time it took to reload the modules (in ms)
 * @param reloadedPaths Number of modules that were reloaded (as a string)
 * @param failedPaths Content to show in the markdown preview
 */
function showReloadInfo(time: string, reloadedPaths: Array<string>, failedPaths: Array<string>, ignorePatterns: Array<string>) {
    let lines = [`========== Reloaded ${reloadedPaths.length} modules in ${time} ms ==========\n`];

    const ignorePatternsStr = ignorePatterns.map(pattern => `"${pattern}"`).join(", ");
    lines.push(`Ignored patterns: ${ignorePatternsStr}\n`);

    if (failedPaths.length > 0) {
        lines.push(
            "Failed to reload the following modules:",
            ...failedPaths,
            "\n"
        );
    }

    const reloadInfo = [];
    let maxTimeLength = 0; // used for padding
    for (const moduleInfo of reloadedPaths) {
        const [time, path] = utils.splitAtFirstOccurrence(moduleInfo, "-");
        reloadInfo.push([time, path]);

        maxTimeLength = Math.max(maxTimeLength, time.length);
    }

    const tableTitleTime = "Time (ms)";
    maxTimeLength = Math.max(maxTimeLength, tableTitleTime.length);

    lines.push(
        "Successfully reloaded the following modules:\n",
        tableTitleTime.padEnd(maxTimeLength, " ") + " | Path",
        "".padEnd(maxTimeLength, "-") + " | -----------------"
    );

    for (const [time, path] of reloadInfo) {
        const paddedTime = time.padEnd(maxTimeLength, ' ');
        lines.push(`${paddedTime} | ${path}`);
    }

    const message = lines.join("\n");
    logging.log(message);
    logging.showLog();
}