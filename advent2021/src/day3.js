import { cp } from 'fs';
import { deflate } from 'zlib';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d3_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    let gamma = "";
    let epsilon = "";

    for (let i = 0; i < lines[0].length; i++) {
        let counter0 = 0;
        let counter1 = 0;
        for (let y = 0; y < lines.length; y++) {
            if (lines[y][i] == "0") {
                counter0++
            }
            else {
                counter1++;
            }
        }

        if (counter0 > counter1) {
            gamma += "0";
            epsilon += "1";
        } else {
            gamma += "1";
            epsilon += "0";
        }
    }

    tools.cprint(gamma);
    tools.cprint(epsilon);
    tools.cprint(parseInt(gamma, 2) * parseInt(epsilon, 2))

    let oxygenRating = findRating(lines, gamma, "1");
    let c02Rating = findRating(lines, epsilon, "0");

    tools.cprint(oxygenRating);
    tools.cprint(c02Rating);
    tools.cprint(parseInt(oxygenRating, 2) * parseInt(c02Rating, 2));
    // 939360 is wrong?? is too low.

}

function findRating(lines, modifier, defaultValue) {
    let tmpArray1 = [];
    let tmpArray2 = [];
    let commonString = "";
    for (const char of modifier) {
        tmpArray1 = lines.filter(x => x.startsWith(commonString + char));
        const reverse = (char == "1") ? "0" : "1";
        tmpArray2 = lines.filter(x => x.startsWith(commonString + reverse));

        if (tmpArray1.length == tmpArray2.length) {
            commonString += defaultValue;
        } else {
            commonString += char;
        }

        if (tmpArray1.length == 1) {
            return lines.filter(x => x.startsWith(commonString))[0];
        }

    }
}

main();