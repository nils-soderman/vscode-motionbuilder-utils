import * as vscode from 'vscode';

import * as path from 'path';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as utils from '../modules/utils';

function getDebugScriptPath(filename: string) {
    return path.join(utils.getPythonDir(), "debug", filename);
}

async function isDebugpyInstalled() {
    const pythonPackages = utils.getExtensionPythonPackagesDir(false);

    const scriptPath = getDebugScriptPath("is_debugpy_installed.py");
    const response = await motionBuilderConsole.executeFile(scriptPath, { ext_packages_dir: pythonPackages }); // eslint-disable-line @typescript-eslint/naming-convention
    if (!response) {
        return "MoBu2023"; // In Mobu 2023, the response might be empty if the Python Editor window is not open
    }

    return response === "True";
}

async function installDebugpy() {
    const pythonPackages = utils.getExtensionPythonPackagesDir(false);
    const scriptPath = getDebugScriptPath("install_debugpy.py");
    const response = await motionBuilderConsole.executeFile(scriptPath, { ext_packages_dir: pythonPackages }); // eslint-disable-line @typescript-eslint/naming-convention

    return response === "True";
}

async function startDebugpyServer(port: number) {
    const pythonPackages = utils.getExtensionPythonPackagesDir(false);
    const scriptPath = getDebugScriptPath("start_debugpy_server.py");
    const response = await motionBuilderConsole.executeFile(scriptPath, { port: port, ext_packages_dir: pythonPackages }); // eslint-disable-line @typescript-eslint/naming-convention

    return response === "True";
}

async function getCurrentDebugPort() {
    const scriptPath = getDebugScriptPath("get_current_debug_port.py");
    const response = await motionBuilderConsole.executeFile(scriptPath);
    if (response && response != "None") {
        return parseInt(response);
    }
    return null;
}


async function getWantedPort() {
    const extConfig = utils.getExtensionConfig();
    const port: number | undefined = extConfig.get("debug.port");
    if (!port) {
        return null;
    }

    if (await utils.isPortAvailable(port)) {
        return port;
    }

    if (extConfig.get("debug.autoPort")) {
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


export async function attachToMotionBuilder() {
    if (utils.isDebuggingMotionBuilder()) {
        return;
    }

    let port = await getCurrentDebugPort();
    if (!port) {
        // Make sure debugpy is installed
        const bIsDebugpyInstalled = await isDebugpyInstalled();
        if (bIsDebugpyInstalled === "MoBu2023") {
            // In Mobu 2023, the response might be empty if the Python Editor window is not open
            vscode.window.showErrorMessage('Due to a bug in MoBu 2023 the MotionBuilder window "Python Editor" must be open before attaching.');
            return;
        }

        if (!bIsDebugpyInstalled) {
            const selectedInstallOption = await vscode.window.showWarningMessage(
                "Python module 'debugpy' is required for debugging",
                "Install"
            );

            if (selectedInstallOption === "Install") {
                if (!await installDebugpy()) {
                    vscode.window.showErrorMessage("Failed to install 'debugpy'");
                    return;
                }
            }
            else {
                return;
            }

        }

        port = await getWantedPort();
        if (!port) {
            return;
        }

        if (!await startDebugpyServer(port)) {
            return;
        }
    }

    vscode.debug.startDebugging(undefined, {
        "name": utils.DEBUG_SESSION_NAME,
        "type": "python",
        "request": "attach",
        "connect": {
            "host": "localhost",
            "port": port
        }
    });


}
