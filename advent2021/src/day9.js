import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;
const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];


function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d9_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    let board = [];

    lines.forEach(line => {
        board.push(line.split("").map(x => Number(x)));
    });

    const lowestPoints = process(board);
    const area = goNiners(lowestPoints, board);
    tools.cprint(area);

}


function process(board) {
    let total = 0;
    const lowestPoints = [];
    for (let y = 0; y < board.length; y++) {
        for (let x = 0; x < board[0].length; x++) {
            if (checkForLowest(y, x, board)) {
                total += board[y][x] + 1;
                lowestPoints.push([y, x]);
            }
        }
    }
    tools.cprint(total);

    return lowestPoints;
}

function goNiners(lowestPoints, board) {
    let total = 0;
    let lakes = {};

    for (const point of lowestPoints) {
        const filledCoords = [];
        const toVisit = [point];
        filledCoords.push(tools.bindArray(point));

        while (toVisit.length > 0) {
            const current = toVisit.shift();
            const [y, x] = current;


            for (const [dy, dx] of tools.ADJ_DIRS) {
                let tmpY = y + dy;
                let tmpX = x + dx;
                if (tmpY >= 0
                    && tmpX >= 0
                    && tmpY < board.length
                    && tmpX < board[0].length
                    && !filledCoords.includes(tools.bindArray([tmpY, tmpX]))
                    && board[tmpY][tmpX] != 9
                ) {
                    toVisit.push([tmpY, tmpX]);
                    filledCoords.push(tools.bindArray([tmpY, tmpX]));

                    let debugg = 1;
                }
            }
        }

        lakes[tools.bindArray(point)] = filledCoords.length;
    }
    tools.printJson(lakes);

    const totals = [];
    for (const [key, value] of Object.entries(lakes)) {
        totals.push(value);
    }

    totals.sort((a, b) => b - a);
    const topThree = totals.splice(0, 3).reduce((a, b) => a * b, 1);



    tools.cprint(topThree);
    return total;

}

function checkForLowest(y, x, board) {
    let retval = true;

    const current = board[y][x];
    for (const [dy, dx] of directions) {
        let tmpY = y + dy;
        let tmpX = x + dx;
        if (tmpY >= 0
            && tmpX >= 0
            && tmpY < board.length
            && tmpX < board[0].length
        ) {
            if (current >= board[tmpY][tmpX]) {
                retval = false;
                break;
            }
        }
    }

    return retval;

}

main();