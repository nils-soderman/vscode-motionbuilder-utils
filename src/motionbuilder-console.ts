import * as vscode from 'vscode';
import * as net from 'net';


const DEFAULT_IP = '127.0.0.1';
const DEFAULT_PORT = 4242;

let gOutputChannel: vscode.OutputChannel;
let gSocket: net.Socket | null;


function getOutputChannel(bEnsureChannelExists = true) {
    if (!gOutputChannel && bEnsureChannelExists) {
        gOutputChannel = vscode.window.createOutputChannel("MotionBuilder");
    }
    return gOutputChannel;
}


function handleResponse(response: string) {
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

    gSocket = net.createConnection(DEFAULT_PORT, DEFAULT_IP);

    gSocket.on('error', (e) => {
        // TODO: option to show a more detailed error log
        vscode.window.showErrorMessage(`Failed to connect to MotionBuilder.`);
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
        /* If we want to remove the '>>>' logged in output
        if (dataRecived.endsWith(">>>")) {
            dataRecived = dataRecived.slice(0, -3).trimEnd();
        }
        */

        handleResponse(dataRecived);
    });

    return gSocket;
}



/**
 * 
 * @param command The command to run
 */
export async function runCommand(command: string) {

    // TODO: this should be an option
    if (false) {
        const outputChannel = getOutputChannel(false);
        if (outputChannel) {
            outputChannel.clear();
        }
    }

    const socket = await getSocket();
    if (!socket) {
        return;
    }

    // Send the commmand
    socket.write(command);
}
