import * as vscode from 'vscode';

import * as crypto from 'crypto';
import * as path from 'path';
import * as fs from 'fs';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as vsCodeExec from '../modules/code-exec';
import * as utils from '../modules/utils';


let gOutputChannel: vscode.OutputChannel | undefined;



/**
 * Get the output channel for this extension
 * @param bEnsureChannelExists If channel doesn't exist, create it
 */
function getOutputChannel() {
    if (!gOutputChannel) {
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder Output");
    }
    return gOutputChannel;
}


export function getExecBaseFilename(id: string) {
    // replace all dashes in the uuid with underscores
    id = id.replace(/-/g, "_");
    return `vscode_motionbuilder_exec_${id}.py`;
}


function getExecAbsFilepath(id: string) {
    return path.join(utils.getExtentionTempDir(), getExecBaseFilename(id));
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
        outputChannel.clear();
    }

    // If the response was written to a file use that instead
    const outputFilepath = getOutputFilepath(id);
    if (fs.existsSync(outputFilepath)) {
        response = fs.readFileSync(outputFilepath, { encoding: "utf-8" }).toString();
        fs.unlink(outputFilepath, () => { });  // Delete the file
    }

    // Format response
    if (response) {
        response += "\n";
    }
    response += ">>>";

    // Add the message to the output channel
    outputChannel.appendLine(response);

    // Bring up the output channel on screen
    if (extConfig.get("execute.showOutput")) {
        outputChannel.show(true);
    }
}

export async function executeCurrentDocument() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const id = crypto.randomUUID();

    const activeDocuemt = vscode.window.activeTextEditor.document;

    const tempFilepath = getExecAbsFilepath(id);
    const fileToExecute = vsCodeExec.getFileToExecute(tempFilepath);
    if (!fileToExecute) {
        return;
    }

    const bIsDebugging = utils.isDebuggingMotionBuilder();
    const response = await executeFile(fileToExecute, activeDocuemt.uri.fsPath, id, bIsDebugging, bIsDebugging);
    if (response !== null) {
        handleResponse(response, id);
    }
}


/**
 * @param filepath The absolute filepath to the file containing the code to execute
 * @param filename The absolute filepath to use as the __file__ variable in the python script
 * @param id UUID to use for the output file
 * @param bIsDebugging If true, the python script will assume debugpy handles the output
 * @returns The output from the python script
 */
export async function executeFile(filepath: string, filename: string, id: string, bIsDebugging: boolean, bUseColors: boolean) {
    const extConfig = utils.getExtensionConfig();

    /* eslint-disable @typescript-eslint/naming-convention */
    const globals = {
        "vsc_file": filepath,
        "vsc_is_debugging": bIsDebugging,
        "vsc_filename": filename,
        "vsc_name": extConfig.get("execute.name"),
        "vsc_id": id,
        "vsc_use_colors": bUseColors
    };
    /* eslint-enable @typescript-eslint/naming-convention */

    const pythonExecFile = path.join(utils.getPythonDir(), "execute.py");
    let response = await motionBuilderConsole.executeFile(pythonExecFile, globals);
    if (response === null)
        return null;

    // If the response was written to a file use that instead
    const outputFilepath = getOutputFilepath(id);
    if (fs.existsSync(outputFilepath)) {
        response = fs.readFileSync(outputFilepath, { encoding: "utf-8" }).toString();
        fs.unlink(outputFilepath, () => { });  // Delete the file
    }

    response = response.replace(/\n\r/g, "\n");

    return response;
}