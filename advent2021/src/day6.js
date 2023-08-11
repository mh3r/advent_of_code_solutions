import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d6_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const fishFarm = [];
    lines.forEach(line => {
        fishFarm.push(...line.split(",").map(x => Number(x)))
    });

    const eden = {};

    Array.from(Array(9)).forEach((v, k) => {
        eden[k] = 0;
    });

    for (const fish of fishFarm) {
        eden[fish]++;

    }
    tools.printJson(eden);
    goForthAndMultiply(eden);

    // tools.cprint(fishFarm);
    // breedingProgram(fishFarm)
}


function goForthAndMultiply(eden) {
    let rep = 256;
    for (let i = 0; i < rep; i++) {
        let additionalSixAndEight = 0;
        for (let i = 0; i < 9; i++) {
            const tally = eden[i];


            if (i == 0) {
                additionalSixAndEight = tally;
            } else {
                eden[i - 1] = tally;
            }
        }
        eden[6] += additionalSixAndEight;
        eden[8] = additionalSixAndEight;
    }


    let total = 0;
    for (let i = 0; i < 9; i++) {
        total += eden[i];
    }

    tools.cprint(total);

}

function breedingProgram(fishFarm) {
    let rep = 80;
    for (let i = 0; i < rep; i++) {
        let newFish = 0;
        for (let f = 0; f < fishFarm.length; f++) {
            const fish = fishFarm[f];
            if (fish == 0) {
                fishFarm[f] = 6;
                newFish++;
            } else {
                fishFarm[f]--;
            }
        }

        for (let x = 0; x < newFish; x++) {
            fishFarm.push(8);
        }
    }

    tools.cprint(fishFarm.length);
}

main();