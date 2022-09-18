import * as vscode from 'vscode';

import * as path from 'path';
import * as fs   from 'fs';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as vsCodeExec         from '../modules/code-exec';
import * as utils                from '../modules/utils';


const TEMP_FILENAME = "vscode_motionbuilder_exec.py";
const TEMP_EXECDATA_FILENAME = "vscode-exec.json";
const PYTHON_EXEC_FILE = path.join(utils.EXTENSION_PYTHON_DIR, "execute.py");
const OUTPUT_FILEPATH = path.join(utils.getExtentionTempDir(), "vscode-exec-out.txt");

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


function readResponse() {
    if (fs.existsSync(OUTPUT_FILEPATH)) {
        return fs.readFileSync(OUTPUT_FILEPATH).toString("utf8");
    }
    return "";
}


/** Handle data recived from the MotionBuilder python server */
function handleResponse(response: string) {
    // If user is debugging MB, all output will automatically be appended to the debug console
    if (utils.isDebuggingMotionBuilder()) {
        return;
    }

    response = response.trim();

    if (response == ">>>") {
        const parsedResponse = readResponse();
        if (parsedResponse) {
            response = `${parsedResponse}>>>`;
        }
    }

    // Format response
    response = response.replace(/\n\r/g, "\n");

    const outputChannel = getOutputChannel();
    if (outputChannel) {
        // Add the message to the output channel
        outputChannel.appendLine(response);

        // Bring up the output channel on screen
        if (utils.getExtensionConfig().get("execute.showOutput")) {
            outputChannel.show(true);
        }
    }
}


/**
 * Write a json temp file that can be read by MotionBuilder, to know what script to execute etc.
 * @param fileToExecute The abs filepath to the .py file that should be executed
 * @param originalFilepath The abs filepath to the source filepath, will be used to set the python var `__file__`
 * @param additionalPrint Additional text to be printed to the output once the code has been executed
 */
function writeDataFile(fileToExecute: string, originalFilepath: string, bIsDebugging = true, additionalPrint = "", nameVariable = "") {
    let data: any = {};
    
    data["file"] = fileToExecute;
    data["is_debugging"] = bIsDebugging;
    data["__file__"] = originalFilepath;
    data["__name__"] = nameVariable;
    
    if (additionalPrint) {
        data["additionalPrint"] = additionalPrint;
    }
    utils.saveTempFile(TEMP_EXECDATA_FILENAME, JSON.stringify(data));
}


export async function execute() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const extConfig = utils.getExtensionConfig();
    const activeDocuemt = vscode.window.activeTextEditor.document;

    const tempFilepath = path.join(utils.getExtentionTempDir(), TEMP_FILENAME);
    let fileToExecute = vsCodeExec.getFileToExecute(tempFilepath);
    if (!fileToExecute) {
        return;
    }

    // File an info file telling mb what script to run, etc.
    const bIsDebugging = utils.isDebuggingMotionBuilder();
    const additionalPrint = bIsDebugging ? ">>>" : "";
    const nameVar: string | undefined = extConfig.get("execute.name");

    writeDataFile(fileToExecute, activeDocuemt.uri.fsPath, bIsDebugging, additionalPrint, nameVar);

    // Clear the output channel if enabled in user settings
    if (extConfig.get("execute.clearOutput")) {
        const outputChannel = getOutputChannel(false);
        if (outputChannel) {
            outputChannel.clear();
        }
    }

    motionBuilderConsole.executeFile(PYTHON_EXEC_FILE, handleResponse);
}
