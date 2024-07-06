import * as vscode from 'vscode';

import * as notebook from './modules/notebook';
import * as logging from './modules/logging';
import * as utils from './modules/utils';

import * as codeCompletion from './scripts/code-completion';
import * as documentation from './scripts/documentation';
import * as reloadModules from './scripts/reload-modules';
import * as execute from './scripts/execute-script';
import * as attach from './scripts/attach';



import * as fs   from 'fs';


export function activate(context: vscode.ExtensionContext) {
	utils.setExtensionDir(context.extensionPath);

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

	deleteOldExtensionData();
}


export function deactivate() {
	// Remove all temp files created by this extension
	utils.cleanupTempFiles();
}


// TODO: Remove this cleanup function in a future release
/**
 * Delete the old appdata folder. Used in versions before 2025.0.0
 */
function deleteOldExtensionData() {
	const appdataFolder = utils.getExtensionAppdataFolder();
	if (fs.existsSync(appdataFolder)) {
		logging.log("Deleting old extension data folder: " + appdataFolder);
		fs.rmSync(appdataFolder, { recursive: true });
	}
}