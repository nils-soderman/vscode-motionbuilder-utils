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

    setup(() => {
        testUtils.initializeExtension();

        vscodeMock.mockOpenExternal();
        vscodeMock.stubShowQuickPick();

        vscodeMock.stubGetConfiguration({
            "motionbuilder": extensionConfig
        });
    });

    teardown(async () => {
        sinon.restore();

        await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
    });

    test('Open Example In Editor', async function () {
        await docs.browseExamples();

        // Check the currently open text editor
        const editor = vscode.window.activeTextEditor;
        assert.ok(editor);
        assert.ok(editor.document.languageId === 'python');
        assert.ok(editor.document.lineCount > 0);
    });

    test("Open in Webbrowser", async function () {
        await docs.browsePython();

        extensionConfig.update(OPEN_IN_EDITOR_CONFIG, false);
        await docs.browseExamples();
    });
});