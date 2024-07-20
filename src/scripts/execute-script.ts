import * as vscode from 'vscode';

import * as crypto from 'crypto';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as vsCodeExec from '../modules/code-exec';
import * as utils from '../modules/utils';


export function getExecBaseFilename(id: string) {
    // replace all dashes in the uuid with underscores
    id = id.replace(/-/g, "_");
    return `vscode_motionbuilder_exec_${id}.py`;
}


async function getExecAbsFilepath(id: string) {
    return vscode.Uri.joinPath(await utils.getExtentionTempDir(), getExecBaseFilename(id));
}


async function getOutputFilepath(id: string) {
    return vscode.Uri.joinPath(await utils.getExtentionTempDir(), `exec-out-${id}.txt`);
}


/** Handle data recived from the MotionBuilder python server */
function handleResponse(response: string, id: string) {
    // If user is debugging MB, all output will automatically be appended to the debug console
    if (utils.isDebuggingMotionBuilder()) {
        return;
    }

    const extConfig = utils.getExtensionConfig();
    const outputChannel = utils.getOutputChannel();

    // Clear the output channel if enabled in user settings
    if (extConfig.get("execute.clearOutput")) {
        outputChannel.clear();
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
    if (!vscode.window.activeTextEditor)
        return;

    const id = crypto.randomUUID();

    const activeDocuemt = vscode.window.activeTextEditor.document;

    const tempFilepath = await getExecAbsFilepath(id);
    const fileToExecute = await vsCodeExec.getFileToExecute(tempFilepath);
    if (!fileToExecute)
        return;

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
export async function executeFile(filepath: vscode.Uri, filename: string, id: string, bIsDebugging: boolean, bUseColors: boolean) {
    const extConfig = utils.getExtensionConfig();

    /* eslint-disable @typescript-eslint/naming-convention */
    const globals = {
        "vsc_file": filepath.fsPath,
        "vsc_is_debugging": bIsDebugging,
        "vsc_filename": filename,
        "vsc_name": extConfig.get("execute.name"),
        "vsc_id": id,
        "vsc_use_colors": bUseColors
    };
    /* eslint-enable @typescript-eslint/naming-convention */

    const pythonExecFile = vscode.Uri.joinPath(utils.getPythonDir(), "execute.py");
    let response = await motionBuilderConsole.executeFile(pythonExecFile, globals);
    if (response === null)
        return null;

    // If the response was written to a file use that instead
    const outputFilepath = await getOutputFilepath(id);
    if (await utils.uriExists(outputFilepath)) {
        response = (await vscode.workspace.fs.readFile(outputFilepath)).toString();
        response = response.replace(/\r\n/g, "\n");
        vscode.workspace.fs.delete(outputFilepath);
    }

    return response;
}
