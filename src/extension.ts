import * as vscode from 'vscode';

import * as notebook from './modules/notebook';
import * as utils from './modules/utils';

import * as codeCompletion from './scripts/code-completion';
import * as documentation from './scripts/documentation';
import * as reloadModules from './scripts/reload-modules';
import * as execute from './scripts/execute-script';
import * as attach from './scripts/attach';
import * as docs from './modules/documentation';


export function activate(context: vscode.ExtensionContext) {
	utils.setExtensionUri(context.extensionUri);

	// Run Scripts
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.execute', () => {
			return execute.executeCurrentDocument();
		})
	);

	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.reloadModules', () => {
			return reloadModules.main();
		})
	);

	// Debugging
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.attach', () => {
			return attach.main(context);
		})
	);

	// Setup Code Completion
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.setupCodeCompletion', () => {
			return codeCompletion.main(context);
		})
	);

	// Browse pyfbsdk Documentation
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentationPython', () => {
			return documentation.browseDocumentation(context);
		})
	);

	// Browse Examples
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentationExamples', () => {
			return documentation.browseExamples(context);
		})
	);

	context.subscriptions.push(notebook.createNotebookController());

	const treeProvider = new docs.PyfbsdkTreeProvider();

	const searchProvider = new docs.PyfbsdkApiSearchProvider(context.extensionUri);

	const detailsProvider = new docs.PyfbsdkDetailsProvider(context.extensionUri);

	searchProvider.onInputChange(treeProvider.applyFilter.bind(treeProvider));


	context.subscriptions.push(
		vscode.window.registerWebviewViewProvider(
			'motionbuilder.pyfbsdk-api.search',
			searchProvider
		));

	context.subscriptions.push(
		vscode.window.registerTreeDataProvider(
			'motionbuilder.pyfbsdk-api.content',
			treeProvider
		));

	context.subscriptions.push(
		vscode.window.registerWebviewViewProvider(
			'motionbuilder.pyfbsdk-api.details',
			detailsProvider
		));

	vscode.commands.registerCommand("motionbuilder.pyfbsdk-api.view-details", function (data : any)
    {
		console.log("motionbuilder.pyfbsdk-api.view-details", data);
        detailsProvider.showDetails(data, 2025);
    });
}


export async function deactivate() {
	// Remove all temp files created by this extension
	await utils.cleanupTempFiles();
}