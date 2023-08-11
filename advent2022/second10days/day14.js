import * as tools from '../tools.js';

const ROCK = "#";
const AIR = ".";
const DUST = "o";
const VERTICAL_PADDING = 15;
const HORIZONTAL_PADDING = 20;
// const HORIZONTAL_PADDING = 2000;

function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d14_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const bluePrint = createBluePrint(lines);
    const bases = findBases(bluePrint);
    tools.cprint(bases);

    const board = terraform(bluePrint, bases);

    // tools.cprint(rows)

    const holePositionX = 500 - bases[0] + bases[4];
    const holePositionY = VERTICAL_PADDING - bases[2];
    const roof = Array(bases[1] - bases[0] + 1 + 2 * bases[4]).fill("~");

    fillEmUp(board, holePositionX, holePositionY);

    let dustCounter = 0;
    board.forEach(y => y.forEach(x => {
        if (x == DUST) dustCounter++;
    }))

    board[holePositionY][holePositionX] = "S";
    board.unshift(roof);
    tools.printBoard(board)

    // tools.printJson(bluePrint)
    tools.cprint(dustCounter);

}


function fillEmUp(board, holePositionX, holePositionY) {
    let isFilled = false;
    let limiter = 35000;
    while (!isFilled && limiter > 0) {
        isFilled = simulateSandDrop(board, holePositionX, holePositionY);
        limiter--;
    }
}


function simulateSandDrop(board, holePositionX, holePositionY) {
    let x = holePositionX;
    let y = holePositionY;
    let stay = false;
    while (!stay) {
        if (board[y + 1][x] == AIR) {
            y++;
        } else if (x > 1 && board[y + 1][x - 1] == AIR) {
            y++;
            x--;
        } else if (x < board[0].length - 1 && board[y + 1][x + 1] == AIR) {
            y++;
            x++;
        } else {
            board[y][x] = DUST;
            stay = true;
        }
        if (y == board.length - 2 || (x == holePositionX && y == holePositionY)) {
            return true;
        }

    }
    return false;

}

function terraform(bluePrint, bases) {
    const board = [];
    const rows = Array(bases[1] - bases[0] + 1 + 2 * bases[4]).fill(AIR);
    const columns = bases[3] - bases[2] + 1 + 2 * bases[5];


    Array.from(Array(columns)).forEach(() => {
        board.push(rows.slice());
    })

    // let floorLevel = bases[3] - bases[2] + 2 + bases[5];
    // console.log(floorLevel);
    // board[floorLevel] = board[floorLevel].map(x => ROCK);

    // bluePrint.push([[0, bases[3] + 2], [board[0].length - 1, bases[3] + 2]]);

    bluePrint.forEach(x => construct(board, x, bases));
    return board
}

function construct(board, instruction, bases) {
    for (let i = 0; i < instruction.length - 1; i++) {
        const current = instruction[i];
        const next = instruction[i + 1];
        const isVertical = current[0] == next[0];
        let start = isVertical ? current[1] - bases[2] + bases[5] : current[0] - bases[0] + bases[4];
        let stop = isVertical ? next[1] - bases[2] + bases[5] : next[0] - bases[0] + bases[4];
        if (start > stop) {
            const tmp = start;
            start = stop;
            stop = tmp;
        }
        const commonAxis = isVertical ? current[0] - bases[0] + bases[4] : current[1] - bases[2] + bases[5];
        buildLine(board, start, stop, commonAxis, isVertical);
    }
}

function buildLine(board, start, stop, commonAxis, isVertical) {
    for (let i = start; i <= stop; i++) {
        if (isVertical) {
            board[i][commonAxis] = ROCK;
        } else {
            board[commonAxis][i] = ROCK;
        }
    }

}

function findBases(bluePrint) {
    let xMin, xMax, yMin, yMax;

    bluePrint.forEach(a => a.forEach(
        task => {
            const x = task[0];
            const y = task[1];
            xMin ??= x;
            xMax ??= x;
            yMin ??= y;
            yMax ??= y;

            xMin = Math.min(xMin, x);
            xMax = Math.max(xMax, x);
            yMin = Math.min(yMin, y);
            yMax = Math.max(yMax, y);
        }));

    return [xMin, xMax, yMin, yMax, HORIZONTAL_PADDING, VERTICAL_PADDING];
}

function createBluePrint(lines) {
    const bluePrint = [];
    let splitted
    let splitGroup
    lines.forEach(line => {
        splitGroup = [];

        line.split(" -> ").forEach(x => {
            splitted = x.split(",").map(x => Number(x));
            splitGroup.push(splitted);

        })
        bluePrint.push(splitGroup);
    });

    return bluePrint;
}

main();