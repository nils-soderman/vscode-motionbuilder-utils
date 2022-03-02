import * as vscode from 'vscode';

import * as path from 'path';

import * as motionBuilderConsole from './motionbuilder-console';
import * as utils from './utils';


const TEMP_FILENAME = "VSCode-MotionBuilder-Exec";
const TEMP_EXECDATA_FILENAME = "vscode-exec.json";
const PYTHON_ENTER_FILE = path.join(utils.EXTENSION_PYTHON_DIR, "execute.py");

let gOutputChannel: vscode.OutputChannel;


function getOutputChannel(bEnsureChannelExists = true) {
    if (!gOutputChannel && bEnsureChannelExists) {
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder");
    }
    return gOutputChannel;
}


function handleResponse(response: string) {
    // If user is debugging MB, all output will automatically be appended to the debug console
    if (vscode.debug.activeDebugSession && vscode.debug.activeDebugSession.name == utils.DEBUG_SESSION_NAME) {
        return;
    }

    // Format response
    response = response.replace(/\n\r/g, "\n");

    const traceBackString = "Traceback (most recent call last):\n";
    if (response.includes(traceBackString)) {
        const responseTracebackSplit = response.split(traceBackString, 2);
        const tracebackMsg = responseTracebackSplit[1].split("\n").slice(2).join("\n");
        response = responseTracebackSplit[0] + traceBackString + tracebackMsg;
    }

    // Log the message in the output channel
    const outputChannel = getOutputChannel();
    outputChannel.appendLine(response);


    if (utils.getExtensionConfig().get("execute.showOutput")) {
        outputChannel.show(true);
    }
}


/**
 * Write a json temp file that can be read by MotionBuilder, to know what script to execute etc.
 * @param fileToExecute The abs filepath to the .py file that should be executed
 * @param originalFilepath The abs filepath to the source filepath, will be used to set the python var `__file__`
 */
function writeDataFile(fileToExecute: string, originalFilepath: string) {
    let data: any = {};
    data["file"] = fileToExecute;
    data["__file__"] = originalFilepath;
    utils.saveTempFile(TEMP_EXECDATA_FILENAME, JSON.stringify(data));
}


/**
 * Try to make sure the text is runnable
 * @param text
 * @param firstCharIndex
 */
function formatSelectedText(text: string, firstCharIndex: number) {
    if (firstCharIndex <= 0) {
        return text;
    }

    let formattedText = "";
    let charactersToRemove = firstCharIndex;
    let i = 0;
    for (let line of text.split("\n")) {
        if (charactersToRemove) {
            if (i == 0) {
                line = line.trimStart();
            }
            else {
                const numberOfWhitespaceCharacters = line.length - line.trimStart().length;
                if (numberOfWhitespaceCharacters < charactersToRemove) {
                    charactersToRemove = numberOfWhitespaceCharacters;
                }
                line = line.slice(charactersToRemove);
            }
        }

        formattedText += line + "\n";
        i++;
    }

    return formattedText;

}


export async function execute() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const activeDocuemt = vscode.window.activeTextEditor.document;
    let selectionText = "";

    // Combine all user selections into a single string
    for (let selection of vscode.window.activeTextEditor.selections) {
        if (!selection.isEmpty) {

            // Get the first line that is not empty
            let firstChar = -1;
            for (let i = 0; i < selection.end.line - selection.start.line; i++) {
                const line = activeDocuemt.lineAt(selection.start.line + i);
                if (!line.isEmptyOrWhitespace) {
                    firstChar = line.firstNonWhitespaceCharacterIndex;
                    break;
                }
            }

            selectionText += formatSelectedText(activeDocuemt.getText(selection), firstChar) + "\n";
        }
    }

    let fileToExecute = "";
    // If user had any selected text, save the selection as a temp file to execute
    if (selectionText) {
        fileToExecute = utils.saveTempFile(TEMP_FILENAME, selectionText);
    }

    else if (activeDocuemt.isDirty) {
        // File is dirty, save a copy of the currenet text in temp
        fileToExecute = utils.saveTempFile(TEMP_FILENAME, activeDocuemt.getText());
    }

    else {
        fileToExecute = activeDocuemt.uri.fsPath;
    }

    // File an info file telling mb what script to run, etc.
    writeDataFile(fileToExecute, activeDocuemt.uri.fsPath);

    if (utils.getExtensionConfig().get("execute.clearOutput")) {
        const outputChannel = getOutputChannel(false);
        if (outputChannel) {
            outputChannel.clear();
        }
    }

    motionBuilderConsole.executeFile(PYTHON_ENTER_FILE, handleResponse);

}

