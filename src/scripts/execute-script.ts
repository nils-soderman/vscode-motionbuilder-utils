import * as vscode from 'vscode';

import * as crypto from 'crypto';
import * as path from 'path';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as vsCodeExec from '../modules/code-exec';
import * as logging from '../modules/logging';
import * as reload from './reload-modules';
import * as utils from '../modules/utils';

let cachedEntryPointPath: vscode.Uri | null = null;


export function getExecBaseFilename(id: string) {
    // replace all dashes in the uuid with underscores
    id = id.replace(/-/g, "_");
    return `vscode_motionbuilder_exec_${id}.py`;
}


async function getTmpExecUri(id: string) {
    return vscode.Uri.joinPath(await utils.getExtensionTempDir(), getExecBaseFilename(id));
}


async function getOutputFilepath(id: string) {
    return vscode.Uri.joinPath(await utils.getExtensionTempDir(), `exec-out-${id}.txt`);
}


/** Handle data received from the MotionBuilder python server */
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


/**
 * Execute the currently active document
 * If anything is selected in the document, only the selected code will be executed
 */
export async function executeCurrentDocument() {
    if (!vscode.window.activeTextEditor)
        return;

    const id = crypto.randomUUID();

    const activeDocument = vscode.window.activeTextEditor.document;

    const tempUri = await getTmpExecUri(id);
    const executeUri = await vsCodeExec.getFileToExecute(tempUri);
    if (!executeUri)
        return;

    const isDebugging = utils.isDebuggingMotionBuilder();
    const response = await executeFile(executeUri, activeDocument.uri.fsPath, id, isDebugging, isDebugging);
    if (response !== null)
        handleResponse(response, id);

    if (executeUri === tempUri)
        vscode.workspace.fs.delete(tempUri, { recursive: false });
}


/**
 * Execute a predefined entry point script
 */
export async function executeEntryPoint() {
    const extConfig = utils.getExtensionConfig();
    const entryPointPath = extConfig.get<string>("execute.entryPointPath");

    let fileUri: vscode.Uri | undefined = undefined;
    if (entryPointPath) {
        if (path.isAbsolute(entryPointPath)) {
            fileUri = vscode.Uri.file(entryPointPath);
        }
        else {
            const workspaceFolders = vscode.workspace.workspaceFolders;
            for (const folder of workspaceFolders || []) {
                const possiblePath = path.join(folder.uri.fsPath, entryPointPath);
                if (await utils.uriExists(vscode.Uri.file(possiblePath))) {
                    fileUri = vscode.Uri.file(possiblePath);
                    break;
                }
            }
        }

        if (!fileUri || !await utils.uriExists(fileUri)) {
            logging.logError(`Entry point path does not exist: ${entryPointPath}`);
            vscode.window.showErrorMessage(`Entry point path does not exist: ${entryPointPath}`);
            return;
        }

    }
    else if (cachedEntryPointPath && await utils.uriExists(cachedEntryPointPath)) {
        fileUri = cachedEntryPointPath;
    }
    else {
        const files = await vscode.workspace.findFiles('**/*.py', '**/env/**');
        const items = files.map(file => {
            let label = file.fsPath;
            const workspaceFolder = vscode.workspace.getWorkspaceFolder(file);
            if (workspaceFolder) {
                label = vscode.workspace.asRelativePath(file);
            }
            return { label: label, description: file.fsPath };
        });

        const selected = await vscode.window.showQuickPick(items, {
            placeHolder: "Select a entry point to execute",
            canPickMany: false,
            title: "Execute Entry Point"
        });

        if (!selected) {
            return;
        }

        cachedEntryPointPath = vscode.Uri.file(selected.description);
        fileUri = cachedEntryPointPath;
    }

    const id = crypto.randomUUID();

    if (extConfig.get<boolean>("execute.entryPointReload")) {
        await reload.main();
    }

    const isDebugging = utils.isDebuggingMotionBuilder();
    const response = await executeFile(fileUri, fileUri.fsPath, id, isDebugging, isDebugging);
    if (response !== null)
        handleResponse(response, id);
}


/**
 * @param scriptUri The absolute filepath to the file containing the code to execute
 * @param filename The absolute filepath to use as the __file__ variable in the python script
 * @param id UUID to use for the output file
 * @param bIsDebugging If true, the python script will assume debugpy handles the output
 * @returns The output from the python script
 */
export async function executeFile(scriptUri: vscode.Uri, filename: string, id: string, bIsDebugging: boolean, bUseColors: boolean) {
    const extConfig = utils.getExtensionConfig();

    /* eslint-disable @typescript-eslint/naming-convention */
    const globals = {
        "vsc_file": scriptUri.fsPath,
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
