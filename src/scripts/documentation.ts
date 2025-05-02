import * as vscode from 'vscode';

import * as htmlParser from 'node-html-parser';

import * as logging from '../modules/logging';
import * as mobu from '../modules/motionbuilder-console';
import * as utils from '../modules/utils';

import * as github from '../modules/github';


// Constants
const GITHUB_EXTENSION_REPOSITORY_NAME = "nils-soderman/vscode-motionbuilder-utils";
const DOCUMENTATION_FOLDER = "documentation/table_of_contents";

let gCurrentVersion: number | null = null;


interface IDocumentationQuickPickItem extends vscode.QuickPickItem {
    url: string;
}

interface IDocumentationToc {
    version: number;
    base_url: string;
    items: IDocumentationQuickPickItem[];
}


async function getCurrentVersion(): Promise<number | null> {
    if (gCurrentVersion === null) {
        const filepath = vscode.Uri.joinPath(utils.getPythonDir(), "info.py");
        gCurrentVersion = await mobu.evaluateFunction<number>(filepath, "version", {}, true);
    }

    return gCurrentVersion;
}

async function getDocumentationDirectory(context: vscode.ExtensionContext): Promise<vscode.Uri> {
    const uri = vscode.Uri.joinPath(context.globalStorageUri, "documentation");
    if (!await utils.uriExists(uri)) {
        await vscode.workspace.fs.createDirectory(uri);
    }
    return uri;
}

// -------------------------------------------------------
//               Python SDK Table of Contents
// -------------------------------------------------------

async function getAvailableVersions(): Promise<{ version: number; download_url: string; }[]> {
    const folderContents = await github.getContents(GITHUB_EXTENSION_REPOSITORY_NAME, DOCUMENTATION_FOLDER);
    return folderContents
        .filter(content => content.type === "file" && content.name.endsWith(".json") && !content.name.includes("examples"))
        .map(content => ({
            version: parseInt(content.name),
            download_url: content.download_url,
        }))
        .filter(content => !isNaN(content.version))
        .sort((a, b) => a.version - b.version);
}

export async function getDocumentationTableOfContentsUri(context: vscode.ExtensionContext, version: number | null): Promise<vscode.Uri> {
    const cacheDir = await getDocumentationDirectory(context);
    if (version === null) {
        const files = (await vscode.workspace.fs.readDirectory(cacheDir))
            .filter(([name, type]) => type === vscode.FileType.File && !name.includes("examples"))
            .sort(([aName], [bName]) => aName.localeCompare(bName));
        if (files.length > 0) {
            // Get the latest version from the cache
            const latestFile = files[files.length - 1][0];
            return vscode.Uri.joinPath(cacheDir, latestFile);
        }

        // Get the latest version
        const latestVersion = await getAvailableVersions();
        if (latestVersion.length === 0) {
            throw new Error("No documentation found!");
        }

        version = latestVersion[latestVersion.length - 1].version;
    }

    // Check if version already exists
    const targetFilepath = vscode.Uri.joinPath(cacheDir, `${version}.json`);
    if (await utils.uriExists(targetFilepath)) {
        return targetFilepath;
    }

    // Check if version exists on GitHub
    const availableVersions = await getAvailableVersions();
    let versionInfo = availableVersions.find(v => v.version === version);
    if (!versionInfo) {
        // Get the closest version
        versionInfo = availableVersions.reduce((closest, current) => {
            return Math.abs(current.version - version) < Math.abs(closest.version - version) ? current : closest;
        });
    }

    const content = await github.getRequest(versionInfo.download_url, 10_000);

    const outFilepath = vscode.Uri.joinPath(cacheDir, `${versionInfo.version}.json`);
    await vscode.workspace.fs.writeFile(outFilepath, Buffer.from(content));

    return outFilepath;
}

async function getDocumentationTableOfContents(context: vscode.ExtensionContext, version: number | null): Promise<IDocumentationToc> {
    const filepath = await getDocumentationTableOfContentsUri(context, version);
    const data = await vscode.workspace.fs.readFile(filepath);
    return JSON.parse(data.toString()) as IDocumentationToc;
}


/**
 * List all pages from one or multiple documentation types, and open up the page selected by the user
 */
export async function browseDocumentation(context: vscode.ExtensionContext) {
    const currentVersion = await getCurrentVersion();
    const tableOfContents = await getDocumentationTableOfContents(context, currentVersion);

    const selection = await vscode.window.showQuickPick(tableOfContents.items, {
        placeHolder: "Select a page to open",
        title: `MotionBuilder ${tableOfContents.version} Documentation`,
    });
    if (!selection) {
        return;
    }

    await vscode.env.openExternal(vscode.Uri.parse(tableOfContents.base_url + selection.url));
}



// -------------------------------------------------------
//                        Examples
// -------------------------------------------------------

