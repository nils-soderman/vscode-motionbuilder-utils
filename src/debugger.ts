import * as vscode from 'vscode';
import * as path from "path";

import * as motionBuilderConsole from './motionbuilder-console';
import * as utils from "./utils";

const TEMP_EXECDATA_FILENAME = "vscode-attach.json";
const START_DEBUG_SERVER_FILENAME = "start_debug_server.py";

function writeDataFile(port: number, targetInstallDir: String) {
    let data: any = {};
    data["port"] = port;
    data["target"] = targetInstallDir;
    utils.saveTempFile(TEMP_EXECDATA_FILENAME, JSON.stringify(data));
}

function serverStartCallback(data: string) {
    console.log("data: " + data);
    
    const port: number | undefined = utils.getExtensionConfig().get("debug.port");
    
    // Start debugging
    vscode.debug.startDebugging(undefined, {
        "name": utils.DEBUG_SESSION_NAME,
        "type": "python",
        "request": "attach",
        "port": port,
        "host": "localhost"
    });
}

export function attachToMotionBuilder() {
    const port: number | undefined = utils.getExtensionConfig().get("debug.port");
    if (!port) {
        return;
    }

    // Make sure user is not already in a debug session
    if (vscode.debug.activeDebugSession) {
        if (vscode.debug.activeDebugSession.name != utils.DEBUG_SESSION_NAME) {
            // Current debug session is not MotionBuilder, show a warning
            vscode.window.showErrorMessage("Another debug session is already running.\n Please close the current debug session before attaching to MotionBuilder.");
        }
        return;
    }

    // Start the MB debug server
    writeDataFile(port, utils.getExtensionPythonModulesDir());
    const startDebugPythonFilepath = path.join(utils.EXTENSION_PYTHON_DIR, START_DEBUG_SERVER_FILENAME);
    motionBuilderConsole.executeFile(startDebugPythonFilepath, serverStartCallback);
}

