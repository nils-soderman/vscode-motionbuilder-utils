import * as assert from 'assert';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testUtils from '../test-utils';
import * as vscodeMock from '../vscode-mock';

import * as docs from '../../../scripts/documentation';

const OPEN_IN_EDITOR_CONFIG = "documentation.openExamplesInEditor";


suite('Documentation', () => {
    const extensionConfig = new vscodeMock.ConfigMock({
        [OPEN_IN_EDITOR_CONFIG]: true
    });

    const extensionContext = vscodeMock.getExtensionContext();
    let openExternalStub: sinon.SinonStub;

    setup(() => {
        testUtils.initializeExtension();

        openExternalStub = vscodeMock.mockOpenExternal();
        vscodeMock.stubShowQuickPick();

        vscodeMock.stubGetConfiguration({
            "motionbuilder": extensionConfig
        });
    });

    teardown(async () => {
        sinon.restore();

        await vscode.workspace.fs.delete(extensionContext.globalStorageUri, { recursive: true });
        await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
    });

    test('Examples', async function () {
        await docs.browseExamples(extensionContext);

        // Check the currently open text editor
        const editor = vscode.window.activeTextEditor;
        assert.ok(editor);
        assert.ok(editor.document.languageId === 'python');
        assert.ok(editor.document.lineCount > 0);

        await vscode.commands.executeCommand('workbench.action.closeActiveEditor');

        // Open external browser
        extensionConfig.update(OPEN_IN_EDITOR_CONFIG, false);
        await docs.browseExamples(extensionContext);
        assert.ok(vscode.window.activeTextEditor === undefined, "Editor was not closed");
        assert.ok(openExternalStub.calledOnce, "Open external was not called once");
    });
    
    test("pyfbsdk documentation", async function () {
        await docs.browseDocumentation(extensionContext);
        assert.ok(openExternalStub.calledOnce, "Open external was not called once");
    });
});