import * as assert from 'assert';
import * as crypto from 'crypto';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testInitialize from '../extension-initialize';
import * as vscodeMock from '../vscode-mock';

import * as codeCompletion from '../../../scripts/code-completion';


const EXPECTED_FILES = [
    "pyfbsdk",
    "pyfbsdk_additions",
    "callbackframework",
    "pythonidelib"
];

const PYTHON_CONFIG_KEY = 'analysis.extraPaths';


suite('Setup Code Completion', () => {
    let showQuickPickStub: sinon.SinonStub;
    let getConfigurationStub: sinon.SinonStub;

    const globalStoragePath = path.join(os.tmpdir(), crypto.randomUUID());;

    const pythonConfig = new vscodeMock.ConfigMock({
        [PYTHON_CONFIG_KEY]: []
    });

    setup(() => {
        testInitialize.initializeExtension();

        showQuickPickStub = vscodeMock.stubShowQuickPick();

        getConfigurationStub = vscodeMock.stubGetConfiguration({
            "python": pythonConfig
        });
    });

    teardown(() => {
        showQuickPickStub.restore();
        getConfigurationStub.restore();

        fs.rmSync(globalStoragePath, { recursive: true, force: true });
    });

    test('Setup Code Completion', async function () {
        // The stub files will be setup in this folder
        const extensionContext = {
            globalStorageUri: vscode.Uri.parse(globalStoragePath),
        } as vscode.ExtensionContext;

        this.timeout(20000); // Because it downloads a file we need a generous timeout
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

        assert.strictEqual(await codeCompletion.addPythonAnalysisPath(globalStoragePath), "add");
        assert.strictEqual(await codeCompletion.addPythonAnalysisPath(globalStoragePath), "exists");

        assert.strictEqual(pythonConfig.globalValue[PYTHON_CONFIG_KEY].length, 1);
    });

    test('addPythonAnalysisPath - workspace', async function () {
        pythonConfig.workspaceValue[PYTHON_CONFIG_KEY] = ['helloWorld'];

        assert.strictEqual(await codeCompletion.addPythonAnalysisPath(globalStoragePath), "add");
        assert.strictEqual(await codeCompletion.addPythonAnalysisPath(globalStoragePath), "exists");
        assert.strictEqual(pythonConfig.workspaceValue[PYTHON_CONFIG_KEY].length, 2);
    });

    test('addPythonAnalysisPath - workspaceFolder', async function () {
        pythonConfig.workspaceFolderValue[PYTHON_CONFIG_KEY] = ['helloWorld'];

        assert.strictEqual(await codeCompletion.addPythonAnalysisPath(globalStoragePath), "add");
        assert.strictEqual(await codeCompletion.addPythonAnalysisPath(globalStoragePath), "exists");
        assert.strictEqual(pythonConfig.workspaceFolderValue[PYTHON_CONFIG_KEY].length, 2);
    });
});