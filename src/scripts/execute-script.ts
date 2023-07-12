import * as vscode from 'vscode';

import * as path from 'path';
import * as fs from 'fs';

import * as uuid from 'uuid';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as vsCodeExec from '../modules/code-exec';
import * as utils from '../modules/utils';


const TEMP_FILENAME = "vscode_motionbuilder_exec";
const PYTHON_EXEC_FILE = path.join(utils.EXTENSION_PYTHON_DIR, "execute.py");

let gOutputChannel: vscode.OutputChannel | undefined;


/**
 * Get the output channel for this extension
 * @param bEnsureChannelExists If channel doesn't exist, create it
 */
function getOutputChannel(bEnsureChannelExists = true) {
    if (!gOutputChannel && bEnsureChannelExists) {
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder");
    }
    return gOutputChannel;
}


function getTempFilepath(id: string) {
    // replace all dashes in the uuid with underscores
    id = id.replace(/-/g, "_");
    return path.join(utils.getExtentionTempDir(), `${TEMP_FILENAME}-${id}.py`);
}

function getOutputFilepath(id: string) {
    return path.join(utils.getExtentionTempDir(), `exec-out-${id}.txt`);
}


/** Handle data recived from the MotionBuilder python server */
function handleResponse(response: string, id: string) {
    // If user is debugging MB, all output will automatically be appended to the debug console
    if (utils.isDebuggingMotionBuilder()) {
        return;
    }

    const extConfig = utils.getExtensionConfig();
    const outputChannel = getOutputChannel();

    // Clear the output channel if enabled in user settings
    if (extConfig.get("execute.clearOutput")) {
        if (outputChannel) {
            outputChannel.clear();
        }
    }

    // If the response was written to a file use that instead
    const outputFilepath = getOutputFilepath(id);
    if (fs.existsSync(outputFilepath)) {
        response = fs.readFileSync(outputFilepath, { encoding: "utf-8" }).toString();
        fs.unlink(outputFilepath, () => { });  // Delete the file
    }

    // Format response
    response = response.replace(/\n\r/g, "\n");
    response = `${response}>>>`;

    if (outputChannel) {
        // Add the message to the output channel
        outputChannel.appendLine(response);

        // Bring up the output channel on screen
        if (extConfig.get("execute.showOutput")) {
            outputChannel.show(true);
        }
    }
}

export async function execute() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const id = uuid.v4();

    const extConfig = utils.getExtensionConfig();
    const activeDocuemt = vscode.window.activeTextEditor.document;

    const tempFilepath = getTempFilepath(id);
    const fileToExecute = vsCodeExec.getFileToExecute(tempFilepath);
    if (!fileToExecute) {
        return;
    }

    let globals: any = {};
    globals["vsc_file"] = fileToExecute;
    globals["vsc_is_debugging"] = utils.isDebuggingMotionBuilder();
    globals["vsc_filename"] = activeDocuemt.uri.fsPath;
    globals["vsc_name"] = extConfig.get("execute.name");
    globals["vsc_id"] = id;

    const response = await motionBuilderConsole.executeFile(PYTHON_EXEC_FILE, globals);
    if (response) {
        handleResponse(response, id);
    }
}
