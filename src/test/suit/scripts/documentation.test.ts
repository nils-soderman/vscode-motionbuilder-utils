import * as assert from 'assert';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testInitialize from '../extension-initialize';
import * as vscodeMock from '../vscode-mock';

import * as docs from '../../../scripts/documentation';


suite('Documentation', () => {
    let showQuickPickStub: sinon.SinonStub;
    let getConfigurationStub: sinon.SinonStub;

    setup(() => {
        testInitialize.initializeExtension();

        showQuickPickStub = vscodeMock.stubShowQuickPick();

        getConfigurationStub = vscodeMock.stubGetConfiguration({
            "motionbuilder": new vscodeMock.ConfigMock({
                "documentation.openExamplesInEditor": true
            })
        });
    });

    teardown(() => {
        showQuickPickStub.restore();
        getConfigurationStub.restore();
    });

    test('Open Example In Editor', async function () {
        await docs.browseExamples();

        // Check the currently open text editor
        const editor = vscode.window.activeTextEditor;
        assert.ok(editor);
        assert.ok(editor.document.languageId === 'python');
        assert.ok(editor.document.lineCount > 0);
    });
});