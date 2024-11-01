import * as tools from '../../js-util/tools.js';

const YEAR = the_year;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

function part1(lines) {
    let answer = 0;
    console.log(`Part 1: ${answer}`)
    const finalAnswer = undefined
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function part2(lines) {
    let answer = 0;
    console.log(`Part 2: ${answer}`)
    const finalAnswer = undefined
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function main() {
    let inputFile = `${dataDir}\\dx_input.txt`;
    inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    part1(lines);
    part2(lines);
}

main();