import * as vscode from 'vscode';

import * as documentation from "./documentation";
import * as autocompletion from "./auto-completion";
import * as execute from "./execute_script";


export function activate(context: vscode.ExtensionContext) {

	// Make sure auto-completion is setup
	autocompletion.setupAutocompletion();

	
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


export function deactivate() { }
