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
        item: IPyfbsdkItemData
    ) {
        super(
            item.label,
            item.children?.length ? vscode.TreeItemCollapsibleState.Collapsed : vscode.TreeItemCollapsibleState.None
        );
        this.type = item.type;

        this.children = item.children?.map(child => new PyfbsdkTreeItem(child));
        this.iconPath = iconMap[item.type];
    }
}

export class PyfbsdkTreeProvider implements vscode.TreeDataProvider<PyfbsdkTreeItem> {

    constructor() { }

    async getTableOfContents(): Promise<IPyfbsdkItemData[] | null> {
        const script = vscode.Uri.joinPath(utils.getPythonDir(), "documentation.py");
        const toc = await mobu.evaluateFunction<IPyfbsdkItemData[]>(script, "get_content");
        return toc;
    }

    getTreeItem(element: PyfbsdkTreeItem) {
        return element;
    }

    async getChildren(element?: PyfbsdkTreeItem): Promise<PyfbsdkTreeItem[]> {
        if (element) {
            return element.children || [];
        }

        const toc = await this.getTableOfContents();
        if (!toc) {
            return [];
        }

        return toc.map(item => {
            return new PyfbsdkTreeItem(item);
        });

    }
}