/**
 * Get the latest example from the GitHub repository
 */
async function getLatestExample() {
    const folderContents = await github.getContents(GITHUB_EXTENSION_REPOSITORY_NAME, DOCUMENTATION_FOLDER);
    const exampleFiles = folderContents.filter(content => content.type === "file" && content.name.endsWith(".json") && content.name.includes("examples"));
    if (exampleFiles.length === 0)
        return null;

    return exampleFiles[0];
}


let gCachedExamplesUri: vscode.Uri | null = null;

async function getExamplesTableOfContentsUri(context: vscode.ExtensionContext): Promise<vscode.Uri | null> {
    if (gCachedExamplesUri) {
        return gCachedExamplesUri;
    }

    const currentVersion = await getCurrentVersion();
    const cacheDir = await getDocumentationDirectory(context);

    // Check for cached examples on disk
    let cachedVersion = -1;
    let cachedExampleFilename = null;
    const exampleFiles = (await vscode.workspace.fs.readDirectory(cacheDir))
        .filter(([name, type]) => type === vscode.FileType.File && name.includes("examples"));
    if (exampleFiles.length > 0) {
        cachedExampleFilename = exampleFiles[0][0];
        cachedVersion = parseInt(cachedExampleFilename.split("_")[0]);
        gCachedExamplesUri = vscode.Uri.joinPath(cacheDir, cachedExampleFilename);
        if (currentVersion === null || currentVersion <= cachedVersion) {
            return gCachedExamplesUri;
        }
    }

    // Get the latest version
    const latestVersionContent = await getLatestExample();
    if (!latestVersionContent) {
        logging.showErrorMessage("No example files found in the GitHub repository.", Error(`No example files found at ${GITHUB_EXTENSION_REPOSITORY_NAME}/${DOCUMENTATION_FOLDER}`));
        return null;
    }

    const latestVersion = parseInt(latestVersionContent.name.split("_")[0]);
    if (isNaN(latestVersion)) {
        logging.showErrorMessage("Failed to parse the latest version from the example files.", Error(`Failed to parse the latest version from ${latestVersionContent.name}`));
        return null;
    }

    if (cachedVersion < latestVersion) {
        // Download the latest version
        const content = await github.getRequest(latestVersionContent.download_url, 10_000);
        const outFilepath = vscode.Uri.joinPath(cacheDir, latestVersionContent.name);

        await vscode.workspace.fs.writeFile(outFilepath, Buffer.from(content));

        // Delete all other cached examples
        for (const [name, type] of exampleFiles) {
            if (name !== latestVersionContent.name) {
                const filepath = vscode.Uri.joinPath(cacheDir, name);
                await vscode.workspace.fs.delete(filepath, { useTrash: false });
            }
        }

        gCachedExamplesUri = outFilepath;
    }

    return gCachedExamplesUri;
}


async function getExamplesTableOfContents(context: vscode.ExtensionContext): Promise<IDocumentationToc | null> {
    const filepath = await getExamplesTableOfContentsUri(context);
    if (!filepath) {
        return null;
    }

    const data = await vscode.workspace.fs.readFile(filepath);
    return JSON.parse(data.toString()) as IDocumentationToc;
}


/**
 * Open the code from a MotionBuilder example inside the editor
 * @param url The full URL to the example documentation web-page
 * @param title The title of the example, will be inserted as a header in the code
 */
async function openExampleInVSCode(url: string, title: string): Promise<vscode.TextEditor | undefined> {
    let data: string;
    try {
        data = await utils.httpsGetRequest(url, { timeout: 10_000 });
    }
    catch (error) {
        logging.showErrorMessage(`Failed to get: ${url}`, error as Error);
        return;
    }

    const parsedHtml = htmlParser.parse(data);

    let lines = parsedHtml.querySelectorAll(".line").map(line => {
        line.querySelectorAll(".lineno").forEach(e => e.remove());
        return line.text;
    });

    // The first line will be used as the tab title for unsaved documents
    lines.unshift(`# ${title}\n`);

    const content = lines.join("\n");

    const doc = await vscode.workspace.openTextDocument({ content, language: 'python' });

    return await vscode.window.showTextDocument(doc);
}


export async function browseExamples(context: vscode.ExtensionContext) {
    const tableOfContents = await getExamplesTableOfContents(context);
    if (!tableOfContents)
        return;

    const selection = await vscode.window.showQuickPick(tableOfContents.items, {
        placeHolder: "Select an example to open",
        title: `MotionBuilder ${tableOfContents.version} Examples`,
    });
    if (!selection) {
        return;
    }

    if (utils.getExtensionConfig().get<boolean>("documentation.openExamplesInEditor"))
        await openExampleInVSCode(tableOfContents.base_url + selection.url, selection.label);
    else
        await vscode.env.openExternal(vscode.Uri.parse(tableOfContents.base_url + selection.url));
}
