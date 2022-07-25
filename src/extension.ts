import * as vscode from 'vscode';

import * as documentation from './scripts/documentation';
import * as mobuDebugger  from './scripts/debugger';
import * as stubFiles 	  from './scripts/stub-files';
import * as execute 	  from './scripts/execute-script';
import * as utils 		  from './modules/utils';


export function activate(context: vscode.ExtensionContext) {

    // Make sure stub files are setup
	stubFiles.setup();
	
	// -------------------------------
	// 		  	  Commands
	// -------------------------------

	// Run Scripts
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.execute', () => {
			execute.execute();
		})
	);

	// Debugging
	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.attach', () => {
			mobuDebugger.attachToMotionBuilder();
		})
	);

	// Documentation
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

	
	// -------------------------------
	// 		  	  Events
	// -------------------------------

	context.subscriptions.push(
		vscode.workspace.onDidChangeConfiguration(onConfigurationChanged)
	);
}


/**
 * Called when some configuration has been changed.
 * @param event The vscode configuration event
 */
async function onConfigurationChanged(event: vscode.ConfigurationChangeEvent) {
	// Early out if no motionbuilder configuration has been updated
	if (!event.affectsConfiguration("motionbuilder")) {
		return;
	}

	let bReloadRequired = false;
	
	// If the MotionBuilder version was changed, update the stub-files
	if (event.affectsConfiguration("motionbuilder.version")) {
		await stubFiles.setup(true);
		bReloadRequired = true;
	}

	// If needed, ask user to reload VS Code
	if (bReloadRequired) {
		let selection = await vscode.window.showInformationMessage("Reload required for changes to take full effect", "Reload", "Close");
		if (selection == "Reload") {
			vscode.commands.executeCommand("workbench.action.reloadWindow");
		}
	}

}


export function deactivate() { 
	// Remove all temp files created by this extension
	utils.cleanupTempFiles();
}