import * as vscode from 'vscode';

import * as path from 'path';
import * as fs   from 'fs';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
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


/**
 * Try to make sure the text is runnable
 * This includes e.g. making sure that all of the text is not indented
 * @param text The text to format
 * @param firstCharIndex Index of the first character (how far it's indented)
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


/**
 * Get the selection as an python executable string
 */
function getSelectedTextAsExecutableString() {
    if (!vscode.window.activeTextEditor) {
        return;
    }

    const activeDocuemt = vscode.window.activeTextEditor.document;
    let executableCodeText = "";

    let selections: Array<vscode.Selection> = [vscode.window.activeTextEditor.selection];

    // If there are more than 1 selection, sort them by their start line number
    if (vscode.window.activeTextEditor.selections.length > 1) {
        // Add selections into an array that we can run the sort function on
        selections = [];
        for (const selection of vscode.window.activeTextEditor.selections) {
            selections.push(selection);
        }

        selections = selections.sort(function (a: any, b: any) {
            return a.start.line - b.start.line;
        });
    }

    // Combine all user selections into a single string
    for (const selection of selections) {
        if (!selection.isEmpty) {

            // Get the character index of the first character that's not whitespace (on the first line that's not whitespace)
            let firstCharIndex = -1;
            for (let i = 0; i < selection.end.line - selection.start.line; i++) {
                const line = activeDocuemt.lineAt(selection.start.line + i);
                if (!line.isEmptyOrWhitespace) {
                    firstCharIndex = line.firstNonWhitespaceCharacterIndex;
                    break;
                }
            }

            // Add empty lines to match line numbers with the actual source file.
            // This is to make sure you get correct line numbers for error messages & to make sure
            // breakpoints work correctly.
            const numberOfLines = executableCodeText.split("\n").length - 1;
            const additionalEmptyLines = "\n".repeat(selection.start.line - numberOfLines);

            executableCodeText += additionalEmptyLines + formatSelectedText(activeDocuemt.getText(selection), firstCharIndex);
        }
    }

    return executableCodeText;
}


export async function execute() {
    if (!vscode.window.activeTextEditor) {
        return;
    }
    const extConfig = utils.getExtensionConfig();
    const activeDocuemt = vscode.window.activeTextEditor.document;
    const selectedCode = getSelectedTextAsExecutableString();

    let fileToExecute = "";

    // If user has any selected text, save the selection as a temp file to execute
    if (selectedCode) {
        fileToExecute = utils.saveTempFile(TEMP_FILENAME, selectedCode);
    }

    // If file is dirty, save a copy of the text and execute that copy instead
    else if (activeDocuemt.isDirty) {
        fileToExecute = utils.saveTempFile(TEMP_FILENAME, activeDocuemt.getText());
    }

    else {
        fileToExecute = activeDocuemt.uri.fsPath;
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
