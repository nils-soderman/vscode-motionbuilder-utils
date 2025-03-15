import * as vscode from 'vscode';

import { MotionBuilderSocket } from 'motionbuilder-socket';

import * as extensionWiki from './extension-wiki';
import * as logging from '../modules/logging';
import * as utils from './utils';


let gSocket: MotionBuilderSocket | null = null;

/**
 * Get a global socket connection to MotionBuilder
 */
async function getSocket() {
    if (gSocket) {
        // TODO: Validate connection, may not be needed. As if we drop connection we now set gSocket to be undefined
        return gSocket;
    }

    const socket = new MotionBuilderSocket();
    logging.log(`Connecting to MotionBuilder at ${socket.ip}:${socket.port}`);

    try {
        await socket.open(10_000);
    }
    catch (e: any) {
        if (e.code === "ECONNREFUSED") {
            vscode.window.showErrorMessage("Failed to connect to MotionBuilder.", "Help").then((selectedValue) => {
                if (selectedValue === "Help") {
                    extensionWiki.openPageInBrowser(extensionWiki.Pages.failedToConnect);
                }
            });
        }
        else if (e.code === "ETIMEDOUT") {
            vscode.window.showErrorMessage("Connection to MotionBuilder timed out, make sure MotionBuilder is not minimized.");
            logging.logError("Connection timed out, this is usually caused by MotionBuilder being minimized");
        }
        else {
            logging.showErrorMessage(`Failed to connect to MotionBuilder with error code: ${e.code}`, e);
            return null;
        }

        logging.logError(JSON.stringify(e));
        return null;
    }

    socket.on("close", () => {
        gSocket = null;
    });
    gSocket = socket;

    logging.log("Connection established");

    await onSocketConnected(socket);

    return gSocket;
}

/**
 * Called when a socket connection is established
 */
async function onSocketConnected(socket: MotionBuilderSocket) {
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (workspaceFolders) {
        let foldersToAddToPath: string[] = [];
        for (const folder of workspaceFolders) {
            const config = vscode.workspace.getConfiguration("motionbuilder", folder.uri);
            if (config.get<boolean>('environment.addWorkspaceToPath', false)) {
                foldersToAddToPath.push(folder.uri.fsPath);
            }
        }

        if (foldersToAddToPath.length > 0) {
            const scriptPath = vscode.Uri.joinPath(utils.getPythonDir(), "add_sys_path.py");

            const response = await executeFile(
                scriptPath,
                {
                    vsc_paths: foldersToAddToPath // eslint-disable-line @typescript-eslint/naming-convention
                }
            );

            if (response)
                logging.log(response);
        }
    }
}


/**
 * Run a command in MotionBuilder
 * @param command The command to run
 * @returns Python output e.g: print statements or errors
 */
export async function runCommand(command: string) {
    const socket = await getSocket();
    if (!socket)
        return null;

    const response = await socket.exec(command);
    return response;
}


/**
 * Execute a file in MotionBuilder
 * @param filepath Absolute path to the file
 * @param variables An object containing key-value pairs of global variables to set before executing the file. The keys should be strings representing the variable names, and the values can be of any serializable type.
 * @returns Python output e.g: print statements or errors
 */
export async function executeFile(filepath: vscode.Uri, variables: { [key: string]: any } = {}) {
    const socket = await getSocket();
    if (!socket)
        return null;

    const response = await socket.execFile(filepath.fsPath, variables);
    return response;
}


export function closeSocket() {
    if (gSocket) {
        try {
            gSocket.close();
        } catch (error: any) {
            logging.showErrorMessage("Error closing the socket", error);
        }
    }
}