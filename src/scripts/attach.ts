import * as vscode from 'vscode';

import * as crypto from 'crypto';

import * as logging from '../modules/logging';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as utils from '../modules/utils';


/**
 * Get the abs path to a debug script
 * @param filename The name of the script
 */
function getDebugScriptPath(filename: string) {
    return vscode.Uri.joinPath(utils.getPythonDir(), "attach", filename);
}


/**
 * Split the response into lines and return an array of lines
 */
function parseResponse(responseRaw: string | null) {
    const response = responseRaw?.split("\n");
    if (!response) {
        return null;
    }
    return response;
}


/**
 * Check if the response contains the successId, and log all other lines
 * @param response The parsed response from MotionBuilder
 * @param successId if this string is found in the response, return true
 * @param failId don't log this string
 * @param bLog Log all lines that are not the successId/failId
 * @returns True if the successId was found in the response
 */
function checkForSuccess(response: string[] | null, successId: string, failId: string = "False", bLog: boolean = true) {
    if (!response) {
        return false;
    }

    let bSuccess = false;
    for (const line of response) {
        if (line === successId)
            bSuccess = true;
        else if (bLog && line !== failId)
            logging.log(line);
    }

    return bSuccess;
}


/**
 * Check if debugpy python module is installed
 * @param pythonPackageDir The path to the extension can install python packages
 */
export async function isDebugpyInstalled(pythonPackageDir: vscode.Uri) {
    logging.log("Checking if debugpy is installed");

    const successId = crypto.randomUUID();
    const scriptPath = getDebugScriptPath("is_debugpy_installed.py");

    const responseRaw = await motionBuilderConsole.executeFile(scriptPath, {
        vsc_target: pythonPackageDir.fsPath,  // eslint-disable-line @typescript-eslint/naming-convention
        vsc_suceess_id: successId  // eslint-disable-line @typescript-eslint/naming-convention
    });

    // In Mobu 2023, the response might be empty if the Python Editor window is not open
    if (!responseRaw) {
        return "MoBu2023";
    }

    return checkForSuccess(parseResponse(responseRaw), successId);
}


/**
 * Install the debugpy python module
 * @param target The directory to install the module in
 */
export async function installDebugpy(target: vscode.Uri) {
    logging.log(`Installing debugpy in ${target.fsPath}`);

    const successId = crypto.randomUUID();
    const scriptPath = getDebugScriptPath("install_debugpy.py");
    const responseRaw = await motionBuilderConsole.executeFile(scriptPath, {
        vsc_target: target.fsPath, // eslint-disable-line @typescript-eslint/naming-convention
        vsc_suceess_id: successId // eslint-disable-line @typescript-eslint/naming-convention
    });

    return checkForSuccess(parseResponse(responseRaw), successId);
}


/**
 * Start the debugpy server in MotionBuilder
 * @param port The port to start the server on
 * @param pythonPackageDir The path to the extension can install python packages
 * @returns True if the server was started successfully
 */
async function startDebugpyServer(port: number, pythonPackageDir: vscode.Uri) {
    const scriptPath = getDebugScriptPath("start_debugpy_server.py");

    const successId = crypto.randomUUID();

    logging.log(`Starting debugpy server on port ${port}`);

    const responseRaw = await motionBuilderConsole.executeFile(scriptPath, {
        vsc_port: port,  // eslint-disable-line @typescript-eslint/naming-convention
        vsc_target: pythonPackageDir.fsPath,  // eslint-disable-line @typescript-eslint/naming-convention
        vsc_suceess_id: successId  // eslint-disable-line @typescript-eslint/naming-convention
    });

    return checkForSuccess(parseResponse(responseRaw), successId);
}


/**
 * Check if debugpy is already running in MotionBuilder, and if so return the port it's using
 */
export async function getCurrentDebugPort() {
    const scriptPath = getDebugScriptPath("get_current_debug_port.py");
    const responseRaw = await motionBuilderConsole.executeFile(scriptPath);
    const lines = parseResponse(responseRaw);
    if (!lines)
        return null;

    for (const line of lines) {
        const port = parseInt(line);
        if (port)
            return port;
    }

    return null;
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
        const pythonPackageDir = vscode.Uri.joinPath(context.globalStorageUri, "site-packages");

        // Make sure debugpy is installed
        const bIsDebugpyInstalled = await isDebugpyInstalled(pythonPackageDir);
        if (bIsDebugpyInstalled === "MoBu2023") {
            // In Mobu 2023, the response might be empty if the Python Editor window is not open
            vscode.window.showErrorMessage('Due to a bug in MoBu 2023 the MotionBuilder window "Python Editor" must be open before attaching.');
            return false;
        }

        if (!bIsDebugpyInstalled) {
            logging.log("debugpy is not installed");
            const selectedInstallOption = await vscode.window.showWarningMessage(
                "Python module 'debugpy' is required for debugging",
                "Install"
            );

            if (selectedInstallOption === "Install") {
                if (!await installDebugpy(pythonPackageDir)) {
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

        if (!await startDebugpyServer(port, pythonPackageDir)) {
            return false;
        }
    }

    const configuration: vscode.DebugConfiguration = {
        "name": utils.DEBUG_SESSION_NAME,
        "type": "python",
        "request": "attach",
        "connect": {
            "host": "localhost",
            "port": port
        }
    };

    logging.log(`Starting debug session with configuration:\n${JSON.stringify(configuration, null, 2)}`);

    return vscode.debug.startDebugging(undefined, configuration);
}
