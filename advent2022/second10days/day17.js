import * as tools from '../tools.js';

let fileName;
const X = "x";
const O = ".";
// const DROP = 1;
// const RIGHT = 2;
// const LEFT = 3;
const SETTLED = "@";
const THREE = 3;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d17_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const directions = []
    const blocks = [];

    lines.forEach(line => {
        for (const char of line) {
            if (char == ">") directions.push(true);
            if (char == "<") directions.push(false);
        }
    });

    // tools.cprint(directions);
    init(blocks);
    // tools.cprint(blocks);

    start(directions, blocks);


    // 3127 too low 
    // 3147 is correct 
}

function init(blocks) {
    const block1 = [];
    block1[0] = [O, X, X, X, X];

    const block2 = [];
    block2[0] = [O, O, O, X];
    block2[1] = [O, O, X, X, X];
    block2[2] = [O, O, O, X];

    const block3 = [];
    block3[0] = [O, O, X, X, X, O, O];
    block3[1] = [O, O, X, O, O, O, O];
    block3[2] = [O, O, X, O, O, O, O];

    const block4 = [];
    block4[0] = [O, O, O, O, X];
    block4[1] = [O, O, O, O, X];
    block4[2] = [O, O, O, O, X];
    block4[3] = [O, O, O, O, X];

    const block5 = [];
    block5[0] = [O, O, O, X, X];
    block5[1] = [O, O, O, X, X];

    blocks.push(block1);
    blocks.push(block2);
    blocks.push(block3);
    blocks.push(block4);
    blocks.push(block5);
}


function start(directions, blocks) {
    const board = [];


    // const rep = 1000000000000;
    const rep = 2022;
    // let j = 0;

    const subDirections = directions.slice();

    for (let j = 0; j <  rep; j++) {
        let maxHeight = conjureBlock(board, blocks[j % 5]);
        move(board, maxHeight + THREE, directions, subDirections);
    }

    tools.cprint(maxHeight(board));

    if (board.length < 100) {
        tools.cprint("=======");
        board.reverse();
        tools.printBoard(board);
    }

}

function conjureBlock(board, block) {
    const yRef = maxHeight(board);
    if (board.length == 0) {
        board.push(Array.from(Array(7)).fill("."));
    }
    // tools.cprint(yRef);

    for (let i = yRef; i < yRef + THREE; i++) {
        if (board[i] == null) board[i] = [];
    }

    let counter = THREE;
    block.forEach(x => {
        board[yRef + counter] = x.slice();
        counter++;
    });
    return yRef;
}

function maxHeight(board) {
    let retval = 0;
    for (let height = board.length - 1; height >= 0; height--) {
        if (board[height].includes(SETTLED)) {
            retval = height + 1;
            break;
        }
    }
    return retval;
}


function move(board, yRef, directions, subDirections) {
    let isSettled = false;
    let blockCoordinates = findBlockCoordinates(board, yRef);

    const canMoveLeft = ([y, x]) => {
        return x > 0 && board[y][x - 1] != SETTLED;
    }
    const canMoveRight = ([y, x]) => {
        return x < (board[0].length - 1) && board[y][x + 1] != SETTLED;
    }

    const canMoveDown = ([y, x]) => {
        return y > 0 && board[y - 1][x] != SETTLED;
    }

    while (!isSettled) {
        const tmpWind = subDirections.shift();
        if (subDirections.length == 0) {
            subDirections.push(...directions.slice());
        }
        if (tmpWind && blockCoordinates.every(canMoveLeft)) {
            blockCoordinates.forEach(([y, x]) => {
                board[y][x] = ".";
                board[y][x - 1] = X;
            })
            blockCoordinates = blockCoordinates.map(([y, x]) => [y, x - 1]);
        }
        if (!tmpWind && blockCoordinates.every(canMoveRight)) {
            blockCoordinates.forEach(([y, x]) => {
                board[y][x] = ".";
                board[y][x + 1] = X;
            })
            blockCoordinates = blockCoordinates.map(([y, x]) => [y, x + 1]);
        }

        if (blockCoordinates.every(canMoveDown)) {
            blockCoordinates.forEach(([y, x]) => {
                board[y][x] = ".";
                board[y - 1][x] = X;
            })
            blockCoordinates = blockCoordinates.map(([y, x]) => [y - 1, x]);
        } else {
            blockCoordinates.forEach(([y, x]) => {
                board[y][x] = SETTLED;
            })
            isSettled = true;
        }

    }

}

function findBlockCoordinates(board, yRef) {
    const blockCoordinates = []
    for (let y = yRef; y < board.length; y++) {
        for (let x = 0; x < board[0].length; x++) {
            if (board[y][x] == X) {
                blockCoordinates.push([y, x]);
            }
        }
    }
    return blockCoordinates;
}

main();