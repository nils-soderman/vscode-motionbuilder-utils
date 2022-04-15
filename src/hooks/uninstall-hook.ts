/**
 * This file get's called when the extension is completely uninstalled.
 */

import * as fs    from 'fs';

import * as utils from '../utils';


function main() {
    // Clean up any temp files
    utils.cleanupTempFiles();
    
    // Cleanup all files placed under %AppData%
    const appdataFolder = utils.getExtensionAppdataFolder();
    if (fs.existsSync(appdataFolder)) {
        fs.rmSync(appdataFolder, { recursive: true });
    }
}


main();