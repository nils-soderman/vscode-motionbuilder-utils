import * as vscode from "vscode";


export const WIKI_URL = "https://github.com/nils-soderman/vscode-motionbuilder-utils/wiki/";

export class Pages {
    static readonly failedToConnect = "Failed-to-connect-to-MotionBuilder-%5BTroubleshooting%5D";
}

function getPageUri(page: string): vscode.Uri {
    return vscode.Uri.parse(WIKI_URL + page);
}

export async function openPageInBrowser(page: string) {
    const uri = getPageUri(page);
    return await vscode.env.openExternal(uri);
}