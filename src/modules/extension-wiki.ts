import * as vscode from "vscode";


export const WIKI_URL = "https://github.com/nils-soderman/vscode-motionbuilder-utils/wiki/";

export class Pages {
    static readonly failedToConnect = "Failed-to-connect-to-MotionBuilder-%5BTroubleshooting%5D";
}

export function getPageUrl(page: string) {
    return WIKI_URL + page;
}

export async function openPageInBrowser(page: string) {
    const url = getPageUrl(page);
    return await vscode.env.openExternal(vscode.Uri.parse(url));
}