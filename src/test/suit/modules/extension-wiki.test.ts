import sinon from 'sinon';

import * as vscodeMock from '../vscode-mock';

import * as wiki from '../../../modules/extension-wiki';


suite('Extension Wiki', () => {
    let stubOpenExternal: sinon.SinonStub;

    setup(() => {
        stubOpenExternal = vscodeMock.mockOpenExternal();
    });

    teardown(() => {
        stubOpenExternal.restore();
    });

    test('Wiki Urls', async function () {
        for (const page of Object.values(wiki.Pages))
            await wiki.openPageInBrowser(page);
    });
});