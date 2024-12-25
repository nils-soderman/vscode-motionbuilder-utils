import * as vscode from 'vscode';

import * as crypto from 'crypto';

import { TextEncoder } from 'util';

import * as executeScript from '../scripts/execute-script';
import * as utils from '../modules/utils';


async function executeHandler(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    const textEncoder = new TextEncoder();

    for (let cell of cells) {
        const id = crypto.randomUUID();
        const baseFilename = executeScript.getExecBaseFilename(id);

        const code = cell.document.getText();
        const filepath = await utils.saveTempFile(baseFilename, code);

        const execution = controller.createNotebookCellExecution(cell);

        execution.start(new Date().getTime());

        const rawResponse = await executeScript.executeFile(filepath, notebook.uri.fsPath, id, false, true);
        if (rawResponse === null) {
            execution.end(false);
            return;
        }

        const executionStopTime = new Date().getTime();

        const outputItem = new vscode.NotebookCellOutputItem(textEncoder.encode(rawResponse), 'text/plain');

        // And then create a new output with that item
        const output = new vscode.NotebookCellOutput([outputItem]);

        execution.replaceOutput([output]);

        execution.end(true, executionStopTime);
    }
}


/**
 * Create a new notebook controller for MotionBuilder
 */
export function createNotebookController() {
    const controller = vscode.notebooks.createNotebookController("mobu-utils.notebook", "jupyter-notebook", "MotionBuilder", executeHandler);
    controller.supportsExecutionOrder = true;
    controller.description = "Executes the code in MotionBuilder";

    return controller;    
}