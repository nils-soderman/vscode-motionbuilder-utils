import * as vscode from 'vscode';

import * as htmlParser    from 'node-html-parser';
import * as path          from 'path';
import * as open          from 'open';

import * as utils from '../modules/utils';


const AUTODESK_HELP_DOMAIN = "https://help.autodesk.com/";
const MOBU_FILE_HOSTING_URL = AUTODESK_HELP_DOMAIN + "cloudhelp/";


/** Documentation table of content types */
const FDOCTYPE = {
    c: "c",
    example: "examples",
    guide: "guide",
    python: "python"
};


/**
 * Get the full URL to the location of the documentation page, from a url relative to the ENU folder.
 * @param version MotionBuilder version
 * @param relativePageURL The page URL relative to the ENU folder, as stored in the json toc.
 */
function getDocumentationPageURL(version: number, relativePageURL: string) {
    return MOBU_FILE_HOSTING_URL + version + "/ENU/" + relativePageURL;
}


/**
 * Parse one of the generated json table of content files.
 * @param type The type of documentation file to parse, should be one of the options in the struct: `FDOCTYPE`
 * @param version MotionBuilder version 
 * @returns a dictionary object that looks like: {"My Page": {"url": "myPage.html"}}
 */
function parseGeneratedDocumentationFile(type: string, version: number) {
    const filepath = path.join(utils.EXTENSION_RESOURCES_DIR, "documentation", version.toString(), `${type}.json`);
    return utils.readJson(filepath);
}


/**
 * Open a MoBu documentation page in the default web-browser app
 * @param relativePageURL The page URL relative to the ENU folder, as stored in the json toc.
 * @param version MotionBuilder version
 */
function openPageInBrowser(relativePageURL: string, version: number) {
    const url = getDocumentationPageURL(version, relativePageURL);
    open(url);
}


/**
 * Open the code from a MotionBuilder example inside the editor
 * @param url The full URL to the example documentation web-page
 * @param filename The abs filepath where to save the file on disk
 */
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
        
        const filepath = utils.saveTempFile(filename, content);
        const openPath = vscode.Uri.file(filepath);
        vscode.workspace.openTextDocument(openPath).then(doc => {
            vscode.window.showTextDocument(doc);
        });
    }

    utils.getRequest(url, handleResponse);
}


/**
 * List all pages from one or multiple documentation types, and open up the page selected by the user
 * @param types List of types to include, types should be of `FDOCTYPE`
 */
async function browseDocumentation(types: string[]) {
    let version: number = utils.getMotionBuilderVersion();

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