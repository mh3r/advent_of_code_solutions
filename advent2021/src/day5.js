import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d5_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const movements = [];
    lines.forEach(line => {
        movements.push(line.replaceAll("->", ",").split(",").map(x => Number(x)));


    });


    processCoords(movements);
    // 16515 too low 
}


function processCoords(movements) {

    const board = {};
    for (const move of movements) {

        populateBoard(move, board);



    }

    let debug = 1;

    let overTwo = Object.entries(board).filter((k, v) => k[1] > 1).length;
    tools.cprint(overTwo);
}


function populateBoard(move, board) {
    const [x1, y1, x2, y2] = move
    // populate movement first 
    let coords = [];

    if (x1 == x2) {
        populateVertical(move, coords);
    } else if (y1 == y2) {
        populateHorizontal(move, coords);
    } else {
        populateDiagonal(move, coords);
    }


    for (const coord of coords) {
        const tmp = board[toString(coord)];

        if (tmp == undefined) {
            board[toString(coord)] = 1;
        } else {
            board[toString(coord)]++;
        }
    }
}

function populateVertical(move, coords) {
    const [x1, y1, x2, y2] = move;
    let start;
    let end;
    if (y1 < y2) {
        start = y1;
        end = y2;
    } else {
        start = y2;
        end = y1;
    }

    for (let i = start; i <= end; i++) {
        coords.push([x1, i]);
    }


}
function populateHorizontal(move, coords) {
    const [x1, y1, x2, y2] = move;
    let start;
    let end;
    if (x1 < x2) {
        start = x1;
        end = x2; 6
    } else {
        start = x2;
        end = x1;
    }

    for (let i = start; i <= end; i++) {
        coords.push([i, y1]);
    }


}

function populateDiagonal(move, coords) {
    const [x1, y1, x2, y2] = move;
    let start;
    let end;

    let upwardSign = 1;
    let verticalStart;

    if (x1 < x2) {
        start = x1;
        end = x2;
        verticalStart = y1;
        if (y1 > y2) {
            upwardSign = -1;
        }
    } else {
        start = x2;
        end = x1;
        verticalStart = y2;
        if (y2 > y1) {
            upwardSign = -1;
        }

    }

    for (let i = start; i <= end; i++) {
        coords.push([i, verticalStart + upwardSign * (i - start)]);
    }

}

function toString(coord) {
    return `${coord[0]}-${coord[1]}`;

}


main();