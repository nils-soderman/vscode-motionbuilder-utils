import * as vscode from 'vscode';

import * as path from 'path';

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

    logging.log("Connecting to MotionBuilder...");

    const socket = new MotionBuilderSocket();

    try {
        await socket.open(10);
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
        }
        else {
            logging.showErrorMessage(`Failed to connect to MotionBuilder with error code: ${e.code}`, JSON.stringify(e));
            return null;
        }

        logging.log(JSON.stringify(e));
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
            const scriptPath = path.join(utils.getPythonDir(), "add_sys_path.py");

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
 * @param variables Global variables to set before executing the file
 * @returns Python output e.g: print statements or errors
 */
export async function executeFile(filepath: string, variables: { [key: string]: any } = {}) {
    const socket = await getSocket();
    if (!socket)
        return null;

    const response = await socket.execFile(filepath, variables);
    return response;
}