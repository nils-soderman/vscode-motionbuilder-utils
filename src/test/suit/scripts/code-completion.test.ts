import * as vscode from 'vscode';

import * as assert from 'assert';

import sinon from 'sinon';

import * as testUtils from '../test-utils';
import * as vscodeMock from '../vscode-mock';

import * as codeCompletion from '../../../scripts/code-completion';


const EXPECTED_FILES = [
    "pyfbsdk",
    "pyfbsdk_additions",
    "callbackframework",
    "pythonidelib"
];

const PYTHON_CONFIG_KEY = 'analysis.extraPaths';


async function testAddPythonAnalysisPath(path: vscode.Uri) {
    assert.strictEqual(await codeCompletion.addPythonAnalysisPath(path.fsPath), "add");
    assert.strictEqual(await codeCompletion.addPythonAnalysisPath(path.fsPath), "exists");
};


suite('Setup Code Completion', () => {
    const extensionContext = vscodeMock.getExtensionContext();

    const pythonConfig = new vscodeMock.ConfigMock({
        [PYTHON_CONFIG_KEY]: []
    });

    setup(() => {
        testUtils.initializeExtension();

        vscodeMock.stubShowQuickPick();

        vscodeMock.stubGetConfiguration({
            "python": pythonConfig
        });
    });

    teardown(async () => {
        sinon.restore();
        pythonConfig.reset();

        if (await testUtils.uriExists(extensionContext.globalStorageUri))
            await vscode.workspace.fs.delete(extensionContext.globalStorageUri, { recursive: true });
    });

    test('Setup Code Completion', async function () {
        this.timeout(20000); // This test downloads a file

        await codeCompletion.main(extensionContext);

        const stubFolder = vscode.Uri.joinPath(extensionContext.globalStorageUri, 'stubs');
        assert.ok(testUtils.uriExists(stubFolder));

        // Make sure all files have been created
        for (const file of EXPECTED_FILES) {
            const filePathPy = vscode.Uri.joinPath(stubFolder, file + '.py');
            const filePathPyi = vscode.Uri.joinPath(stubFolder, file + '.pyi');
            assert.ok(testUtils.uriExists(filePathPy));
            assert.ok(testUtils.uriExists(filePathPyi));
        }

        // Make sure the path has been added to the python configuration
        const paths = pythonConfig.get(PYTHON_CONFIG_KEY);
        assert.strictEqual(paths.length, 1);
        assert.strictEqual(paths[0], stubFolder.fsPath);
    });
    
    test('addPythonAnalysisPath - global', async function () {
        await testAddPythonAnalysisPath(extensionContext.globalStorageUri);

        assert.strictEqual(pythonConfig.globalValue[PYTHON_CONFIG_KEY].length, 1);
    });

    test('addPythonAnalysisPath - workspace', async function () {
        pythonConfig.workspaceValue[PYTHON_CONFIG_KEY] = ['helloWorld'];

        await testAddPythonAnalysisPath(extensionContext.globalStorageUri);

        assert.strictEqual(pythonConfig.workspaceValue[PYTHON_CONFIG_KEY].length, 2);
    });

    test('addPythonAnalysisPath - workspaceFolder', async function () {
        pythonConfig.workspaceFolderValue[PYTHON_CONFIG_KEY] = ['helloWorld'];

        await testAddPythonAnalysisPath(extensionContext.globalStorageUri);

        assert.strictEqual(pythonConfig.workspaceFolderValue[PYTHON_CONFIG_KEY].length, 2);
    });
});