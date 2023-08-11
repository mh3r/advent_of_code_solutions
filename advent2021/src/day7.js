import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d7_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const crabs = [];
    const crabsTally = {};
    lines.forEach(line => {
        crabs.push(...line.split(",").map(x => Number(x)));
    });


    crabs.forEach(x => {
        const tmp = crabsTally[x];
        if (tmp == undefined) {
            crabsTally[x] = 1;
        } else {
            crabsTally[x]++;
        }

    });

    const sum = crabs.reduce((a, b) => a + b, 0);
    const avg = Math.ceil(sum / crabs.length);
    const min = findLowestFuel(avg, crabsTally);
    tools.cprint(min);
    // tools.cprint(calculateCrabCost(3));
}

function findLowestFuel(avg, crabsTally) {
    let minLowest = Infinity;
    for (let i = avg; i >= 0; i--) {
        const cost = calculateFuelCost(i, crabsTally);
        if (cost < minLowest) {
            minLowest = cost;
        } else {
            break;
        }

    }
    return minLowest;
}

function calculateFuelCost(dest, crabsTally) {
    let cost = 0;
    for (const [pos, value] of Object.entries(crabsTally)) {
        cost += calculateCrabCost(Math.abs(dest - Number(pos))) * value;
    }
    return cost;
}


function calculateCrabCost(distance) {
    let cost = 0;
    if (distance > 0) {
        for (let i = 1; i <= distance; i++) {
            cost += i;
        }
    }
    return cost;
}

main();