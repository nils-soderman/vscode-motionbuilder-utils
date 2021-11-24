import * as path from 'path';
import * as os from "os";
import * as fs from 'fs';


const TEMPFOLDER_NAME = "VSCode-MotionBuilder-Utils";


export function saveTempFile(filename: string, text: string) {
    const filepath = path.join(getExtentionTempDir(), filename);
    fs.writeFileSync(filepath, text);
    return filepath;
}


export function getExtentionTempDir(bEnsureExists = true) {
    const tempDir = path.join(os.tmpdir(), TEMPFOLDER_NAME);
    if (bEnsureExists && !fs.existsSync(tempDir)) {
        fs.mkdirSync(tempDir);
    }
    return tempDir;
}


export function cleanupTempFiles() {
    const tempDir = getExtentionTempDir();
    if (fs.existsSync(tempDir)) {
        fs.rmdirSync(tempDir, { recursive: true });
    }
}


export function readJson(filepath: string) {
    const fileContent = fs.readFileSync(filepath);
    return JSON.parse(fileContent.toString());
}