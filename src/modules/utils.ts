import * as vscode from 'vscode';

import * as tcpPortUsed from 'tcp-port-used';
import * as https from 'https';
import * as path from 'path';
import * as os from 'os';
import * as fs from 'fs';

import * as logging from './logging';

// Variables
const EXTENSION_DATA_FOLDER_NAME = "VSCode-MotionBuilder-Utils";
export const DEBUG_SESSION_NAME = "MotionBuilder Utils";


// -----------------------------------------------------------------------------------------
//                                 Extension Directories
// -----------------------------------------------------------------------------------------

let _extensionUri: vscode.Uri | undefined; // Stores the absolute path to this extension's directory, set on activation

/**
 * This function should only be called once, on activation
 * @param uri Should be: `ExtensionContext.extensionPath`
 */
export function setExtensionUri(uri: vscode.Uri) {
    _extensionUri = uri;
}

/**
 * This function cannot be called in top-level. It must be called after the extension has been activated
 * @returns The absolute path to this extension's directory
 */
export function getExtensionUri(): vscode.Uri {
    if (!_extensionUri) {
        throw Error("Extension Dir hasn't been set yet! This should be set on activation. This function cannot be called in top-level.");
    }
    return _extensionUri;
}

/**
 * @returns The absolute path to this extension's python directory
 */
export function getPythonDir() {
    return vscode.Uri.joinPath(getExtensionUri(), "python");
}


/**
 * @param bEnsureExists If folder doesn't exist, create it
 * @returns absolute path to this extensions tempdir
 */
export async function getExtensionTempDir(bEnsureExists = true) {
    const tmpDir = vscode.Uri.joinPath(
        vscode.Uri.file(os.tmpdir()),
        EXTENSION_DATA_FOLDER_NAME
    );

    if (bEnsureExists)
        createDirectoryIfNotExists(tmpDir);

    return tmpDir;
}


/** Check if a filesystem file/directory exists at the given uri */
export async function uriExists(uri: vscode.Uri): Promise<boolean> {
    try {
        const stat = await vscode.workspace.fs.stat(uri);
        return true;
    } catch (error) {
        return false;
    }
}


// -----------------------------------------------------------------------------------------
//                                     Extension
// -----------------------------------------------------------------------------------------

/** Check if we're currently attached to a MotionBuilder instance */
export function isDebuggingMotionBuilder() {
    if (!vscode.debug.activeDebugSession) {
        return false;
    }
    return vscode.debug.activeDebugSession.name === DEBUG_SESSION_NAME;
}

export function getActiveWorkspaceFolder(): vscode.WorkspaceFolder | undefined {
    if (vscode.window.activeTextEditor) {
        const activeDocument = vscode.window.activeTextEditor.document;
        return vscode.workspace.getWorkspaceFolder(activeDocument.uri);
    }
}

/**
 * @returns The workspace configuration for this extension _('motionbuilder')_
 */
export function getExtensionConfig(): vscode.WorkspaceConfiguration {
    // Try to get the active workspace folder first, to have it read Folder Settings
    const activeWorkspaceFolder = getActiveWorkspaceFolder()?.uri;
    return vscode.workspace.getConfiguration("motionbuilder", activeWorkspaceFolder);
}


function getDeprecatedConfig<T>(key: string, deprecatedKey: string): T | undefined {
    const extConfig = getExtensionConfig();

    const value = extConfig.get<T>(key);
    if (value !== undefined && value !== extConfig.inspect(key)?.defaultValue) {
        return value;
    }

    const deprecatedValue = extConfig.get<T>(deprecatedKey);
    if (deprecatedValue !== undefined && deprecatedValue !== extConfig.inspect(deprecatedKey)?.defaultValue) {
        vscode.window.showWarningMessage(`The setting 'motionbuilder.${deprecatedKey}' is deprecated, please use 'motionbuilder.${key}' instead`);
        return deprecatedValue;
    }

    return value;
}


// -----------------------------------------------------------------------------------------
//                                    Filesystem
// -----------------------------------------------------------------------------------------

export async function createDirectoryIfNotExists(directory: vscode.Uri) {
    if (!await uriExists(directory)) {
        try {
            await vscode.workspace.fs.createDirectory(directory);
        } catch (error) {
            logging.showErrorMessage(`Failed to create directory ${directory.fsPath}`, error as Error);
            return false;
        }
    }

    return true;
}

/**
 * Write a temp file inside of this extensions temp directory
 * @param filename The basename of the file
 * @param text Text to write to the file
 * @returns the absolute filepath of the file
 */
export async function saveTempFile(filename: string, text: string) {
    const filepath = vscode.Uri.joinPath(await getExtensionTempDir(), filename);
    await vscode.workspace.fs.writeFile(filepath, Buffer.from(text));
    return filepath;
}


/**
 * Delete the temp folder created by this extension (and all of the files inside of it)
 */
export async function cleanupTempFiles() {
    const tmpDir = await getExtensionTempDir(false);
    
    if (fs.existsSync(tmpDir.fsPath)) {
        fs.rmSync(tmpDir.fsPath, { recursive: true });
    }
}


/**
 * @param filepath the absoulte filepath to the json file
 * @returns the parsed data as a object
 */
export async function readJson(filepath: vscode.Uri) {
    const fileContent = await vscode.workspace.fs.readFile(filepath);
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
    return path.resolve(a).toLowerCase() === path.resolve(b).toLowerCase();
}


// -----------------------------------------------------------------------------------------
//                                        Network
// -----------------------------------------------------------------------------------------

/**
 * Do a web get-request
 * @param url The url whose content to fetch
*/
export function httpsGetRequest(url: string, options: https.RequestOptions = {}): Promise<string> {
    return new Promise((resolve, reject) => {
        https.get(url, options, (res) => {
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
        }).on("error", (err: Error) => {
            reject(err);
        });
    });
}


/** 
 * Check if a port is taken 
 * @param port The port to check
 * @param host The ip, will default to localhost
*/
export async function isPortAvailable(port: number, host?: string): Promise<boolean> {
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


let gOutputChannel: vscode.OutputChannel | undefined;

/** Get the output channel for this extension */
export function getOutputChannel() {
    if (!gOutputChannel) {
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder Output");
    }
    return gOutputChannel;
}