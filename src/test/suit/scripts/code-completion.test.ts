import * as vscode from 'vscode';

import * as assert from 'assert';
import * as path from 'path';
import * as fs from 'fs';

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


async function testAddPythonAnalysisPath(path: string) {
    assert.strictEqual(await codeCompletion.addPythonAnalysisPath(path), "add");
    assert.strictEqual(await codeCompletion.addPythonAnalysisPath(path), "exists");
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

        await vscode.workspace.fs.delete(
            vscode.Uri.file(extensionContext.globalStorageUri.fsPath),
            { recursive: true }
        );
    });

    test('Setup Code Completion', async function () {
        this.timeout(20000); // This test downloads a file

        await codeCompletion.main(extensionContext);

        const stubFolder = path.join(extensionContext.globalStorageUri.fsPath, 'stubs');
        assert.ok(fs.existsSync(stubFolder));

        // Make sure all files have been created
        for (const file of EXPECTED_FILES) {
            const filePathPy = path.join(stubFolder, file + '.py');
            const filePathPyi = path.join(stubFolder, file + '.pyi');
            assert.ok(fs.existsSync(filePathPy));
            assert.ok(fs.existsSync(filePathPyi));
        }

        // Make sure the path has been added to the python configuration
        const paths = pythonConfig.get(PYTHON_CONFIG_KEY);
        assert.strictEqual(paths.length, 1);
        assert.strictEqual(paths[0], stubFolder);
    });
    
    test('addPythonAnalysisPath - global', async function () {
        pythonConfig.reset();

        testAddPythonAnalysisPath(extensionContext.globalStorageUri.fsPath);

        assert.strictEqual(pythonConfig.globalValue[PYTHON_CONFIG_KEY].length, 1);
    });

    test('addPythonAnalysisPath - workspace', async function () {
        pythonConfig.workspaceValue[PYTHON_CONFIG_KEY] = ['helloWorld'];

        testAddPythonAnalysisPath(extensionContext.globalStorageUri.fsPath);

        assert.strictEqual(pythonConfig.workspaceValue[PYTHON_CONFIG_KEY].length, 2);
    });

    test('addPythonAnalysisPath - workspaceFolder', async function () {
        pythonConfig.workspaceFolderValue[PYTHON_CONFIG_KEY] = ['helloWorld'];

        testAddPythonAnalysisPath(extensionContext.globalStorageUri.fsPath);

        assert.strictEqual(pythonConfig.workspaceFolderValue[PYTHON_CONFIG_KEY].length, 2);
    });
});