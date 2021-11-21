import * as vscode from 'vscode';
import * as https from 'https';
import * as path from 'path';
import * as os from "os";
import * as fs from 'fs';

import * as child_process from "child_process";

const MOBU_DOCS_URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/";

function parseJsonFile(type: string) {
    const filepath = path.join(__dirname, "..", "documentation", `${type}.json`);
    const fileContent = fs.readFileSync(filepath);
    return JSON.parse(fileContent.toString());
}

// TODO: this function is now in 2 places
function saveTempFile(filename: string, text: string,) {
    const filepath = path.join(os.tmpdir(), filename);
    fs.writeFileSync(filepath, text);
    return filepath;
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

            const filepath = saveTempFile(filename, content);

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
        let itemsToAppend = parseJsonFile(type);
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

    if (relativeURL.startsWith("SDKSamples")) {
        // Open in VSCode
        openExampleInVSCode(MOBU_DOCS_URL + relativeURL);
    }
    else {
        const url = `${MOBU_DOCS_URL}?url=${relativeURL},topicNumber=${items[selection]["id"]}`;
        child_process.exec(`start ${url}`);
    }
}

export async function browseExamples() {
    browseDocumentation(["examples"]);
}

export async function browsePython() {
    browseDocumentation(["python"]);
}

export async function browseC() {
    browseDocumentation(["c"]);
}

export async function browseGuide() {
    browseDocumentation(["guide"]);
}

export async function browseFullDocumentation() {
    browseDocumentation(["guide", "c", "python", "examples"]);
}


// TODO: Custom, allow user to select what types to browse in user settings
export async function browseCustomDocumentation() {
    const types: string[] = [];
    browseDocumentation(types);
}