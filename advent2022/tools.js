import { readFile, readFileSync } from 'fs';

export function readFileFromLocal(fileName) {
    return readFileSync(fileName, 'utf-8');
}


export function printJson(data) {
    console.log(JSON.stringify(data, null, 2));
}

export function cprint(data) {
    console.log(data);
}

export function printBoard(array) {
    for (const line of array) {
        cprint(line.join(""))
    }
}

 