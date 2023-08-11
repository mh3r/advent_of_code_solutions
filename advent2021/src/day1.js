import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d1_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    lines.forEach(line => {

        // tools.cprint(line);
    });


    for (let i = 0; i < lines.length - 3; i++) {
        let tmp1 = Number(lines[i] )+ Number(lines[i + 1]) + Number(lines[i + 2]);
        let tmp2 = Number(lines[i + 1]) + Number(lines[i + 2]) + Number(lines[i + 3]);

        if (tmp1 < tmp2) {
            counter++;
        }

    }

    tools.cprint(counter)



}



main();