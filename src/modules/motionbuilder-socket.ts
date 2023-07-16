import * as net from 'net';

class ErrorWithCode extends Error {
    constructor(message: string, public code?: string) {
        super(message);
    }
}

export class MotionBuilderSocket {
    private socket?: net.Socket;
    private isReady = false;

    private writeQueue: { command: string, resolve: (value: string) => void, reject: (error: Error) => void }[] = [];
    private isExecuting = false;

    constructor(
        public readonly ip = '127.0.0.1',
        public readonly port = 4242
    ) {
    }

    private onError(e: Error) {
        this.socket?.destroy();
    }


    private onClose() {
        this.socket = undefined;
        this.isReady = false;
    }


    /**
     * Write to the socket and wait for a response.
     * @param buffer The data to write to the socket
     * @returns 
     */
    private write(buffer: string | Uint8Array): Promise<string> {
        return new Promise((resolve, reject) => {
            if (!this.isOpen()) {
                reject(new Error('Socket is not ready, you must wait for the open promise to resolve.'));
                return;
            }

            this.writeQueue.push({ command: buffer.toString(), resolve, reject });

            if (!this.isExecuting) {
                this.executeNextCommand();
            }
        });
    }

    private executeNextCommand() {
        const command = this.writeQueue.shift();
        if (!command || !this.isOpen()) {
            this.isExecuting = false;
            return;
        }
        this.isExecuting = true;

        this.socket?.write(command.command, (error) => {
            if (error) {
                command.reject(error);
                this.executeNextCommand();
                return;
            }
        });

        let recivedBuffer = '';
        this.socket?.on('data', (chunk: Buffer) => {
            recivedBuffer += chunk.toString('utf8');

            if (recivedBuffer.trimEnd().endsWith('>>>')) {
                this.socket?.removeAllListeners('data');
                const outputData = recivedBuffer.trimEnd().slice(0, -3).trimEnd(); // Remove the >>> & trailing whitespace
                command.resolve(outputData);
                this.executeNextCommand();
            }
        });
    }

    on(event: 'close', listener: (...args: any[]) => void) {
        this.socket?.on(event, listener);
    }

    isOpen(): boolean {
        return this.socket !== undefined && this.socket.writable && this.isReady;
    }

    /**
     * Opens a connection to MotionBuilder, this must be called before any other methods.
     * @param timeoutInSeconds How long to wait for a connection before timing out. Set to 0 to disable timeout.
     * @returns A promise that resolves when the connection is ready.
     */
    open(timeoutInSeconds = 10): Promise<void> {
        this.socket = net.createConnection(this.port, this.ip);

        this.socket.on('error', this.onError);
        this.socket.on("close", this.onClose);

        return new Promise((resolve, reject: (error: Error) => void) => {
            let timeout: NodeJS.Timeout | undefined = undefined;
            if (timeoutInSeconds > 0) {
                timeout = setTimeout(() => {
                    reject(new ErrorWithCode('Connection timed out', "ETIMEDOUT"));
                    this.socket?.destroy();
                }, timeoutInSeconds * 1000);
            }

            this.socket?.on('data', (data) => {
                const dataStr = data.toString().trimEnd();

                if (dataStr.endsWith('>>>')) {
                    this.socket?.removeAllListeners('data');
                    this.isReady = true;
                    clearTimeout(timeout);
                    resolve();
                }
            });

            this.socket?.once('error', (error: any) => {
                clearTimeout(timeout);
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
     * Execute a python statement in MotionBuilder.
     * @param command Python code to run. To run multiple statements, seperate them with a semicolon.
     * @returns Python output such as print statements or errors
     */
    exec(command: string): Promise<string> {
        return this.write(command);
    }
}