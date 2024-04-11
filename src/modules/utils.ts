import * as vscode from 'vscode';

import * as tcpPortUsed from 'tcp-port-used';
import * as https from 'https';
import * as path from 'path';
import * as os from 'os';
import * as fs from 'fs';

// Variables
const EXTENSION_DATA_FOLDER_NAME = "VSCode-MotionBuilder-Utils";
export const DEBUG_SESSION_NAME = "MotionBuilder Utils";


// -----------------------------------------------------------------------------------------
//                                 Extension Directories
// -----------------------------------------------------------------------------------------

let _extensionDir: string | undefined; // Stores the absolute path to this extension's directory, set on activation

/**
 * This function should only be called once, on activation
 * @param dir Should be: `ExtensionContext.extensionPath`
 */
export function setExtensionDir(dir: string) {
    _extensionDir = dir;
}

/**
 * This function cannot be called in top-level. It must be called after the extension has been activated
 * @returns The absolute path to this extension's directory
 */
export function getExtensionDir() {
    if (!_extensionDir) {
        throw Error("Extension Dir hasn't been set yet! This should be set on activation. This function cannot be called in top-level.");
    }
    return _extensionDir;
}

/**
 * @returns The absolute path to this extension's python directory
 */
export function getPythonDir() {
    return path.join(getExtensionDir(), "python");
}

/**
 * @returns The absolute path to this extension's resources directory
 */
export function getResourcesDir() {
    return path.join(getExtensionDir(), "resources");
}

// TODO: These functions were deprecated in version 2025.0.0. Remove them in the future.
/**
 * @deprecated Will be removed in the future.
 */
export function getAppDataFolder() {
    return process.env.APPDATA || (process.platform === 'darwin' ? process.env.HOME + '/Library/Preferences' : process.env.HOME + "/.local/share");
}

/**
 * @deprecated Will be removed in the future. Use `context.globalStoragePath` instead
 */
export function getExtensionAppdataFolder() {
    const appdataDir = path.join(getAppDataFolder(), EXTENSION_DATA_FOLDER_NAME);
    return appdataDir;
}


/**
 * @param bEnsureExists If folder doesn't exist, create it
 * @returns absolute path to this extensions tempdir
 */
export function getExtentionTempDir(bEnsureExists = true) {
    const tempDir = path.join(os.tmpdir(), EXTENSION_DATA_FOLDER_NAME);
    if (bEnsureExists && !fs.existsSync(tempDir)) {
        fs.mkdirSync(tempDir);
    }
    return tempDir;
}


// -----------------------------------------------------------------------------------------
//                                     Extension
// -----------------------------------------------------------------------------------------

/** Check if we're currently attached to a MotionBuilder instance */
export function isDebuggingMotionBuilder() {
    if (!vscode.debug.activeDebugSession) {
        return false;
    }
    return vscode.debug.activeDebugSession.name == DEBUG_SESSION_NAME;
}

/**
 * @returns The workspace configuration for this extension _('motionbuilder')_
 */
export function getExtensionConfig() {
    // Try to get the active workspace folder first, to have it read Folder Settings
    let workspaceFolder: vscode.Uri | undefined;
    if (vscode.window.activeTextEditor) {
        const activeDocumenet = vscode.window.activeTextEditor.document;
        workspaceFolder = vscode.workspace.getWorkspaceFolder(activeDocumenet.uri)?.uri;
    }

    return vscode.workspace.getConfiguration("motionbuilder", workspaceFolder);
}


// -----------------------------------------------------------------------------------------
//                                    Filesystem
// -----------------------------------------------------------------------------------------

/**
 * Write a temp file inside of this extensions temp directory
 * @param filename The basename of the file
 * @param text Text to write to the file
 * @returns the absolute filepath of the file
 */
export function saveTempFile(filename: string, text: string) {
    const filepath = path.join(getExtentionTempDir(), filename);
    fs.writeFileSync(filepath, text);
    return filepath;
}


/**
 * Delete the temp folder created by this extension (and all of the files inside of it)
 */
export function cleanupTempFiles() {
    const tempDir = getExtentionTempDir();
    if (fs.existsSync(tempDir)) {
        fs.rmSync(tempDir, { recursive: true });
    }
}


/**
 * @param filepath the absoulte filepath to the json file
 * @returns the parsed data as a object
 */
export function readJson(filepath: string) {
    const fileContent = fs.readFileSync(filepath);
    return JSON.parse(fileContent.toString());
}

/**
 * Expand a path's environment variables  
 * Example:   
 * `%AppData%/HelloWorld/..` -> `C:/.../AppData/HelloWorld/...`
 */
export function expandPath(path: string) {
    // @ts-ignore
    return path.replace(/%([^%]+)%/g, (_, n) => process.env[n]);
}

/**
 * Ensure a path uses forward slashes
 */
export function ensureForwardSlashes(path: string) {
    return path.replace(/\\/g, "/").replace(/\/\//g, "/");
}


/**
 * Compare two paths and check if they are pointing to the same file / directory
 * Regardless of case sensitivity, forward or backward slashes etc. 
 */
export function isPathsSame(a: string, b: string) {
    return path.resolve(a).toLowerCase() == path.resolve(b).toLowerCase();
}


// -----------------------------------------------------------------------------------------
//                                        Network
// -----------------------------------------------------------------------------------------

/**
 * Do a web get-request
 * @param url The url whose content to fetch
*/
export function getRequest(url: string, headers?: any): Promise<string> {
    return new Promise((resolve, reject) => {
        https.get(url, {headers}, (res) => {
            let data = '';
            res.on('data', (chunk) => {
                data += chunk;
            });

            res.on('end', () => {
                if (!res.statusCode || res.statusCode >= 400) {
                    reject(new Error(`${url} returned with status code: ${res.statusCode}\nHeaders:\n${JSON.stringify(res.headers, null, 2)}\nBody:\n${data}`));
                    return;
                }
                else
                    resolve(data);
            });

            res.on('error', (err) => {
                reject(err);
            });
        });
    });
}


/** 
 * Check if a port is taken 
 * @param port The port to check
 * @param host The ip, will default to localhost
*/
export async function isPortAvailable(port: number, host?: string) {
    return !await tcpPortUsed.check(port, host);
}


/**  
 * Check the ports between `startPort` -> `startPort + num`, and return the first one that's free
 * @param startPort The port to start itterating from
 * @param num How many ports to check
 * @param host The ip, will default to localhost
 * @returns The port as a number, or `null` if all ports were taken
*/
export async function findFreePort(startPort: number, num: number, host?: string) {
    for (let i = 0; i < num; i++) {
        const port = startPort + i;
        if (await isPortAvailable(port, host)) {
            return port;
        }
    }
    
    return null;
}


// -----------------------------------------------------------------------------------------
//                                        Misc
// -----------------------------------------------------------------------------------------

/**
 * Split a string at the first occurence of a separator
 */
export function splitAtFirstOccurrence(str: string, separator: string) {
    const index = str.indexOf(separator);
    return [str.slice(0, index), str.slice(index + 1)];
}