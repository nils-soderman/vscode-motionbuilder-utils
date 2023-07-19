import open = require('open');

export const WIKI_URL = "https://github.com/nils-soderman/vscode-motionbuilder-utils/wiki/";

export class Pages {
    static readonly failedToConnect = "Failed-to-connect-to-MotionBuilder-%5BTroubleshooting%5D";
}

export function getPageUrl(page: string) {
    return WIKI_URL + page;
}

export function openPageInBrowser(page: string) {
    const url = getPageUrl(page);
    open(url);
}