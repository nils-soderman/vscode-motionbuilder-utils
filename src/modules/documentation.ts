import * as vscode from 'vscode';

import * as mobu from './motionbuilder-console';
import * as utils from './utils';

enum EItemType {
    Enum = "enum",
    EnumMember = "enum-member",
    Class = "class",
    Function = "function",
    Method = "method",
    Property = "property",
}

interface IPyfbsdkItemData {
    label: string;
    type: EItemType;
    children?: IPyfbsdkItemData[];
}

const iconMap: Record<EItemType, vscode.ThemeIcon> = {
    [EItemType.Enum]: new vscode.ThemeIcon('symbol-enum'),
    [EItemType.EnumMember]: new vscode.ThemeIcon('symbol-enum-member'),
    [EItemType.Class]: new vscode.ThemeIcon('symbol-class'),
    [EItemType.Function]: new vscode.ThemeIcon('symbol-function'),
    [EItemType.Method]: new vscode.ThemeIcon('symbol-method'),
    [EItemType.Property]: new vscode.ThemeIcon('symbol-property'),
};


class PyfbsdkTreeItem extends vscode.TreeItem {
    type: EItemType;
    children?: PyfbsdkTreeItem[];

    constructor(
        item: IPyfbsdkItemData,
        defaultCollapsibleState: vscode.TreeItemCollapsibleState = vscode.TreeItemCollapsibleState.Collapsed,
        parent: PyfbsdkTreeItem | null = null
    ) {
        super(
            item.label,
            item.children?.length ? defaultCollapsibleState : vscode.TreeItemCollapsibleState.None
        );
        this.id = `${parent?.label}-${item.label}-${defaultCollapsibleState}`;
        this.type = item.type;

        this.children = item.children?.map(child => new PyfbsdkTreeItem(child, defaultCollapsibleState, this));
        this.iconPath = iconMap[item.type];
    }
}

export class PyfbsdkTreeProvider implements vscode.TreeDataProvider<PyfbsdkTreeItem> {
    private filters: string[] = [];

    private _onDidChangeTreeData: vscode.EventEmitter<PyfbsdkTreeItem | undefined | void> = new vscode.EventEmitter<PyfbsdkTreeItem | undefined | void>();
    readonly onDidChangeTreeData: vscode.Event<PyfbsdkTreeItem | undefined | void> = this._onDidChangeTreeData.event;

    constructor() { }

    refresh(): void {
        this._onDidChangeTreeData.fire();
    }

    async getTableOfContents(): Promise<IPyfbsdkItemData[] | null> {
        const script = vscode.Uri.joinPath(utils.getPythonDir(), "documentation.py");
        const toc = await mobu.evaluateFunction<IPyfbsdkItemData[]>(script, "get_content");
        return toc;
    }

    getTreeItem(element: PyfbsdkTreeItem) {
        return element;
    }

    private filterItems(items: IPyfbsdkItemData[]): IPyfbsdkItemData[] {
        if (this.filters.length === 0) {
            return items;
        }

        return items.filter(item => {
            const label = item.label.toLowerCase();
            if (this.filters.every(filter => label.includes(filter))) {
                return true;
            }
            if (item.children) {
                const filteredChildren = this.filterItems(item.children);
                if (filteredChildren.length > 0) {
                    item.children = filteredChildren;
                    return true;
                }
            }
            return false;
        });
    }

    async getChildren(element?: PyfbsdkTreeItem): Promise<PyfbsdkTreeItem[]> {
        if (element) {
            return element.children || [];
        }

        const toc = await this.getTableOfContents();
        if (!toc) {
            return [];
        }

        const defaultCollapsibleState = this.filters.length > 0 ? vscode.TreeItemCollapsibleState.Expanded : vscode.TreeItemCollapsibleState.Collapsed;

        return this.filterItems(toc).map(item => {
            let itema = new PyfbsdkTreeItem(item, defaultCollapsibleState);
            return itema;
        })
    }

    public applyFilter(filter: string) {
        this.filters = filter.toLowerCase().split(/\s+/).filter(Boolean);
        this.refresh();
    }
}



export class PyfbsdkApiSearchProvider implements vscode.WebviewViewProvider {
    private _view?: vscode.WebviewView;

    private _onInputChange: Array<(data: string) => void> = [];

    constructor(
        private readonly _extensionUri: vscode.Uri,
    ) { }

    public onInputChange(callback: (data: string) => void) {
        this._onInputChange.push(callback);
    }

    resolveWebviewView(
        webviewView: vscode.WebviewView,
        _context: vscode.WebviewViewResolveContext,
        _token: vscode.CancellationToken,
    ) {
        this._view = webviewView;

        webviewView.webview.options = {
            // Allow scripts in the webview
            enableScripts: true,

            localResourceRoots: [
                this._extensionUri
            ]
        };

        webviewView.webview.html = this._getHtmlForWebview(webviewView.webview);

        webviewView.webview.onDidReceiveMessage(data => {
            this._handleOnInputChanged(data);
        });
    }

    private _getHtmlForWebview(webview: vscode.Webview) {
        // Use a nonce to only allow a specific script to be run.

        return `
        <input
            class="monaco-inputbox"
            id="search"
            type="text"
            style="width: 100%; display: block; padding: 5px; font-size: 130%; background: var(--vscode-input-background); border: 1px solid gray; color: var(--vscode-input-foreground);"
            placeholder="Filter"
        />

        <script>
        let vscode = acquireVsCodeApi();
        let searchBox = document.getElementById("search");
        searchBox.addEventListener("input", function()
        {
            vscode.postMessage(searchBox.value);
        });
        </script>
    `;
    }

    _handleOnInputChanged(data: any) {
        this._onInputChange.forEach(callback => {
            callback(data);
        });
    }
}


// https://help.autodesk.com/cloudhelp/2025/ENU/MOBU-PYTHON-API-REF/classpyfbsdk_1_1_f_b_actor.html#a2588621fd23bed7d99e01afcc70b12fb
// https://help.autodesk.com/cloudhelp/2025/ENU/MOBU-PYTHON-API-REF/classpyfbsdk_1_1_f_b_body_node_id.html#a3aff0e391469e95d84217cae0e62450a
// https://help.autodesk.com/cloudhelp/2025/ENU/MOBU-PYTHON-API-REF/namespacepyfbsdk.html#abd10ff8451ab44da23aac4fd9ce644e5