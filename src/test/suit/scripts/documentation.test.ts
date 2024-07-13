import * as assert from 'assert';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testInitialize from '../extension-initialize';
import * as vscodeMock from '../vscode-mock';

import * as docs from '../../../scripts/documentation';

import * as https from "https";

const OPEN_IN_EDITOR_CONFIG = "documentation.openExamplesInEditor";


suite('Documentation', () => {
    let showQuickPickStub: sinon.SinonStub;
    let getConfigurationStub: sinon.SinonStub;
    let stubOpenExternal: sinon.SinonStub;

    const extensionConfig = new vscodeMock.ConfigMock({
        [OPEN_IN_EDITOR_CONFIG]: true
    });

    setup(() => {
        testInitialize.initializeExtension();

        stubOpenExternal = vscodeMock.mockOpenExternal();
        showQuickPickStub = vscodeMock.stubShowQuickPick();

        getConfigurationStub = vscodeMock.stubGetConfiguration({
            "motionbuilder": extensionConfig
        });
    });

    teardown(() => {
        showQuickPickStub.restore();
        getConfigurationStub.restore();
        stubOpenExternal.restore();
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