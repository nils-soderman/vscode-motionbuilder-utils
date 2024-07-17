import * as assert from 'assert';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testInitialize from '../extension-initialize';
import * as vscodeMock from '../vscode-mock';

import * as exec from '../../../scripts/execute-script';
import * as utils from '../../../modules/utils';

const config = {
    showOutput: "execute.showOutput",
    clearOutput: "execute.clearOutput",
    name: "execute.name"
};

function checkOutput(outputChannel: vscodeMock.MockOutputChannel, expected: string) {
    assert.equal(outputChannel.output.length, 1);
    assert.equal(outputChannel.output[0], expected + "\n>>>\n");
}

suite('Execute', function () {
    this.timeout(20000);

    let getConfigurationStub: sinon.SinonStub;
    let stubGetOutputChannel: sinon.SinonStub;

    let editor: vscode.TextEditor;

    let mobuOutputChannel: vscodeMock.MockOutputChannel;

    const execName = "vscode-test";
    const extensionConfig = new vscodeMock.ConfigMock({
        [config.name]: execName,
        [config.showOutput]: true,
        [config.clearOutput]: true,
    });

    setup(async () => {
        testInitialize.initializeExtension();

        const filepath = testInitialize.getPythonTestFilepath("hello_world.py");
        const document = await vscode.workspace.openTextDocument(filepath);
        editor = await vscode.window.showTextDocument(document);


        getConfigurationStub = vscodeMock.stubGetConfiguration({
            "motionbuilder": extensionConfig
        });

        mobuOutputChannel = new vscodeMock.MockOutputChannel();
        stubGetOutputChannel = sinon.stub(utils, "getOutputChannel").returns(mobuOutputChannel);
    });

    teardown(async () => {
        getConfigurationStub.restore();
        stubGetOutputChannel.restore();

        await vscode.commands.executeCommand('workbench.action.closeActiveEditor');

        extensionConfig.reset();
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
        const utf8String = "你好世界-öäå";

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