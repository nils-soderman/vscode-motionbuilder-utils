import * as vscode from 'vscode';

import * as child_process from "child_process";
import * as htmlParser    from 'node-html-parser';
import * as path          from 'path';

import * as utils from '../modules/utils';


const AUTODESK_HELP_DOMAIN = "https://help.autodesk.com/";
const MOBU_FILE_HOSTING_URL = AUTODESK_HELP_DOMAIN + "cloudhelp/";


const FDOCTYPE = {
    c: "c",
    example: "examples",
    guide: "guide",
    python: "python"
};


function getDocumentationPageURL(version: number, relativePageURL: string) {
    return MOBU_FILE_HOSTING_URL + version + "/ENU/" + relativePageURL;
}


function parseGeneratedDocumentationFile(type: string, version: number) {
    const filepath = path.join(utils.EXTENSION_RESOURCES_DIR, "documentation", version.toString(), `${type}.json`);
    return utils.readJson(filepath);
}


function openPageInBrowser(pageId: string, version: number) {
    const url = getDocumentationPageURL(version, pageId);
    child_process.exec(`start ${url}`);
}


function openExampleInVSCode(url: string, filename: string) {
    function handleResponse(data: string, statusCode?: number) {
        // TODO: check statusCode
        const parsedHtml = htmlParser.parse(data);
        let content = "";
        for (const line of parsedHtml.querySelectorAll(".line")) {
            let lineText = line.text.split(/[0-9]\s(.+)/)[1];
            if (lineText) {
                content += line.text.split(/[0-9]\s(.+)/)[1] + "\n";
            }
            else {
                content += "\n";
            }
        }

        // Save file
        const filepath = utils.saveTempFile(filename, content);

        const openPath = vscode.Uri.file(filepath);
        vscode.workspace.openTextDocument(openPath).then(doc => {
            vscode.window.showTextDocument(doc);
        });
    }

    utils.getRequest(url, handleResponse);
}


async function browseDocumentation(types: string[]) {
    let version: number = utils.getVersion();

    let items: any = {};
    let browsingType: string = "";
    for (const type of types) {
        let itemsToAppend = parseGeneratedDocumentationFile(type, version);
        if (types.length > 1) {
            const prefix = `${type[0].toUpperCase() + type.slice(1)}`;
            for (const [key, value] of Object.entries(itemsToAppend)) {
                // @ts-ignore
                items[`[${prefix}] ${key}`] = { url: value["url"], type: type };
            }
        }
        else {
            items = Object.assign(items, itemsToAppend);
            browsingType = type;
        }
    }

    const selectableItems = Object.keys(items);
    const selection = await vscode.window.showQuickPick(selectableItems);
    if (!selection) {
        return;
    }

    const relativePageUrl = items[selection]["url"];
    if (!browsingType) {
        browsingType = items[selection]["type"];
    }

    if (browsingType == FDOCTYPE.example && utils.getExtensionConfig().get("documentation.openExamplesInEditor")) {
        // Open in VSCode
        const url = getDocumentationPageURL(version, relativePageUrl);

        // Construct a filename
        let filename = selection.replace(/\//g, "_");
        if (!filename.endsWith(".py")) {
            filename += ".py";
        }
        if (filename.includes(":")) {
            filename = filename.split(":")[1].trimStart();
        }

        openExampleInVSCode(url, "Example_" + filename);
    }
    else {
        openPageInBrowser(relativePageUrl, version);
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