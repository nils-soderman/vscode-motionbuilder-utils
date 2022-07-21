import * as vscode from 'vscode';

import * as path from "path";
import * as fs   from "fs";

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as utils                from "../modules/utils";


const TEMP_EXECDATA_FILENAME = "vscode-attach.json";
const TEMP_EXECOUTPUT_FILENAME = "vscode-attach-out.txt";
const START_DEBUG_SERVER_FILENAME = "start_debug_server.py";

let gLastDebugAttempt: number = 0;


function writeDataFile(port: number, targetInstallDir: String) {
    let data: any = {};
    data["port"] = port;
    data["target"] = targetInstallDir;
    utils.saveTempFile(TEMP_EXECDATA_FILENAME, JSON.stringify(data));
}

function readResponse() {
    const outputFilepath = path.join(utils.getExtentionTempDir(), TEMP_EXECOUTPUT_FILENAME);
    if (fs.existsSync(outputFilepath)) {
        const response = fs.readFileSync(outputFilepath).toString("utf8");
        return response;
    }
    return "";
}


function serverStartCallback(data: string) {
    const currentTime = new Date().getTime();
    const deltaTime = (currentTime - gLastDebugAttempt) / 1000;
    gLastDebugAttempt = currentTime;

    // If a call is made within ~half a second, Then this is the same
    // call, just more data beeing passed along from the MB python server
    if (deltaTime < 0.5) {
        return;
    }

    if (utils.isDebuggingMotionBuilder()) {
        return;
    }

    const response = readResponse();

    if (response.startsWith("ERROR:")) {
        let message = response.replace("ERROR:", "").replace(">>>", "").trim();
        vscode.window.showErrorMessage(message);
        return;
    }

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

    if (utils.isDebuggingMotionBuilder()) {
        return;
    }

    // Start the MB debug server
    writeDataFile(port, utils.getExtensionPythonModulesDir());
    const startDebugPythonFilepath = path.join(utils.EXTENSION_PYTHON_DIR, START_DEBUG_SERVER_FILENAME);
    motionBuilderConsole.executeFile(startDebugPythonFilepath, serverStartCallback);
}
