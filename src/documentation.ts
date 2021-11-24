import * as vscode from 'vscode';
import * as https from 'https';
import * as path from 'path';
import * as fs from 'fs';

import * as child_process from "child_process";

import * as utils from './utils';


const MOBU_DOCS_URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/";

const FDOCTYPE = {
    c: "c",
    example: "examples",
    guide: "guide",
    python: "python"
};


function parseDocumentation(type: string) {
    const filepath = path.join(__dirname, "..", "documentation", `${type}.json`);
    return utils.readJson(filepath);
}


function openExampleInVSCode(url: string) {
    https.get(url, (res) => {
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });

        res.on('end', () => {
            // Get the script as plain text
            const content = data.split("<body>")[1].replace(/<[^>]*>/g, '').trim();

            // Save file
            let filename = path.basename(url);
            if (filename.includes(".")) {
                filename = filename.split(".")[0];
            }
            filename += ".py";

            const filepath = utils.saveTempFile(filename, content);

            const openPath = vscode.Uri.file(filepath);
            vscode.workspace.openTextDocument(openPath).then(doc => {
                vscode.window.showTextDocument(doc);
            });

        });
    });
}


async function browseDocumentation(types: string[]) {
    let items: any = {};
    for (const type of types) {
        let itemsToAppend = parseDocumentation(type);
        if (types.length > 1) {
            const prefix = `${type[0].toUpperCase() + type.slice(1)}: `;
            for (const [key, value] of Object.entries(itemsToAppend)) {
                items[prefix + key] = value;
            }
        }
        else {
            items = Object.assign(items, itemsToAppend);
        }
    }

    const selectableItems = Object.keys(items);
    const selection = await vscode.window.showQuickPick(selectableItems);
    if (!selection) {
        return;
    }

    const relativeURL: string = items[selection]["url"].replace(/\s/g, "%20");

    if (relativeURL.startsWith("SDKSamples") && utils.getExtensionConfig().get("documentation.openExamplesInEditor")) {
        // Open in VSCode
        openExampleInVSCode(MOBU_DOCS_URL + relativeURL);
    }
    else {
        const url = `${MOBU_DOCS_URL}?url=${relativeURL},topicNumber=${items[selection]["id"]}`;
        child_process.exec(`start ${url}`);
    }
}


export async function browseExamples() {
    return browseDocumentation([FDOCTYPE.example]);
}


export async function browsePython() {
    return browseDocumentation([FDOCTYPE.python]);
}


export async function browseC() {
    return browseDocumentation([FDOCTYPE.c]);
}


export async function browseGuide() {
    return browseDocumentation([FDOCTYPE.guide]);
}


export async function browseFullDocumentation() {
    return browseDocumentation([FDOCTYPE.guide, FDOCTYPE.c, FDOCTYPE.python, FDOCTYPE.example]);
}