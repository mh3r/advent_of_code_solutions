import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;
const testFile = `${baseDir}\\data\\test.txt`;

function part1(input) {
    let answer;
    console.log(`Part 1: ${answer}`)
}

function part2(input) {
    let answer;
    console.log(`Part 2: ${answer}`)
}

function main() {
    let inputFile = `${dataDir}\\d1_input.txt`;
    inputFile = testFile;

    console.log("Input File: " + inputFile);
    const input = tools.readFileFromLocal(inputFile).split(/\r?\n/);

    part1(input);
    part2(input);
}

main();