import * as net from 'net';

export class MotionBuilderSocket {
    private socket?: net.Socket;
    private isReady = false;

    constructor(
        public readonly ip = '127.0.0.1',
        public readonly port = 4242
    ) {
    }

    private onError(e: Error) {
        if (e.message.includes("ECONNRESET")) {
            // Connection interupted. MotionBuilder was most likely closed
        }

        else {
            // Something has gone wrong
        }

        this.socket?.destroy();
    }

    private onClose() {
        this.socket = undefined;
    }

    /**
     * Opens a connection to MotionBuilder, this must be called before any other methods.
     * @returns A promise that resolves when the connection is ready.
     */
    open(): Promise<void> {
        this.socket = net.createConnection(this.port, this.ip);

        this.socket.on('error', this.onError);
        this.socket.on("close", this.onClose);

        return new Promise((resolve, reject: (error: Error) => void) => {
            this.socket?.on('data', (data) => {
                const dataStr = data.toString().trimEnd();

                if (dataStr.endsWith('>>>')) {
                    this.socket?.removeAllListeners('data');
                    this.isReady = true;
                    resolve();
                }
            });

            this.socket?.once('error', (error: any) => {
                reject(error);
            });
        });
    }

    /**
     * Close this socket connection
     */
    close() {
        this.socket?.destroy();
    }

    /**
     * Write to the socket and wait for a response.
     * Consider using exec() instead if you want to run a command.
     * @param buffer The data to write to the socket
     * @returns 
     */
    write(buffer: string | Uint8Array): Promise<string> {
        return new Promise((resolve, reject) => {
            if (!this.socket || !this.isReady) {
                reject(new Error('Socket is not ready, you must wait for the open promise to resolve.'));
                return;
            }

            this.socket.write(buffer, (error) => {
                if (error) {
                    reject(error);
                    return;
                }
            });

            let recivedBuffer = '';
            this.socket?.on('data', (chunk: Buffer) => {
                recivedBuffer += chunk.toString('utf8');

                if (recivedBuffer.trimEnd().endsWith('>>>')) {
                    this.socket?.removeAllListeners('data');
                    resolve(recivedBuffer);
                }
            });
        });
    }

    /**
     * Execute a python statement in MotionBuilder.
     * @param command Python code to run. To run multiple statements, seperate them with a semicolon.
     * @returns Python output such as print statements or errors
     */
    exec(command: string): Promise<string> {
        if (!command.endsWith('\n')) {
            command += '\n';
        }

        return this.write(command);
    }
}