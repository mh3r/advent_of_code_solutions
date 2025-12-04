import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = undefined


    for (let y = 0; y < config.grid.length; y++) {
        for (let x = 0; x < config.grid[0].length; x++) {
            if (config.grid[y][x] === ROLL) {
                if (isAccessible(config.grid, y, x)) {
                    answer += 1
                }
            }
        }

        console.log(`Part 1: ${answer}`)
        console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
    }

}

function isAccessible(grid, y, x) {
    let counter = 0;

    for (const [dy, dx] of tools.ADJ_DIRS_2) {
        let tmpY = y + dy;
        let tmpX = x + dx;
        if (tmpY >= 0
            && tmpX >= 0
            && tmpY < grid.length
            && tmpX < grid[0].length
        ) {
            if (grid[tmpY][tmpX] === ROLL) {
                counter++;
            }
        }
    }
    return counter < 4
}


function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    let previousAnswer = 0
    const toBeDeleted = [];

    while (previousAnswer == 0 || answer != previousAnswer) {

        previousAnswer = answer

        for (const [dy, dx] of toBeDeleted) {
            config.grid[dy][dx] = EMPTY
        }

        toBeDeleted.length = 0;

        for (let y = 0; y < config.grid.length; y++) {
            for (let x = 0; x < config.grid[0].length; x++) {
                if (config.grid[y][x] === ROLL && isAccessible(config.grid, y, x) ) {
                    answer += 1;
                    toBeDeleted.push([y, x]);
                }
            }
        }
    }


    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d4_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const grid = []
    for (const line of config.raw) {
        const row = line.split('')
        grid.push(row);
    }
    config.grid = grid;


    // part1({ ...config });
    part2({ ...config });
}


const EMPTY = '.'
const ROLL = '@'
main()
