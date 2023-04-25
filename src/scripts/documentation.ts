import * as vscode from 'vscode';

import * as htmlParser from 'node-html-parser';
import * as path from 'path';
import * as fs from 'fs';
import * as open from 'open';

import * as utils from '../modules/utils';


const AUTODESK_DOCS_URL = "https://help.autodesk.com/cloudhelp/";
const PYTHON_REF = "ENU/MotionBuilder-SDK/py_ref/";


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
 * @param version MotionBuilder version, if not specified, the base directory containing all versions is returned.
 */
function getDocumentationDirectory(version?: number) {
    let directory = path.join(utils.EXTENSION_RESOURCES_DIR, "documentation");
    if (version) {
        directory = path.join(directory, version.toString());
    }
    return directory;
}

/**
 * Parse one of the generated json table of content files.
 * @param type The type of documentation file to parse, should be one of the options in the struct: `FDOCTYPE`
 * @param version MotionBuilder version 
 * @returns a dictionary object that looks like: {"My Page": {"url": "myPage.html"}}
 */
function parseGeneratedDocumentationFile(type: string, version: number) {
    const filepath = path.join(getDocumentationDirectory(version), `${type}.json`);
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
        if (!statusCode || statusCode >= 400) {
            vscode.window.showErrorMessage(`Failed to get: ${url}`);
            return;
        }

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
    }

    utils.getRequest(url, handleResponse);
}

function getAvailableDocumentationVersions() {
    const documentationDir = getDocumentationDirectory();
    return fs.readdirSync(documentationDir).map(v => parseInt(v));
}

function getClosestAvailableVersion(version: number, type: string) {
    const versions = getAvailableDocumentationVersions();
    if (versions.includes(version)) {
        if (fs.existsSync(path.join(getDocumentationDirectory(version), `${type}.json`))) {
            return version;
        }
    }

    // Find the closest version
    let closestVersion: number | undefined;
    for (const v of versions) {
        if (!fs.existsSync(path.join(getDocumentationDirectory(v), `${type}.json`))) {
            continue;
        }

        if (!closestVersion) {
            closestVersion = v;
            continue;
        }

        if (Math.abs(v - version) < Math.abs(closestVersion - version)) {
            closestVersion = v;
        }
    }

    return closestVersion;
}

/**
 * List all pages from one or multiple documentation types, and open up the page selected by the user
 * @param type List of types to include, types should be of `FDOCTYPE`
 */
async function browseDocumentation(type: string) {
    const version = getClosestAvailableVersion(utils.getMotionBuilderVersion(), type);
    if (!version) {
        return;
    }

    let items: any = {};
    let browsingType: string = "";

    let itemsToAppend = parseGeneratedDocumentationFile(type, version);
    items = Object.assign(items, itemsToAppend);
    browsingType = type;

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
        let filename = selection.replace(/[/\\]/g, "_");
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
    return browseDocumentation(FDOCTYPE.example);
}


export async function browsePython() {
    return browseDocumentation(FDOCTYPE.python);
}