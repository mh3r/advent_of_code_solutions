import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d13_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    let coords = [];
    let folds = []
    lines.forEach(line => {
        if (line.length > 0) {
            if (line.startsWith("fold")) {
                folds.push(line.split(" ")[2]);
            } else {
                coords.push(line);
            }

        }
    });


    for (const instruction of folds) {
        coords = fold(coords, instruction);
    }
    tools.cprint(coords.length);

    specialPrint(coords);

}

function specialPrint(coords) {
    const display = [];

    let maxX;
    let maxY;
    const yx = [];
    for (const coord of coords) {
        const splitted = coord.split(",");
        let x = Number(splitted[0]);
        let y = Number(splitted[1]);
        maxX = maxX > x ? maxX : x;
        maxY = maxY > y ? maxY : y;
    }


    for (let y = 0; y <= maxY +1; y++) {
        let line = [];
        for (let x = 0; x <= maxX+1; x++) {
            if (coords.includes(`${x},${y}`)) {
                line.push("o");
            } else {
                line.push(" ");
            }
        }
        display.push(line);
    }

    // RGZLBHFP
    tools.printBoard(display);
}


function fold(coords, instruction) {
    const splitted = instruction.split("=");
    const axis = splitted[0] == "y" ? foldY : foldX;
    return axis(coords, Number(splitted[1]));
}

function foldY(coords, yAxis) {
    let top = [];
    let bottom = [];
    for (const row of coords) {
        const splitted = row.split(",");
        const y = Number(splitted[1]);

        if (y < yAxis) {
            top.push(row);
        } else {
            bottom.push(row);
        }

    }

    for (const row of bottom) {
        const splitted = row.split(",");
        const newY = 2 * yAxis - Number(splitted[1]);

        const newCoord = splitted[0] + "," + newY;
        if (!top.includes(newCoord)) {
            top.push(newCoord);
        }
    }
    let debug = 1;

    return top;
}

function foldX(coords, xAxis) {
    let left = [];
    let right = [];
    for (const row of coords) {
        const splitted = row.split(",");
        const x = Number(splitted[0]);

        if (x < xAxis) {
            left.push(row);
        } else {
            right.push(row);
        }

    }

    for (const row of right) {
        const splitted = row.split(",");
        const newX = 2 * xAxis - Number(splitted[0]);

        const newCoord = newX + "," + splitted[1];
        if (!left.includes(newCoord)) {
            left.push(newCoord);
        }
    }
    let debug = 1;

    return left;
}


main();