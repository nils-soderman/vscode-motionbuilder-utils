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

/** Documentation table of content types */
export enum EDocType {
    example = "examples.json",
    python = "python.json"
};


async function getCurrentVersion(): Promise<number | null> {
    if (gCurrentVersion === null) {
        const filepath = vscode.Uri.joinPath(utils.getPythonDir(), "info.py");
        gCurrentVersion = await mobu.evaluateFunction<number>(filepath, "version");
    }

    return gCurrentVersion;
}

function getDocumentationDirectory(context: vscode.ExtensionContext): vscode.Uri {
    return vscode.Uri.joinPath(context.globalStorageUri, "documentation");
}

async function getDocumentationTableOfContentsUri(context: vscode.ExtensionContext, type: EDocType, version: number | null): Promise<vscode.Uri> {
    const cacheDir = getDocumentationDirectory(context);
    if (version === null) {
        let directories = (await vscode.workspace.fs.readDirectory(cacheDir));
        directories.sort(([aName], [bName]) => aName.localeCompare(bName));
        for (const [name, type] of directories) {
            if (type === vscode.FileType.Directory) {
                const folderVersion = parseInt(name);
                const filepath = vscode.Uri.joinPath(cacheDir, name, type.toString());
                if (!isNaN(folderVersion) && await utils.uriExists(filepath)) {
                    return filepath;
                }
            }
        }

        // Get the latest version
        const latestVersion = await getAvailableVersions();
        if (latestVersion.length === 0) {
            throw new Error("No documentation found!");
        }

        version = latestVersion[latestVersion.length - 1].version;
    }

    // Check if version already exists
    const filepath = vscode.Uri.joinPath(cacheDir, version.toString(), type.toString());
    if (await utils.uriExists(filepath)) {
        return filepath;
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

    // Download the documentation
    const contentList = await github.getContents(GITHUB_EXTENSION_REPOSITORY_NAME, versionInfo.path);
    const file = contentList.find(content => content.name === type.toString());
    if (!file) {
        throw new Error(`Documentation file not found for version ${version}`);
    }
    const content = await github.getRequest(file.download_url, 10_000);

    vscode.workspace.fs.createDirectory(vscode.Uri.joinPath(cacheDir, versionInfo.version.toString()));
    await vscode.workspace.fs.writeFile(filepath, Buffer.from(content));

    return filepath;
}


async function getDocumentationTableOfContents(context: vscode.ExtensionContext, type: EDocType, version: number | null): Promise<IDocumentationToc> {
    const filepath = await getDocumentationTableOfContentsUri(context, type, version);
    const data = await vscode.workspace.fs.readFile(filepath);
    return JSON.parse(data.toString()) as IDocumentationToc;
}


async function getAvailableVersions(): Promise<{ version: number; path: string; }[]> {
    const folderContents = await github.getContents(GITHUB_EXTENSION_REPOSITORY_NAME, DOCUMENTATION_FOLDER);
    return folderContents
        .filter(content => content.type === "dir")
        .map(content => ({
            version: parseInt(content.name),
            path: content.path
        }))
        .filter(content => !isNaN(content.version))
        .sort((a, b) => a.version - b.version);
}


/**
 * Open the code from a MotionBuilder example inside the editor
 * @param url The full URL to the example documentation web-page
 * @param filename The abs filepath where to save the file on disk
 */
async function openExampleInVSCode(url: string) {
    let data: string;
    try {
        data = await utils.httpsGetRequest(url, { timeout: 10_000 });
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

    const doc = await vscode.workspace.openTextDocument({ content, language: 'python' });

    return await vscode.window.showTextDocument(doc);
}


/**
 * List all pages from one or multiple documentation types, and open up the page selected by the user
 * @param type List of types to include, types should be of `FDOCTYPE`
 */
export async function browseDocumentation(context: vscode.ExtensionContext, type: EDocType) {
    const currentVersion = await getCurrentVersion();
    const tableOfContents = await getDocumentationTableOfContents(context, type, currentVersion);

    const selection = await vscode.window.showQuickPick(tableOfContents.items, {
        placeHolder: "Select a page to open",
    });
    if (!selection) {
        return;
    }

    if (type == EDocType.example && utils.getExtensionConfig().get<boolean>("documentation.openExamplesInEditor")) {
        // Open in VSCode
        await openExampleInVSCode(tableOfContents.base_url + selection.url);
    }
    else {
        await vscode.env.openExternal(vscode.Uri.parse(tableOfContents.base_url + selection.url));
    }
}
