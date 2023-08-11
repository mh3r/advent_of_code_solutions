import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

const errorPrices = [3, 57, 1197, 25137];
// ): 3 points.
// ]: 57 points.
// }: 1197 points.
// >: 25137 points.
const opens = "([{<";
const opens1 = ["(", "[", "{", "<"];
const closes = ")]}>";
const closes1 = [")", "]", "}", ">"];

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d10_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();



    lines.forEach(line => {

    });

    process(lines);


}


function process(lines) {
    const bracketCounter = [];
    const completers = [];
    for (let i = 0; i < lines.length; i++) {

        const splitted = lines[i].split("");
        // tools.cprint(splitted);

        // const openSize = splitted.filter(x => opens.indexOf(x) > 0).length;


        const openQueue = [];
        let ignore = false;
        for (let x = 0; x < lines[i].length; x++) {
            const char = lines[i].charAt(x);
            if (opens.indexOf(char) >= 0) {
                openQueue.push(char);
            } else {
                const lastChar = openQueue[openQueue.length - 1];

                const lastCharIndex = opens.indexOf(lastChar);
                if (char == closes.charAt(lastCharIndex)) {
                    openQueue.pop();
                } else {
                    bracketCounter.push(closes.indexOf(char));
                    ignore = true;
                    break;
                }
            }
        }

        if (!ignore) {
            // tools.cprint(openQueue.join(""));
            completers.push(openQueue.join(""));
        }
    }

    let total = 0;
    bracketCounter.forEach(x => total += errorPrices[x]);
    tools.cprint(total);

    // part2
    let total2 = [];
    for (const completer of completers) {
        let midTotal = 0;
        for (let i = completer.length - 1; i >= 0; i--) {
            midTotal *= 5;
            midTotal += opens.indexOf(completer[i]) + 1;

        }
        total2.push(midTotal);


    }

    total2.sort((a, b) => a - b)
    tools.cprint(total2[Math.floor(total2.length / 2)]);


    let debug = 1;

}


main();