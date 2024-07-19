/**
 * Code that needs to be run before the tests are run
 */

import * as path from 'path';

import * as utils from '../../modules/utils';


export function initializeExtension() {
    const extensionDir = path.join(__dirname, '..', '..', '..');
    utils.setExtensionDir(extensionDir);
}

export function getPythonTestFilepath(filename: string): string {
    return path.join(utils.getPythonDir(), "test", filename);
}