import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;
const MARKED = "*";

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d4_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const content = tools.readFileFromLocal(fileName).replaceAll("\r", "");

    const segments = content.split(/\n\n/);
    if (segments[segments.length - 1].length == 0) segments.pop();

    const bingoNumbers = segments.shift().split(",");
    const boards = [];

    for (const segment of segments) {
        let tmpArray = segment.replaceAll("\n", " ").replaceAll("  ", " ").split(" ");
        tmpArray = tmpArray.filter(x => x.length > 0);
        boards.push(tmpArray);
    }


    tools.cprint(bingoNumbers);
    tools.cprint(boards);
    const finalNumber = processBoard(bingoNumbers, boards);
    tools.cprint(finalNumber);
}

function processBoard(bingoNumbers, boards) {

    const winners = new Set();

    for (const number of bingoNumbers) {
        for (let i = 0; i < boards.length; i++) {
            const board = boards[i];
            if (number == 24) {
                let debug = 1;
            }
            const index = board.indexOf(number);
            if (index >= 0) {
                board[index] = MARKED;
                if (checkWin(board, index)) {

                    winners.add(i);

                    if (winners.size == boards.length) {
                        let theRest = board.filter(x => x != MARKED);
                        theRest = theRest.map(x => Number(x));
                        let total = theRest.reduce(
                            (accumulator, currentValue) => accumulator + currentValue,
                            0
                        );

                        return total * Number(number);
                    }
                }
            }

        }
    }
}


function checkWin(board, index) {
    const column = index % 5;
    const row = Math.floor(index / 5);

    const verticalWin = board.filter((v, k) => k % 5 == column).every(x => x == MARKED);
    const horizontalWin = board.filter((v, k) => k >= row * 5 && k < (row + 1) * 5).every(x => x == MARKED);

    if (horizontalWin || verticalWin) {
        let debug = 1;
    }

    return horizontalWin || verticalWin;
}

main();