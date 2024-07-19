import * as vscode from 'vscode';

let gOutputChannel: vscode.OutputChannel | undefined;

export function getOutputChannel() {
    if (!gOutputChannel)
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder Log");

    return gOutputChannel;
}

export function showLog() {
    const outputChannel = getOutputChannel();
    outputChannel.show(true);
}


export function log(message: string) {
    const outputChannel = getOutputChannel();
    outputChannel.appendLine(message);
}

export async function showErrorMessage(message: string, fullError: string) {
    log(fullError);

    const selectedValue = await vscode.window.showErrorMessage(message, "Show log");
    if (selectedValue == "Show log")
        showLog();
}