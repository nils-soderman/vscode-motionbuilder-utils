import * as vscode from 'vscode';

import * as net from 'net';

// import { TelnetSocket } from "telnet-stream";

const DEFAULT_IP = '127.0.0.1';
const DEFAULT_PORT = 4242;

let gOutputChannel: vscode.OutputChannel;
let gSocket: net.Socket;


function getOutputChannel(bEnsure = true) {
    if (!gOutputChannel && bEnsure) {
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder");
    }
    return gOutputChannel;
}


function handleResponse(recivedString: string) {
    let match = recivedString.match(/(>>>([^]*)>>>)/);
    if (!match) {
        return;
    }

    let response = match[0].trim().slice(3, -3).trim();
    response = response.replace(/\n\r/g, "\n");

    const outputChannel = getOutputChannel();

    outputChannel.appendLine(response);

    // TODO: this should be an option
    outputChannel.show(true);
}


async function getSocket() {
    if (gSocket) {
        // TODO: Validate connection, otherwise try to re-connect
        return gSocket;
    }

    const socket = net.createConnection(DEFAULT_PORT, DEFAULT_IP);

    socket.on('error', (e) => {
        console.error(e);
        socket.destroy();
    });

    let fullResponse = "";

    socket.on("data", function (buffer) {
        fullResponse += buffer.toString("utf8");
        console.log("fullResponse: " + fullResponse);
        return;
        if (fullResponse.match(/(>>>([^]*)>>>)/)) {
            //socket.destroy();
            handleResponse(fullResponse);
        }
    });


    return socket;
}



/**
 * 
 * @param command The command to run
 */
export async function runCommand(command: string) {
    const outputChannel = getOutputChannel(false);

    // TODO: this should be an option
    if (outputChannel) {
        outputChannel.clear();
    }

    const socket = await getSocket();
    
    // Send the commmand
    socket.write(command);
}
