import * as vscode from 'vscode';

import * as htmlParser from 'node-html-parser';
import * as path from 'path';

import * as utils from '../modules/utils';
import * as logging from '../modules/logging';

import open = require('open');


const AUTODESK_DOCS_URL = "https://help.autodesk.com/cloudhelp/";
const PYTHON_REF = "ENU/MOBU-PYTHON-API-REF/";
const MOTIONBUILDER_VERSION = 2025;

interface IDocumentationQuickPickItem extends vscode.QuickPickItem {
    url: string;
}


/** Documentation table of content types */
const FDOCTYPE = {
    example: "examples",
    python: "python"
};


/**
 * Get the full URL to the location of the documentation page, from a url relative to the ENU folder.
 * @param version MotionBuilder version
 * @param relativePageURL The page URL relative to the ENU folder, as stored in the json toc.
 */
function getDocumentationPageURL(version: number, relativePageURL: string) {
    return `${AUTODESK_DOCS_URL}${version}/${PYTHON_REF}${relativePageURL}`;
}

/**
 * Get the directory where the documentation is stored.
 */
function getDocumentationDirectory() {
    return path.join(utils.getResourcesDir(), "documentation");
}

/**
 * Parse one of the generated json table of content files.
 * @param type The type of documentation file to parse, should be one of the options in the struct: `FDOCTYPE`
 * @returns a dictionary object that looks like: {"My Page": {"url": "myPage.html"}}
 */
function parseGeneratedDocumentationFile(type: string): {
    items: IDocumentationQuickPickItem[],
} {
    const filepath = path.join(getDocumentationDirectory(), `${type}.json`);
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
    utils.getRequest(url).then(
        (data) => {
            const parsedHtml = htmlParser.parse(data);

            let content = "";
            for (const line of parsedHtml.querySelectorAll(".line")) {
                // Remove line numbers
                line.querySelectorAll(".lineno").forEach(e => e.remove());

                content += line.text + "\n";
            }

            const filepath = utils.saveTempFile(filename, content);
            const openPath = vscode.Uri.file(filepath);
            vscode.workspace.openTextDocument(openPath).then(doc => {
                vscode.window.showTextDocument(doc);
            });
        },
        (err) => logging.showErrorMessage(`Failed to get: ${url}`, err)
    );
}


/**
 * List all pages from one or multiple documentation types, and open up the page selected by the user
 * @param type List of types to include, types should be of `FDOCTYPE`
 */
async function browseDocumentation(type: string, bExampels = false) {
    const placeHolder = bExampels ? `Search the MotionBuilder examples` : `Search the MotionBuilder ${type} documentation`;

    const data = parseGeneratedDocumentationFile(type);
    const selection = await vscode.window.showQuickPick(data.items, {
        placeHolder
    });
    if (!selection) {
        return;
    }

    const relativePageUrl = selection.url;

    if (bExampels && utils.getExtensionConfig().get<boolean>("documentation.openExamplesInEditor")) {
        // Open in VSCode
        const url = getDocumentationPageURL(MOTIONBUILDER_VERSION, relativePageUrl);

        // Construct a filename
        let filename = selection.label.replace(/[/\\]/g, "_");
        if (!filename.endsWith(".py")) {
            filename += ".py";
        }
        if (filename.includes(":")) {
            filename = filename.split(":")[1].trimStart();
        }

        openExampleInVSCode(url, "Example_" + filename);
    }
    else {
        openPageInBrowser(relativePageUrl, MOTIONBUILDER_VERSION);
    }
}


export async function browseExamples() {
    return browseDocumentation(FDOCTYPE.example, true);
}


export async function browsePython() {
    return browseDocumentation(FDOCTYPE.python);
}