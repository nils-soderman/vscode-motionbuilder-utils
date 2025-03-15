import * as vscode from 'vscode';

const LOG_CHANNEL_NAME = "MotionBuilder Log";
let gOutputChannel: vscode.LogOutputChannel | undefined;


/**
 * Get the output channel for logging, creating it if it doesn't exist.
 */
export function getOutputChannel() {
    if (!gOutputChannel)
        gOutputChannel = vscode.window.createOutputChannel(LOG_CHANNEL_NAME, { log: true });

    return gOutputChannel;
}


/**
 * Log a message to the output channel.
 */
export function log(message: string) {
    const outputChannel = getOutputChannel();
    outputChannel.info(message);
}


/**
 * Log an error message to the output channel.
 */
export function logError(error: string | Error) {
    const outputChannel = getOutputChannel();
    outputChannel.error(error);
}


/**
 * Show an error message to the user and log the error.
 * Error message will include a "Show log" option that will open the log output channel.
 * @param message The message to show to the user.
 * @param error The error to log.
 */
export async function showErrorMessage(message: string, error: Error) {
    const outputChannel = getOutputChannel();
    outputChannel.error(error.message);

    const SHOW_LOG_OPTION = "Show log";
    const selectedValue = await vscode.window.showErrorMessage(message, SHOW_LOG_OPTION);
    if (selectedValue === SHOW_LOG_OPTION)
        outputChannel.show(true);
}