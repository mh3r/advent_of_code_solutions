import { debug } from 'console';
import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;
const END = "end";

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d12_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const cavern = {};
    populateCavern(lines, cavern);

    spelunking(cavern);
    let debug = 1;


}

function populateCavern(lines, cavern) {
    lines.forEach(line => {
        // line = line.replaceAll("end", END);
        const splitted = line.split("-");
        const left = splitted[0];
        const right = splitted[1];

        if (left == "dc") {
            let debuggg = 1;
        }
        connectCavern(left, right, cavern);
        connectCavern(right, left, cavern);
    });
}

function connectCavern(left, right, cavern) {
    if (right == "start") return;

    let tmp = cavern[left];
    if (tmp == undefined) {
        cavern[left] = {};
        cavern[left].small = [];
        cavern[left].big = [];
    }
    if (right[0].charCodeAt(0) < 97) {
        cavern[left].big.push(right);
    } else {
        cavern[left].small.push(right);
    }
}

function spelunking(cavern) {
    const paths = [];


    rabbitHoleRec("start", cavern, paths);


    tools.cprint(paths.length);
    let debug = 1;

}


function rabbitHoleRec(currentPathway, cavern, paths) {
    const splitted = currentPathway.split("-");
    const current = splitted[splitted.length - 1];

    if (current == END) {
        paths.push(currentPathway);
        return;
    }

    const currentNode = cavern[current];

    const potentialPaths = [...currentNode.big];
    potentialPaths.push(...currentNode.small);

    for (const potential of potentialPaths) {
        // if (potential[0].charCodeAt(0) >= 97 && hasVisitedThatSmall(currentPathway, potential)) {
        //     continue;
        // }
        if (potential[0].charCodeAt(0) >= 97 && weirdCaveScenario(currentPathway, potential)) {
            continue;
        }

        rabbitHoleRec(currentPathway + "-" + potential, cavern, paths)
    }


}

function hasVisitedThatSmall(pathway, target) {
    return pathway.split("-").filter(x => x[0].charCodeAt(0) >= 97).includes(target);
}

function weirdCaveScenario(pathway, target) {
    const allSmall = pathway.split("-").filter(x => x[0].charCodeAt(0) >= 97);
    const newSet = new Set(allSmall);
    const hasDouble = allSmall.length != newSet.size;

    return hasDouble && allSmall.includes(target);
}

main();