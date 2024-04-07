import * as vscode from 'vscode';

import * as codeCompletion from './scripts/code-completion';
import * as documentation from './scripts/documentation';
import * as reloadModules from './scripts/reloadModules';
import * as attach from './scripts/attach';
import * as execute from './scripts/execute-script';
import * as utils from './modules/utils';


export function activate(context: vscode.ExtensionContext) {
	utils.setExtensionDir(context.extensionPath);

	// Run Scripts
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.execute', () => {
			execute.execute();
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
			attach.attachToMotionBuilder();
		})
	);

	// Setup Code Completion
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.setupCodeCompletion', () => {
			codeCompletion.main();
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
}


export function deactivate() {
	// Remove all temp files created by this extension
	utils.cleanupTempFiles();
}