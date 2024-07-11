/**
 * This file contains mock classes and functions for testing vscode extensions
 */
import * as vscode from 'vscode';

import sinon from 'sinon';


export class ConfigMock {
    globalValue: Record<string, any>;
    workspaceValue: Record<string, any>;
    workspaceFolderValue: Record<string, any>;

    constructor(readonly defaultValue: Record<string, any>) {
        this.globalValue = { ...defaultValue };
        this.workspaceValue = { ...defaultValue };
        this.workspaceFolderValue = { ...defaultValue };
    }

    get(key: string, defaultValue?: any) {
        return this.globalValue[key] || defaultValue;
    }

    inspect(key: string) {
        return {
            key: key,
            globalValue: this.globalValue[key],
            workspaceValue: this.workspaceValue[key],
            workspaceFolderValue: this.workspaceFolderValue[key],
            defaultValue: this.defaultValue[key]
        };
    }

    update(key: string, value: any, configurationTarget?: boolean | vscode.ConfigurationTarget, overrideInLanguage?: boolean) {
        if (configurationTarget === vscode.ConfigurationTarget.Workspace)
            this.workspaceValue[key] = value;
        else if (configurationTarget === vscode.ConfigurationTarget.WorkspaceFolder)
            this.workspaceFolderValue[key] = value;
        else
            this.globalValue[key] = value;

        return Promise.resolve();
    }

    has(key: string) {
        return this.globalValue[key] !== undefined;
    }

    reset() {
        this.globalValue = { ...this.defaultValue };
        this.workspaceValue = { ...this.defaultValue };
        this.workspaceFolderValue = { ...this.defaultValue };
    }
}

/**
 * Create a stub for vscode.window.showQuickPick that returns the first item in the list
 */
export function stubShowQuickPick() {
    let showQuickPickStub = sinon.stub(vscode.window, 'showQuickPick');

    showQuickPickStub.callsFake(async (items: readonly vscode.QuickPickItem[] | Thenable<readonly vscode.QuickPickItem[]>, options: vscode.QuickPickOptions | undefined, token?: vscode.CancellationToken | undefined) => {
        return new Promise(async (resolve) => {
            resolve((await items)[0]);
        });
    });

    return showQuickPickStub;
}

export function stubGetConfiguration(config: Record<string, ConfigMock>) {
    const getConfigurationStub = sinon.stub(vscode.workspace, 'getConfiguration');

    getConfigurationStub.callsFake((section?: string, scope?: vscode.ConfigurationScope | null) => {
        if (!section) {
            throw new Error('Section is required');
        }

        return config[section] as vscode.WorkspaceConfiguration;
    });

    return getConfigurationStub;
}