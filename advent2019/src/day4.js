import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;
const testFile = `${baseDir}\\data\\test.txt`;

function part1(input) {
    let answer;
    console.log(`Part 1: ${answer}`)
    const finalAnswer = 1
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function part2(input) {
    let answer;
    console.log(`Part 2: ${answer}`)
    const finalAnswer = undefined
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function main() {
    let inputFile = `${dataDir}\\d4_input.txt`;
    inputFile = testFile;

    console.log("Input File: " + inputFile);
    const input = tools.readFileFromLocal(inputFile).split(/\r?\n/);

    part1(input);
    part2(input);
}

main();