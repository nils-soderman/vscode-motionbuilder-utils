import * as vscode from 'vscode';

import * as notebook from './modules/notebook';
import * as utils from './modules/utils';

import * as codeCompletion from './scripts/code-completion';
import * as documentation from './scripts/documentation';
import * as reloadModules from './scripts/reload-modules';
import * as execute from './scripts/execute-script';
import * as attach from './scripts/attach';


export function activate(context: vscode.ExtensionContext) {
	utils.setExtensionUri(context.extensionUri);

	// Run Scripts
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.execute', () => {
			execute.executeCurrentDocument();
		})
	);
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.reloadModules', () => {
			reloadModules.main();
		})
	);

	// Debugging
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.attach', () => {
			attach.main(context);
		})
	);

	// Setup Code Completion
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.setupCodeCompletion', () => {
			codeCompletion.main(context);
		})
	);

	// Documentation
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentationPython', () => {
			documentation.browsePython();
		})
	);
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentationExamples', () => {
			documentation.browseExamples();
		})
	);

	notebook.setupNotebook(context);
}


export async function deactivate() {
	// Remove all temp files created by this extension
	await utils.cleanupTempFiles();
}