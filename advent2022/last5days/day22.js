import * as tools from '../tools.js';

const R = 0;
const D = 1;
const L = 2;
const U = 3;

const DOT = ".";

const HASH = "#";
const SPACE = " ";

const PART = 2;

let fileName;
function main() {

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d22_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    const rawInput = tools.readFileFromLocal(fileName);
    let tmpSplit = fileName.includes("test") ?
        tools.readFileFromLocal(fileName).split(/\n\r?\r\n/)
        : tools.readFileFromLocal(fileName).split(/\n\n/);

    const rawBoard = tmpSplit[0];
    const rawInstructions = tmpSplit[1];

    const lines = fileName.includes("test") ? rawBoard.split(/\n?\r/) : rawBoard.split(/\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    for (let i = 0; i < lines.length; i++) {
        lines[i] = lines[i].replaceAll("\n", "");
        lines[i] = lines[i].split("");
    }
    // lines.forEach(x => x = x.split(""));

    if (fileName.includes("test")) tools.printBoard(lines);

    const regexpCoordinates = /\d+|L|R/g;
    let movements = rawInstructions.match(regexpCoordinates);

    run(lines, movements);

    // 130120 wrong too high 
}

class Cursor {
    constructor(xCoord) {
        this.x = xCoord;
        this.y = 0;
        this.direction = R;
    }

    get value() {
        return 1000 * (this.y + 1)
            + 4 * (this.x + 1)
            + this.direction;

    }

    move(movement, board) {
        if (movement == "L" || movement == "R") {
            if (movement == "R") {
                this.direction = (this.direction + 1) % 4;
            } else {
                this.direction = this.direction == R ? U : this.direction - 1;
            }

            return;
        }

        movement = Number(movement);
        let predictMove;
        switch (this.direction) {
            case U:
                predictMove = this.nextUpCoordinates;
                break;
            case R:
                predictMove = this.nextRightCoordinates;
                break;
            case L:
                predictMove = this.nextLeftCoordinates;
                break;
            case D:
                predictMove = this.nextDownCoordinates;
                break;
        }

        // tools.cprint(movement);
        // if (movement == 43) {
        //     let debug = 1;
        // }

        for (let i = 1; i <= movement; i++) {
            const next = predictMove(this.y, this.x, board);
            let nextStep = board[next[0]][next[1]];
            if (nextStep == DOT) {
                this.y = next[0];
                this.x = next[1];
            } else {
                // this is hash .. do nothing 
                break;
            }
        }
    }

    nextRightCoordinates(y, x, board) {
        if (x == board[y].length - 1 || board[y][x + 1] == SPACE || board[y][x + 1] == undefined) {
            for (let i = 0; i < board[y].length; i++) {
                if (board[y][i] == DOT || board[y][i] == HASH) {
                    return [y, i];
                }
            }
        } else {
            return [y, x + 1];
        }
    }

    nextLeftCoordinates(y, x, board) {
        let nextPiece = board[y][x - 1];
        if (x == 0 || !(nextPiece == DOT || nextPiece == HASH)) {
            return [y, board[y].length - 1];
        } else {
            return [y, x - 1];
        }
    }

    nextUpCoordinates(y, x, board) {
        if (y == 0 || board[y - 1][x] == SPACE || board[y - 1][x] == undefined) {
            for (let i = board.length - 1; i > 0; i--) {
                if (board[i][x] == DOT || board[i][x] == HASH) {
                    return [i, x];
                }
            }
        } else {
            return [y - 1, x];
        }
    }

    nextDownCoordinates(y, x, board) {
        if (y == board.length - 1 || board[y + 1][x] == SPACE || board[y + 1][x] == undefined) {
            for (let i = 0; i < board.length; i++) {
                if (board[i][x] == DOT || board[i][x] == HASH) {
                    return [i, x];
                }
            }
        } else {
            return [y + 1, x];
        }
    }
}


function run(board, movements) {
    let xCoord;
    for (let i = 0; i < board[0].length; i++) {
        if (board[0][i] == DOT || board[0][i] == HASH) {
            xCoord = i - 1;
            break;
        }
    }

    const cursor = new Cursor(xCoord);

    for (const movement of movements) {
        cursor.move(movement, board);
    }

    let debug = 0;
    tools.cprint(cursor.value);
}




main();