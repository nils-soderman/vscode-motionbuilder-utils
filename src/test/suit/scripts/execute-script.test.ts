import * as assert from 'assert';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testUtils from '../test-utils';
import * as vscodeMock from '../vscode-mock';

import * as exec from '../../../scripts/execute-script';
import * as mobuConsole from '../../../modules/motionbuilder-console';
import * as utils from '../../../modules/utils';

const config = {
    showOutput: "execute.showOutput",
    clearOutput: "execute.clearOutput",
    name: "execute.name",
    addWorkspaceToPath: "environment.addWorkspaceToPath"
};

function checkOutput(outputChannel: vscodeMock.MockOutputChannel, expected: string) {
    assert.equal(outputChannel.output.length, 1);
    assert.equal(outputChannel.output[0], expected + "\n>>>\n");
}

suite('Execute', function () {
    this.timeout(20000);

    let editor: vscode.TextEditor;
    let mobuOutputChannel: vscodeMock.MockOutputChannel;

    const execName = "vscode-test";
    const extensionConfig = new vscodeMock.ConfigMock({
        [config.name]: execName,
        [config.showOutput]: true,
        [config.clearOutput]: true,
        [config.addWorkspaceToPath]: true
    });

    setup(async () => {
        testUtils.initializeExtension();

        const filepath = testUtils.getPythonTestFilepath("hello_world.py");
        const document = await vscode.workspace.openTextDocument(filepath);
        editor = await vscode.window.showTextDocument(document);

        vscodeMock.stubGetConfiguration({
            "motionbuilder": extensionConfig
        });

        mobuOutputChannel = new vscodeMock.MockOutputChannel();
        sinon.stub(utils, "getOutputChannel").returns(mobuOutputChannel);
    });

    teardown(async () => {
        sinon.restore();
        extensionConfig.reset();

        await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
    });

    test("Sys Path", async function () {
        const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
        assert.ok(workspaceFolder);
        
        // Restart connection with 'addWorkspaceToPath' set to true
        mobuConsole.closeSocket();

        const result = await mobuConsole.runCommand("import sys;print(';'.join(sys.path))");
        assert.ok(result);

        const paths = result.split(";");
        assert.ok(paths.includes(workspaceFolder.uri.fsPath), `${workspaceFolder.uri.fsPath} not in:\n${paths.join("\n")}`);    
    });

    test('Execute File', async function () {
        await exec.executeCurrentDocument();

        checkOutput(mobuOutputChannel, execName);
    });

    test('Clear Output', async function () {
        extensionConfig.update(config.clearOutput, false);
        for (let i = 1; i <= 3; i++) {
            await exec.executeCurrentDocument();
            assert.equal(mobuOutputChannel.output.length, i);
        }

        extensionConfig.update(config.clearOutput, true);
        for (let i = 1; i <= 3; i++) {
            await exec.executeCurrentDocument();
            assert.equal(mobuOutputChannel.output.length, 1);
        }
    });

    test('Show Output', async function () {
        mobuOutputChannel.bVisible = false;

        extensionConfig.update(config.showOutput, false);
        await exec.executeCurrentDocument();
        assert.ok(!mobuOutputChannel.bVisible);

        extensionConfig.update(config.showOutput, true);
        await exec.executeCurrentDocument();
        assert.ok(mobuOutputChannel.bVisible);
    });

    test('Execute Selection', async function () {
        await editor.edit(editBuilder => {
            editBuilder.insert(new vscode.Position(0, 0), "    print('1')\n  print('2')\n");
        });

        editor.selection = new vscode.Selection(new vscode.Position(0, 0), new vscode.Position(2, 0));

        await exec.executeCurrentDocument();

        checkOutput(mobuOutputChannel, "1\n2");
    });

    test('UTF-8 Characters', async function () {
        const utf8String = "你好世界-öäå";
        await editor.edit(editBuilder => {
            const fullRange = new vscode.Range(
                editor.document.positionAt(0),
                editor.document.positionAt(editor.document.getText().length)
            );
            editBuilder.replace(fullRange, `print('${utf8String}')`);
        });

        await exec.executeCurrentDocument();

        checkOutput(mobuOutputChannel, utf8String);
    });

    test('Large Unsaved Output', async function () {
        const utf8String = "abc-你好世界-öäå";

        await editor.edit(editBuilder => {
            const fullRange = new vscode.Range(
                editor.document.positionAt(0),
                editor.document.positionAt(editor.document.getText().length)
            );
            editBuilder.replace(fullRange, `for i in range(1000):\n    print('${utf8String}')`);
        });

        await exec.executeCurrentDocument();

        const expectedOutput = `${utf8String}\n`.repeat(1000).trimEnd();
        checkOutput(mobuOutputChannel, expectedOutput);
    });

    test('No Editor', async function () {
        await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
        await exec.executeCurrentDocument();

        assert.equal(mobuOutputChannel.output.length, 0);
    });
});