import * as vscode from 'vscode';

import * as extensionWiki from './extension-wiki';
import { MotionBuilderSocket } from 'motionbuilder-socket';


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

    try {
        await socket.open();
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
            vscode.window.showErrorMessage(`MotionBuilder: Something went wrong when trying to connect to MB.\n${e.message}`);
        }

        return null;
    }

    socket.on("close", () => {
        gSocket = null;
    });
    gSocket = socket;

    return gSocket;
}



/**
 * Run a command in MotionBuilder
 * @param command The command to run
 * @returns Python output e.g: print statements or errors
 */
export async function runCommand(command: string) {
    const socket = await getSocket();
    if (!socket) {
        return null;
    }

    const response = await socket.exec(command);
    return response;
}


/**
 * Execute a file in MotionBuilder
 * @param filepath Absolute path to the file
 * @param variables Global variables to set before executing the file
 * @returns Python output e.g: print statements or errors
 */
export async function executeFile(filepath: string, variables = {}) {
    const socket = await getSocket();
    if (!socket) {
        return null;
    }

    const response = await socket.execFile(filepath, variables);
    return response;
}