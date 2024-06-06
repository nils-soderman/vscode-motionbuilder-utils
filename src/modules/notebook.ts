import * as vscode from 'vscode';

import * as crypto from 'crypto';
import * as path from 'path';

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
async function executeHandlerNoIPython(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    for (let cell of cells) {
        const execution = controller.createNotebookCellExecution(cell);
        execution.start();

        const id = crypto.randomUUID();
        const baseFilename = executeScript.getExecBaseFilename(id);

        const code = cell.document.getText();
        const filepath = utils.saveTempFile(baseFilename, code);

        // const pythonExecFile = path.join(utils.getPythonDir(), "notebook", "notebook.py");

        // const response = await motionBuilderConsole.executeFile(pythonExecFile, {
        //     vsc_code: code // eslint-disable-line @typescript-eslint/naming-convention
        // });
        // console.log("response: " + response);

        const rawResponse = await executeScript.executeFile(filepath, notebook.uri.fsPath, id, false, true);
        if (rawResponse === null) {
            execution.end(false);
            return;
        }

        const outputItem = new vscode.NotebookCellOutputItem(new TextEncoder().encode(rawResponse), 'text/plain');

        // And then create a new output with that item
        const output = new vscode.NotebookCellOutput([outputItem]);

        execution.replaceOutput([output]);

        execution.end(true);
    }
}


async function executeHandler(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    if (cachedIsIPythonInstalled === null) {
        cachedIsIPythonInstalled = await isIPythonInstalled();
    }

    if (!cachedIsIPythonInstalled || true) {
        executeHandlerNoIPython(cells, notebook, controller);
        return;
    }
    else {
        // executeHandlerIPython(cells, notebook, controller);
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