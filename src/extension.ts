// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as execute from "./execute_script";
import * as child_process from "child_process";
import * as path from "path";

const MOBU_DOCS_URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/";

// TODO: Features:
// * Autocompletion setup when installed (add extra path)
// * TelNet -> RunInMotionBuilder


// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Auto-completion:
	let pythonConfig = vscode.workspace.getConfiguration("python");
	let extraPaths: Array<string> | undefined = pythonConfig.get("analysis.extraPaths");
	if (extraPaths)
	{
		let completionPath: string = path.join(path.dirname(__dirname), "auto_completion");
		if (!extraPaths.includes(completionPath)) {
			extraPaths.splice(0, 0, completionPath);
			pythonConfig.update("analysis.extraPaths", extraPaths, true);
		}
	}
	

	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.execute', () => {
			execute.execute();
		})
	);

	context.subscriptions.push(
		vscode.commands.registerCommand('motionbuilder.openDocumentation', () => {
			// for now, just open the docs in the browser
			child_process.exec(`start ${MOBU_DOCS_URL}`);
		})
	);

}



// this method is called when your extension is deactivated
export function deactivate() {}
