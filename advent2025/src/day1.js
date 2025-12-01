import * as tools from '../../js-util/tools.js';

const YEAR = 2025;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

function part1(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    let inputFile = `${dataDir}\\d1_input.txt`;
    inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    part1({ ...config });
    part2({ ...config });
}

main();