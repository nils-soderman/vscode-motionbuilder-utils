/**
 * This scripts get's called once this extension has been uninstalled & VS Code restarted (not reloaded).
 * This get's called outside of VS Code's environment & without the extension being loaded,
 * Therefore any custom modules nor the vscode api cannot be reached here, only import native nodejs modules! 
 */

import * as path from 'path';
import * as fs   from 'fs';


/** --------------------------------------------------------------------------
 *                      Functions lifted from Utils
 * -------------------------------------------------------------------------- */


export function getAppDataFolder() {
    return process.env.APPDATA || (process.platform === 'darwin' ? process.env.HOME + '/Library/Preferences' : process.env.HOME + "/.local/share");
}

export function getExtensionAppdataFolder() {
    return path.join(getAppDataFolder(), "Code", "User", "globalStorage", "nilssoderman.mobu-utils");
}


/** --------------------------------------------------------------------------
 *                                  Main
 * -------------------------------------------------------------------------- */

function main() {
    // Cleanup all files placed in the extension's appdata folder
    const appdataFolder = getExtensionAppdataFolder();
    if (fs.existsSync(appdataFolder)) {
        fs.rmSync(appdataFolder, { recursive: true });
    }
}


if (require.main === module) {
    main();
}