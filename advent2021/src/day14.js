import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    // fileName = "D:/aoc/advent2021/data/d14_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    let seed;
    const multipliers = {};
    lines.forEach(line => {
        if (line.length > 0) {
            if (line.includes("-")) {
                const splitted = line.split(" -> ");
                const left = splitted[0];
                const right = splitted[1];

                multipliers[left] = left[0] + right;
            } else {
                seed = line;
            }

        }
    });


    const result = rabbit(seedSplitter(seed), multipliers);


    const tally = {};

    for (const char of result) {
        const tmp = tally[char];

        if (tmp == null) {
            tally[char] = 1;
        } else {
            tally[char]++;
        }
    }


    let min = Infinity;
    let max = 0;

    for (const [k, v] of Object.entries(tally)) {
        max = max > v ? max : v;
        min = min < v ? min : v;
    }

    tools.cprint(max-min);
    let debug = 1;


}


function seedSplitter(seed) {
    const seeds = [];

    for (let i = 0; i < seed.length - 1; i++) {
        seeds.push(seed[i] + seed[i + 1]);
    }

    return seeds;
}

function rabbit(seeds, multipliers) {
    const rep = 10;
    let retval;
    Array.from(Array(rep)).forEach(() => {
        let newSeed = "";
        for (let i = 0; i < seeds.length; i++) {
            const current = seeds[i];
            const tmp = multipliers[current];

            if (tmp == null) {
                newSeed += current;
            } else {
                newSeed += tmp;
                if (i == seeds.length - 1) {
                    newSeed += current[1];
                }
            }
        }
        seeds = seedSplitter(newSeed);
        tools.cprint(seeds.length);
        retval = newSeed;
    });

    return retval;
}


// maybe we can calculate and morph the pair without keeping arrays and string concatenation 
// and treat the segments separately 
 
main();