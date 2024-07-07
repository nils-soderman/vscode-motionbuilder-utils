import * as vscode from 'vscode';

import * as crypto from 'crypto';
import * as path from 'path';
import * as fs from 'fs';

import { TextEncoder } from 'util';

import * as motionBuilderConsole from '../modules/motionbuilder-console';
import * as executeScript from '../scripts/execute-script';
import * as logging from '../modules/logging';
import * as utils from '../modules/utils';

let cachedIsIPythonInstalled: boolean | null = null;


/**
 * Check if IPython is installed in the Python environment.
 * @returns True if IPython is installed, false if it is not, and null if it could not be determined.
 */
async function isIPythonInstalled(): Promise<boolean | null> {
    const successId = crypto.randomUUID();

    const scriptPath = path.join(utils.getPythonDir(), "notebook", "is_ipython_installed.py");
    let response = await motionBuilderConsole.executeFile(scriptPath,
        {
            vsc_suceess_id: successId, // eslint-disable-line @typescript-eslint/naming-convention
        }
    );

    if (response === null) {
        return null;
    }

    let bSuccess = false;
    for (let line of response.split(/\r\n|\r|\n/)) {
        if (line === successId) {
            bSuccess = true;
        }
        else if (line) {
            logging.logMessage(line);
        }
    }

    return bSuccess;
}


/**
 * Execute the cells in the notebook without IPython
 */
async function executeHandlerBasic(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    for (let cell of cells) {
        const id = crypto.randomUUID();
        const baseFilename = executeScript.getExecBaseFilename(id);

        const code = cell.document.getText();
        const filepath = utils.saveTempFile(baseFilename, code);

        const execution = controller.createNotebookCellExecution(cell);

        execution.start(new Date().getTime());

        const rawResponse = await executeScript.executeFile(filepath, notebook.uri.fsPath, id, false, true);
        if (rawResponse === null) {
            execution.end(false);
            return;
        }

        const executionStopTime = new Date().getTime();

        const outputItem = new vscode.NotebookCellOutputItem(new TextEncoder().encode(rawResponse), 'text/plain');

        // And then create a new output with that item
        const output = new vscode.NotebookCellOutput([outputItem]);

        execution.replaceOutput([output]);

        execution.end(true, executionStopTime);
    }
}


/**
 * Execute the cells in the notebook with IPython features
 */
async function executeHandlerIPython(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    for (let cell of cells) {
        const execution = controller.createNotebookCellExecution(cell);
        execution.start(new Date().getTime());

        const id = crypto.randomUUID();
        const baseFilename = executeScript.getExecBaseFilename(id);

        const code = cell.document.getText();
        const filepath = utils.saveTempFile(baseFilename, code);

        const pythonExecFile = path.join(utils.getPythonDir(), "notebook", "notebook.py");

        let response = await motionBuilderConsole.executeFile(pythonExecFile, {
            vsc_code: code, // eslint-disable-line @typescript-eslint/naming-convention
            vsc_command_id: id, // eslint-disable-line @typescript-eslint/naming-convention
        });

        const executionStopTime = new Date().getTime();

        if (response === null) {
            execution.end(false);
            return;
        }

        const outputFilepath = executeScript.getOutputFilepath(id);
        if (fs.existsSync(outputFilepath)) {
            response = fs.readFileSync(outputFilepath, { encoding: "utf-8" }).toString();
            fs.unlink(outputFilepath, () => { });  // Delete the file
        }

        console.log(response);

        // Parse the response
        let responseObj = [];
        try{
            responseObj = JSON.parse(response);
        }
        catch (e) {
            logging.logMessage(`Error parsing response: ${response}\n${e}`);
            execution.end(false);
            return;
        }
        let outputs = [];

        // Replace the cell's output with the response
        for (const key in responseObj) {
            const outputItems: vscode.NotebookCellOutputItem[] = [];
            const value = responseObj[key]; // = {"text/plain": "<IPython.core.display.Markdown object>", "text/markdown": "## Hello World!"}
            for (const mimeType in value) {
                const data = value[mimeType];

                let outputItem: vscode.NotebookCellOutputItem;
                if (mimeType === 'image/png' || mimeType === 'image/jpeg' || mimeType === 'image/svg+xml') {
                    const buffer = Buffer.from(data, 'base64');
                    outputItem = new vscode.NotebookCellOutputItem(buffer, mimeType);
                }
                else {
                    outputItem = new vscode.NotebookCellOutputItem(new TextEncoder().encode(data), mimeType);
                }

                outputItems.push(outputItem);
            }
            const output = new vscode.NotebookCellOutput(outputItems);
            outputs.push(output);
        }

        execution.replaceOutput(outputs);

        execution.end(true, executionStopTime);
    }
}



async function executeHandler(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    if (cachedIsIPythonInstalled === null) {
        cachedIsIPythonInstalled = await isIPythonInstalled();
    }

    if (!cachedIsIPythonInstalled) {
        executeHandlerBasic(cells, notebook, controller);
    }
    else {
        executeHandlerIPython(cells, notebook, controller);
    }
}


/**
 * Setup the notebook controller
 * @param context The extension context
 */
export function setupNotebook(context: vscode.ExtensionContext) {
    const controller = vscode.notebooks.createNotebookController("mobu-utils.notebook", "jupyter-notebook", "MotionBuilder", executeHandler);
    controller.supportsExecutionOrder = true;

    context.subscriptions.push(controller);
}