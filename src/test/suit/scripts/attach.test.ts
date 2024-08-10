import * as assert from 'assert';

import * as vscode from 'vscode';

import sinon from 'sinon';

import * as testUtils from '../test-utils';
import * as vscodeMock from '../vscode-mock';

import * as utils from '../../../modules/utils';
import * as attach from '../../../scripts/attach';

const CONFIG_KEYS = {
    port: "attach.port",
    autoPort: "attach.autoPort"
};


suite('Attach', function () {
    this.timeout(5 * 1000);

    const extensionConfig = new vscodeMock.ConfigMock({
        [CONFIG_KEYS.port]: 4243,
        [CONFIG_KEYS.autoPort]: true
    });

    let extensionContext: vscode.ExtensionContext;
    let tempDebugpyInstallDir: vscode.Uri;

    suiteTeardown(async () => {
        if (await testUtils.uriExists(tempDebugpyInstallDir))
            await vscode.workspace.fs.delete(tempDebugpyInstallDir, { recursive: true });
    });
    
    setup(() => {
        testUtils.initializeExtension();

        extensionContext = vscodeMock.getExtensionContext();
        tempDebugpyInstallDir = vscode.Uri.joinPath(extensionContext.globalStorageUri, "site-packages");

        vscodeMock.stubGetConfiguration({
            "motionbuilder": extensionConfig
        });
    });

    teardown(async () => {
        sinon.restore();
        extensionConfig.reset();

        await vscode.debug.stopDebugging();
    });

    test('Install Debugpy', async function () {
        this.timeout(30 * 1000);

        assert.ok(await attach.installDebugpy(tempDebugpyInstallDir));
        assert.ok(await attach.isDebugpyInstalled(tempDebugpyInstallDir));
        
        // We expect to see a single folder with the Python version here, e.g. "Python311"
        const folderContent = await vscode.workspace.fs.readDirectory(tempDebugpyInstallDir);
        assert.equal(folderContent.length, 1);

        const [name, type] = folderContent[0];
        assert.ok(name.startsWith("Python"));
        assert.strictEqual(type, vscode.FileType.Directory);

        // Check that the debugpy module is present
        const debugpyPath = vscode.Uri.joinPath(tempDebugpyInstallDir, name, "debugpy");
        assert.ok(await vscode.workspace.fs.stat(debugpyPath));

    });

    test('Get Wanted Port', async function () {
        // Calling tcp-port-used on the debugpy port breaks the debugpy server
        // TODO: Look into a fix for this
        sinon.stub(utils, "isPortAvailable").callsFake(async (port: number) => {
            return port !== 4242;
        });

        assert.ok(await attach.getWantedPort());

        extensionConfig.update(CONFIG_KEYS.port, undefined);
        assert.ok(await attach.getWantedPort() === null);

        // port 4242 is busy because MotionBuilder's python server is running on it
        extensionConfig.update(CONFIG_KEYS.port, 4242);
        const wantedPort = await attach.getWantedPort();
        assert.ok(wantedPort && wantedPort > 4242);
        
        extensionConfig.update(CONFIG_KEYS.autoPort, false);
        assert.ok(await attach.getWantedPort() === null);
    });

    test('Start Debugpy & Attach', async function () {
        this.timeout(20 * 1000);

        assert.ok(await attach.main(extensionContext));
        
        assert.ok(utils.isDebuggingMotionBuilder());
        
        // Re-attach should not start a new session
        assert.ok(await attach.main(extensionContext));
    });
    
    test('Re-attach', async function() {
        assert.ok(await attach.getCurrentDebugPort());
        
        assert.ok(!utils.isDebuggingMotionBuilder());
        assert.ok(await attach.main(extensionContext));

        assert.ok(utils.isDebuggingMotionBuilder());
    });
    
});
