import * as vscode from 'vscode';
import * as https from 'https';
import * as path from 'path';
import * as os from "os";
import * as fs from 'fs';


const TEMPFOLDER_NAME = "VSCode-MotionBuilder-Utils";


/**
 * @param bEnsureExists If folder doesn't exist, create it
 * @returns absolute path to this extensions tempdir
 */
export function getExtentionTempDir(bEnsureExists = true) {
    const tempDir = path.join(os.tmpdir(), TEMPFOLDER_NAME);
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

/**
 * Delete the temp folder created by this extension (and all of the files inside of it)
 */
export function cleanupTempFiles() {
    const tempDir = getExtentionTempDir();
    if (fs.existsSync(tempDir)) {
        fs.rmdirSync(tempDir, { recursive: true });
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


export function getAppDataFolder() {
    return process.env.APPDATA || (process.platform === 'darwin' ? process.env.HOME + '/Library/Preferences' : process.env.HOME + "/.local/share");
}


export function getExtensionAppdataFolder(bEnsureExists = true) {
    const appdataDir = path.join(getAppDataFolder(), TEMPFOLDER_NAME);
    if (bEnsureExists && !fs.existsSync(appdataDir)) {
        fs.mkdirSync(appdataDir);
    }
    return appdataDir;
}



/**
 * @returns The workspace configuration for this extension _('motionbuilder')_
 */
export function getExtensionConfig() {
    return vscode.workspace.getConfiguration("motionbuilder");
}


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