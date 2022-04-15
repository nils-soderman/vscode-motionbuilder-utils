import * as vscode from 'vscode';

import * as net from 'net'; 

const IP = '127.0.0.1';
const PORT = 4242;

let gSocket: net.Socket | undefined;
let onDataRecived: Function;


async function getSocket() {
    if (gSocket !== undefined) {
        // TODO: Validate connection, may not be needed. As if we drop connection we now set gSocket to be undefined
        return gSocket;
    }

    gSocket = net.createConnection(PORT, IP);

    gSocket.on('error', (e) => {
        if (e.message.includes("ECONNRESET")) {
            // Connection interupted. MotionBuilder was most likely closed
        }

        else if (e.message.includes("ECONNREFUSED")) {
            // Failed to connect
            // TODO: Should probably link to a trouble-shooting page.
            vscode.window.showErrorMessage(`Failed to connect to MotionBuilder.`);
        }

        else {
            // Something has gone wrong, print error
            // TODO: option to show a more detailed error log
            vscode.window.showErrorMessage(`MotionBuilder: Something went wrong when trying to connect to MB.\n${e.stack}`);
            console.log(e.stack);
        }

        if (gSocket) {
            gSocket.destroy();
        }
    });

    let bSocketEstablished = false;
    
    gSocket.on("data", function (buffer) {
        let dataRecived = buffer.toString("utf8");

        if (!bSocketEstablished) {
            if (!dataRecived.includes(">>>")) {
                return;
            }

            bSocketEstablished = true;
            dataRecived = dataRecived.split(">>>", 1)[1];
            if (!dataRecived) {
                return;
            }

        }

        dataRecived = dataRecived.trim();
        if (onDataRecived != undefined) {
            onDataRecived(dataRecived);
        }
    });

    gSocket.on('close', (h: any | undefined) => {
        gSocket = undefined;
    });

    return gSocket;
}


/**
 * 
 * @param command The command to run
 */
export async function runCommand(command: string, callback: Function) {
    const socket = await getSocket();
    if (!socket) {
        return;
    }

    onDataRecived = callback;

    // Send the commmand
    socket.write(command);
}


export async function executeFile(filepath: string, callback: Function) {
    runCommand(`with open(r'${filepath}','r')as f:exec(f.read())\n`, callback);
}