import * as vscode from 'vscode';

import * as logging from '../modules/logging';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as utils from '../modules/utils';


/**
 * Get the abs path to the attach.py script
 */
function getAttachScript() {
    return vscode.Uri.joinPath(utils.getPythonDir(), "attach.py");
}


/**
 * Check if debugpy python module is installed
 */
export function isDebugpyInstalled() {
    return motionBuilderConsole.evaluateFunction<number>(getAttachScript(), "is_debugpy_installed");
}


/**
 * Install the debugpy python module
 */
export async function installDebugpy() {
    logging.log(`Installing debugpy `);

    return await motionBuilderConsole.evaluateFunction<boolean>(getAttachScript(), "install_debugpy") == true;
}


/**
 * Start the debugpy server in MotionBuilder
 * @param port The port to start the server on
 * @returns True if the server was started successfully
 */
async function startDebugpyServer(port: number) {
    logging.log(`Starting debugpy server on port ${port}`);

    return await motionBuilderConsole.evaluateFunction<boolean>(
        getAttachScript(),
        "start_debugpy_server",
        { port }
    ) == true;

}


/**
 * Check if debugpy is already running in MotionBuilder, and if so return the port it's using
 */
export function getCurrentDebugPort() {
    return motionBuilderConsole.evaluateFunction<number>(getAttachScript(), "get_current_debugpy_port");
}


/**
 * Get a free port to use for the debugpy server
 */
export async function getWantedPort() {
    const extConfig = utils.getExtensionConfig();

    const port = extConfig.get<number>("attach.port");
    if (!port) {
        return null;
    }

    if (await utils.isPortAvailable(port)) {
        return port;
    }

    if (extConfig.get<boolean>("attach.autoPort")) {
        const freePort = await utils.findFreePort(port, 100);
        if (freePort) {
            return freePort;
        }

        vscode.window.showErrorMessage(`Failed to find a free port between ${port} and ${port + 100}. Please change the port in the extension settings`);
    }
    else {
        vscode.window.showErrorMessage(`Port ${port} is already in use. Please change the port in the extension settings or enable 'Auto Port'`);
    }

    return null;
}


export async function main(context: vscode.ExtensionContext): Promise<boolean> {
    if (utils.isDebuggingMotionBuilder()) {
        logging.log("Already debugging MotionBuilder, aborting attach attempt.");
        return true;
    }

    logging.log("Checking if debugpy is already running");
    let port = await getCurrentDebugPort();
    if (port) {
        logging.log(`debugpy is running on port ${port}`);
    }
    else {
        // Make sure debugpy is installed
        const bIsDebugpyInstalled = await isDebugpyInstalled();

        if (!bIsDebugpyInstalled) {
            logging.log("debugpy is not installed");
            const selectedInstallOption = await vscode.window.showWarningMessage(
                "Python module 'debugpy' is required for debugging",
                "Install"
            );

            if (selectedInstallOption === "Install") {
                if (!await installDebugpy()) {
                    logging.showErrorMessage("Failed to install debugpy", new Error("Failed to install debugpy"));
                    return false;
                }
            }
            else {
                return false;
            }
        }

        port = await getWantedPort();
        if (!port) {
            return false;
        }

        if (!await startDebugpyServer(port)) {
            return false;
        }
    }

    const configuration: vscode.DebugConfiguration = {
        "name": utils.DEBUG_SESSION_NAME,
        "type": "debugpy",
        "request": "attach",
        "connect": {
            "host": "localhost",
            "port": port
        }
    };

    logging.log(`Starting debug session with configuration:\n${JSON.stringify(configuration, null, 2)}`);

    return vscode.debug.startDebugging(undefined, configuration);
}
