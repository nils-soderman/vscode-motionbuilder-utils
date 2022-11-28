import * as vscode from 'vscode';

import * as https from 'https';
import * as path  from 'path';
import * as os    from 'os';
import * as fs    from 'fs';

// Variables
const EXTENSION_DATA_FOLDER_NAME = "VSCode-MotionBuilder-Utils";
export const DEBUG_SESSION_NAME = "MotionBuilder Utils";
export const EXTENSION_DIR = path.dirname(path.dirname(__dirname));
export const EXTENSION_PYTHON_DIR = path.join(EXTENSION_DIR, "python");
export const EXTENSION_RESOURCES_DIR = path.join(EXTENSION_DIR, "resources");
export const DEFAULT_VERSION = 2023;


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


/** Check if we're currently attached to a MotionBuilder instance */
export function isDebuggingMotionBuilder() {
    if (!vscode.debug.activeDebugSession) {
        return false;
    }
    return vscode.debug.activeDebugSession.name == DEBUG_SESSION_NAME;
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
 * Get the Appdata folder path
 */
export function getAppDataFolder() {
    return process.env.APPDATA || (process.platform === 'darwin' ? process.env.HOME + '/Library/Preferences' : process.env.HOME + "/.local/share");
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
 * Get this extension's subfolder under AppData which can be used to store files in
 * @param bEnsureExists If folder doesn't exists, create it
 */
export function getExtensionAppdataFolder(bEnsureExists = true) {
    const appdataDir = path.join(getAppDataFolder(), EXTENSION_DATA_FOLDER_NAME);
    if (bEnsureExists && !fs.existsSync(appdataDir)) {
        fs.mkdirSync(appdataDir);
    }
    return appdataDir;
}


/**
 * Get this extension's folder where python site-packages can be installed
 * @param bEnsureExists If folder doesn't exists, create it
 */
export function getExtensionPythonPackagesDir(bEnsureExists = true) {
    const sitePackageDir = path.join(getExtensionAppdataFolder(), "python", "site-packages");
    if (bEnsureExists && !fs.existsSync(sitePackageDir)) {
        fs.mkdirSync(sitePackageDir, {"recursive": true});
    }
    return sitePackageDir;
}


/**
 * @returns The workspace configuration for this extension _('motionbuilder')_
 */
export function getExtensionConfig() {
    // Try to get the active workspace folder first, to have it read Folder Settings
    let workspaceFolder;
    if (vscode.window.activeTextEditor) {
        const activeDocumenet = vscode.window.activeTextEditor.document;
        workspaceFolder = vscode.workspace.getWorkspaceFolder(activeDocumenet.uri);
    }

    return vscode.workspace.getConfiguration("motionbuilder", workspaceFolder);
}


/**
 * Compare two paths and check if they are pointing to the same file / directory
 * Regardless of case sensitivity, forward or backward slashes etc. 
 */
export function isPathsSame(a: string, b: string) {
    return path.resolve(a).toLowerCase() == path.resolve(b).toLowerCase();
}


/**
 * Get the MotionBuilder version the user wants to use given by the config
 */
export function getMotionBuilderVersion() {
    let version: number | undefined = getExtensionConfig().get("version");
    if (!version) {
        return DEFAULT_VERSION;
    }
    return version;
}


/**
 * Do a web get-request
 * @param url The url whose content to fetch
 * @param callback Callback function to call with the response. Will be called with 2 parameters: (data: string, statusCode: number)
 */
export function getRequest(url: string, callback?: Function) {
    https.get(url, (res) => {
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });

        res.on("end", () => {
            if (callback) {
                callback(data, res.statusCode);
            }
        });

        res.on('error', () => {
            if (callback) {
                callback(data, res.statusCode);
            }
        });
    });
}