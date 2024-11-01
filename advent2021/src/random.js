import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;
const LEFT = "L";
const RIGHT = "R";
const ROOT = "r00t";
const origin = [0, 0]

function main() {
    fileName = "advent2021/data/test.txt";

    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    const firstPath = Array.from(lines[0].split(","))
    const secondPath = Array.from(lines[1].split(","))

    const firstSteps = traverse(firstPath);
    const secondSteps = traverse(secondPath);

    const intersections = firstSteps.filter(x => secondSteps.includes(x))
    console.log(intersections)

    const totalDistances = intersections.map(x => tools.manhattanDistance(origin, tools.unbindArray(x)))
    console.log(totalDistances)

    console.log("part 1 answer:", Math.min(...totalDistances))
    let debug = 1

    const stepsArray = []

    intersections.forEach(x => stepsArray.push(firstSteps.indexOf(x) + secondSteps.indexOf(x) + 2))

    console.log(stepsArray)
    console.log("part 2 answer:", Math.min(...stepsArray))
}







main();


