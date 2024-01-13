import * as vscode from 'vscode';

import * as crypto from 'crypto';

import * as executeScript from '../scripts/execute-script';
import * as utils from '../modules/utils';
import { TextEncoder } from 'util';

export function setupNotebook(context: vscode.ExtensionContext) {
    const controller = vscode.notebooks.createNotebookController("mobu-utils.notebook", "jupyter-notebook", "MotionBuilder", executeHandler);
    controller.supportsExecutionOrder = true;

    context.subscriptions.push(controller);
}

async function executeHandler(cells: vscode.NotebookCell[], notebook: vscode.NotebookDocument, controller: vscode.NotebookController) {
    for (let cell of cells) {
        const execution = controller.createNotebookCellExecution(cell);
        execution.start();

        const id = crypto.randomUUID();
        const baseFilename = executeScript.getExecBaseFilename(id);

        let code = cell.document.getText();
        const filepath = utils.saveTempFile(baseFilename, code);

        const response = await executeScript.executeFile(filepath, notebook.uri.fsPath, id, false);
        if (response === null) {
            execution.end(false);
            return;
        }

        const outputItem = new vscode.NotebookCellOutputItem(new TextEncoder().encode(response), 'text/plain');

        // And then create a new output with that item
        const output = new vscode.NotebookCellOutput([outputItem]);

        execution.replaceOutput([output]);

        execution.end(true);
    }
}
