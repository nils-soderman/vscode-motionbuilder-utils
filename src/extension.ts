import * as vscode from 'vscode';

import * as autocompletion from "./auto-completion";
import * as documentation from "./documentation";
import * as execute from "./execute-script";
import * as utils from './utils';


export function activate(context: vscode.ExtensionContext) {

	const mobuConfig = vscode.workspace.getConfiguration("motionbuilder");
    if (mobuConfig.get("motionbuilder.autocompletion.patchOnActivated")) {
		// Make sure auto-completion is setup
		autocompletion.setupAutocompletion();
	}

	
	// -------------------------------
	// 		  	  Commands
	// -------------------------------

	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.execute', () => {
			execute.execute();
		})
	);


	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentation', () => {
			documentation.browseFullDocumentation();
		})
	);
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentationPython', () => {
			documentation.browsePython();
		})
	);
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.browseDocumentationC', () => {
			documentation.browseC();
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
