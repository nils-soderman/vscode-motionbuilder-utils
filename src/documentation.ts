import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';

import * as child_process from "child_process";

const MOBU_DOCS_URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/";

function readJsonFile(filepath: string) {
    const fileContent = fs.readFileSync(filepath);
    return JSON.parse(fileContent.toString());
}



export async function openPage() {
    // TODO: Split into commands for browsing: All, Python, C++, Examples
    const filepath = path.join(__dirname, "..", "documentation", "content.json");
    const contentDict = readJsonFile(filepath);
    const items = Object.keys(contentDict);
    const selection = await vscode.window.showQuickPick(items);
    if (!selection)
        return;

    const url = MOBU_DOCS_URL + contentDict[selection];


    // "https://download.autodesk.com/us/motionbuilder/sdk-documentation/index.html?url=./files/WS73099cc142f48755-57af30d311c79e97fc3e12.htm,topicNumber=d0e319"

    // TODO: If it's a help page. Download content and create a local file (that can be executed)
    child_process.exec(`start ${url}`);


}

