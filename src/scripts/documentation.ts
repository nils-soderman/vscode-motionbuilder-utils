import * as vscode from 'vscode';

import * as htmlParser from 'node-html-parser';

import * as logging from '../modules/logging';
import * as utils from '../modules/utils';


const AUTODESK_DOCS_URL = "https://help.autodesk.com/cloudhelp/";
const PYTHON_REF = "ENU/MOBU-PYTHON-API-REF/";
const MOTIONBUILDER_VERSION = 2026;

interface IDocumentationQuickPickItem extends vscode.QuickPickItem {
    url: string;
}

/**
 * Construct a valid filename from the selection label
 * @param label The label from which to construct the filename
 */
function constructPythonFilename(label: string): string {
    let filename = label.replace(/[/\\]/g, "_");

    if (!filename.endsWith(".py")) {
        filename += ".py";
    }

    if (filename.includes(":")) {
        filename = filename.split(":")[1].trimStart();
    }

    return filename;
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
    return vscode.Uri.joinPath(utils.getResourcesDir(), "documentation");
}

/**
 * Parse one of the generated json table of content files.
 * @param type The type of documentation file to parse, should be one of the options in the struct: `FDOCTYPE`
 * @returns a dictionary object that looks like: {"My Page": {"url": "myPage.html"}}
 */
async function parseGeneratedDocumentationFile(type: string): Promise<{ items: IDocumentationQuickPickItem[]; }> {
    const filepath = vscode.Uri.joinPath(getDocumentationDirectory(), `${type}.json`);
    return await utils.readJson(filepath);
}


/**
 * Open a MoBu documentation page in the default web-browser app
 * @param relativePageURL The page URL relative to the ENU folder, as stored in the json toc.
 * @param version MotionBuilder version
 */
function openPageInBrowser(relativePageURL: string, version: number) {
    const url = getDocumentationPageURL(version, relativePageURL);
    return vscode.env.openExternal(vscode.Uri.parse(url));
}


/**
 * Open the code from a MotionBuilder example inside the editor
 * @param url The full URL to the example documentation web-page
 * @param filename The abs filepath where to save the file on disk
 */
async function openExampleInVSCode(url: string, filename: string) {
    let data: string;
    try {
        data = await utils.getRequest(url, { timeout: 10_000 });
    }
    catch (error) {
        logging.showErrorMessage(`Failed to get: ${url}`, error as Error);
        return;
    }

    const parsedHtml = htmlParser.parse(data);

    const lines = parsedHtml.querySelectorAll(".line");

    const content = lines.map(line => {
        line.querySelectorAll(".lineno").forEach(e => e.remove());
        return line.text;
    }).join("\n");

    const filepath = await utils.saveTempFile(filename, content);
    const doc = await vscode.workspace.openTextDocument(filepath);

    return await vscode.window.showTextDocument(doc);
}


/**
 * List all pages from one or multiple documentation types, and open up the page selected by the user
 * @param type List of types to include, types should be of `FDOCTYPE`
 */
async function browseDocumentation(type: string, bExample = false) {
    const placeHolder = bExample ? `Search the MotionBuilder examples` : `Search the MotionBuilder ${type} documentation`;

    const data = await parseGeneratedDocumentationFile(type);
    const selection = await vscode.window.showQuickPick(data.items, {
        placeHolder
    });
    if (!selection) {
        return;
    }

    const relativePageUrl = selection.url;

    if (bExample && utils.getExtensionConfig().get<boolean>("documentation.openExamplesInEditor")) {
        // Open in VSCode
        const url = getDocumentationPageURL(MOTIONBUILDER_VERSION, relativePageUrl);
        const filename = constructPythonFilename(selection.label);

        await openExampleInVSCode(url, "Example_" + filename);
    }
    else {
        await openPageInBrowser(relativePageUrl, MOTIONBUILDER_VERSION);
    }
}


export async function browseExamples() {
    return browseDocumentation(FDOCTYPE.example, true);
}


export async function browsePython() {
    return browseDocumentation(FDOCTYPE.python);
}
