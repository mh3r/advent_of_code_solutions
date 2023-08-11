import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d2_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const start = [0, 0];
    let aim = 0;
    lines.forEach(line => {
        const splitted = line.split(" ");
        const quant = Number(splitted[1]);
        if (line.includes("forward")) {
            start[1] += quant;
            start[0] += quant * aim;
        }
        if (line.includes("down")) {  aim += quant; }
        if (line.includes("up")) { aim -= quant; }

    });
    tools.cprint(start[0] * start[1]);


}



main();