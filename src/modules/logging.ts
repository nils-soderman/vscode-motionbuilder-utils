import * as vscode from 'vscode';

let gOutputChannel: vscode.OutputChannel | undefined;

export function getOutputChannel() {
    if (!gOutputChannel)
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder Utils Log");

    return gOutputChannel;
}


export function logMessage(message: string, bShowLog = false) {
    message = message.replace(/\n\r/g, "\n");
    
    const outputChannel = getOutputChannel();
    outputChannel.appendLine(message);

    if (bShowLog)
        outputChannel.show(true);
}

export async function showErrorMessage(message: string, fullError: string) {
    const additionalInfo = "Please consider opening an issue on GitHub with the error message above.";
    fullError = fullError + "\n\n" + additionalInfo;

    const selectedValue = await vscode.window.showErrorMessage(message, "Show error");
    if (selectedValue == "Show error")
        logMessage(fullError, true);
}