import * as vscode from 'vscode';

const LOG_CHANNEL_NAME = "MotionBuilder Log";
let gOutputChannel: vscode.LogOutputChannel | undefined;

export function getOutputChannel() {
    if (!gOutputChannel)
        gOutputChannel = vscode.window.createOutputChannel(LOG_CHANNEL_NAME, { log: true });

    return gOutputChannel;
}

export function log(message: string) {
    const outputChannel = getOutputChannel();
    outputChannel.info(message);
}

export async function showErrorMessage(message: string, error: Error) {
    const outputChannel = getOutputChannel();
    outputChannel.error(error.message);

    const SHOW_LOG_OPTION = "Show log";
    const selectedValue = await vscode.window.showErrorMessage(message, SHOW_LOG_OPTION);
    if (selectedValue === SHOW_LOG_OPTION)
        outputChannel.show(true);
}