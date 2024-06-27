import * as vscode from 'vscode';

import * as crypto from 'crypto';
import * as path from 'path';
import * as fs from 'fs';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as vsCodeExec from '../modules/code-exec';
import * as utils from '../modules/utils';


const TEMP_FILENAME = "vscode_motionbuilder_exec";

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


function getTempFilepath(id: string) {
    // replace all dashes in the uuid with underscores
    id = id.replace(/-/g, "_");
    return path.join(utils.getExtentionTempDir(), `${TEMP_FILENAME}_${id}.py`);
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


/**
 * Get all current workspace folders as an array of strings
 */
function getWorkspaceFolders(): string[] {
    const folders = vscode.workspace.workspaceFolders;
    if (!folders) {
        return [];
    }

    return folders.map((folder) => folder.uri.fsPath);
}


export async function execute() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const id = crypto.randomUUID();

    const extConfig = utils.getExtensionConfig();
    const activeDocuemt = vscode.window.activeTextEditor.document;

    const tempFilepath = getTempFilepath(id);
    const fileToExecute = vsCodeExec.getFileToExecute(tempFilepath);
    if (!fileToExecute) {
        return;
    }

    /* eslint-disable @typescript-eslint/naming-convention */
    const globals: any = {
        vsc_id: id,
        vsc_file: fileToExecute,
        vsc_is_debugging: utils.isDebuggingMotionBuilder(),
        vsc_filename: activeDocuemt.uri.fsPath,
        vsc_name: extConfig.get("execute.name"),
    };
    /* eslint-enable @typescript-eslint/naming-convention */

    const pythonExecFile = path.join(utils.getPythonDir(), "execute.py");
    const response = await motionBuilderConsole.executeFile(pythonExecFile, globals);
    if (response !== null) {
        handleResponse(response, id);
    }
}
