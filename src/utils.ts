import * as path from 'path';
import * as os from "os";
import * as fs from 'fs';


export function saveTempFile(filename: string, text: string) {
    const filepath = path.join(getExtentionTempDir(), filename);
    fs.writeFileSync(filepath, text);
    return filepath;
}

export function getExtentionTempDir() {
    const tempDir = path.join(os.tmpdir(), "VSCode-MotionBuilder-Utils");
    if (!fs.existsSync(tempDir)) {
        fs.mkdirSync(tempDir);
    }
    return tempDir;
}


export function readJson(filepath: string) {
    const fileContent = fs.readFileSync(filepath);
    return JSON.parse(fileContent.toString());
}