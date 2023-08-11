import { privateDecrypt } from 'crypto';
import { cp } from 'fs';
import { totalmem } from 'os';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d11_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const board = []
    lines.forEach(line => {
        const row = line.split("");
        board.push(row.map(x => Number(x)));
    });


    party(board);

}

function party(board) {
    tools.printBoard(board);

    const rep = 330;
    let flashCounter = 0;
    let stepCounter = 0;
    Array.from(Array(rep)).forEach(() => {
        const niners = [];
        if (allLight(board)) {
            tools.cprint(stepCounter);

        }
        grow(board, niners);
        flash(board, niners);
        flashCounter += restoration(board);

        stepCounter++;
    })


    tools.cprint("\n\n")
    tools.printBoard(board);


    tools.cprint("\n\n")
    tools.cprint(flashCounter);

}

function flash(board, niners) {
    for (const nine of niners) {
        const split = nine.split(":");
        const y = Number(split[0]);
        const x = Number(split[1]);

        infect(y, x, board, niners);
    }
}

function infect(y, x, board, niners) {
    for (const [dy, dx] of tools.ADJ_DIRS_2) {
        let tmpY = y + dy;
        let tmpX = x + dx;;
        if (tmpY >= 0
            && tmpX >= 0
            && tmpY < board.length
            && tmpX < board[0].length

        ) {
            const grown = board[tmpY][tmpX] + 1;
            board[tmpY][tmpX] = grown;
            if (grown > 9 && !niners.includes(tools.bindArray([tmpY, tmpX]))) {
                niners.push(tools.bindArray([tmpY, tmpX]))
            }
        }
    }
}

function grow(board, niners) {
    for (let y = 0; y < board.length; y++) {
        for (let x = 0; x < board[0].length; x++) {
            const grown = board[y][x] + 1;
            board[y][x] = grown;
            if (grown > 9) {
                niners.push(tools.bindArray([y, x]))
            }
        }
    }
}

function restoration(board) {
    let counter = 0;
    for (let y = 0; y < board.length; y++) {
        for (let x = 0; x < board[0].length; x++) {
            const current = board[y][x];

            if (current > 9) {
                board[y][x] = 0;
                counter++;
            }
        }
    }
    return counter;
}

function allLight(board) {
    let total = 0
    for (const row of board) {
        total += row.filter(x => x == 0).length;
    }

    return 100 == total;
}

main();