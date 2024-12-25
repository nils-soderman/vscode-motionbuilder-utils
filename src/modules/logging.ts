import * as vscode from 'vscode';

const LOG_CHANNEL_NAME = "MotionBuilder Log";
let gOutputChannel: vscode.OutputChannel | undefined;

export function getOutputChannel() {
    if (!gOutputChannel)
        gOutputChannel = vscode.window.createOutputChannel(LOG_CHANNEL_NAME);

    return gOutputChannel;
}

export function showLog() {
    const outputChannel = getOutputChannel();
    outputChannel.show(true);
}

export function log(message: string) {
    const outputChannel = getOutputChannel();
    const timestamp = new Date().toISOString();
    outputChannel.appendLine(`[${timestamp}] ${message}`);
}

export async function showErrorMessage(message: string, error: Error) {
    log(`${error.name}: ${error.message}`);

    const SHOW_LOG_OPTION = "Show log";
    const selectedValue = await vscode.window.showErrorMessage(message, SHOW_LOG_OPTION);
    if (selectedValue === SHOW_LOG_OPTION)
        showLog();
}