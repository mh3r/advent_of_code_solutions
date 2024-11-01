import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;
const testFile = `${baseDir}\\data\\test.txt`;

function part1(input) {
    let answer = 0;
    input.forEach(x => answer += massCalculation(x));
    console.log(`Part 1: ${answer}`)
    const finalAnswer = 3423511
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function part2(input) {
    let answer = 0;
    input.forEach(x => answer += massCalculation(x, true));
    console.log(`Part 2: ${answer}`)
    const finalAnswer = 5132379
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function massCalculation(input, isFuelception = false) {
    let retval = Math.floor(input / 3) - 2

    if (isFuelception) {
        let tmpAnswer = retval
        while (true) {
            tmpAnswer = massCalculation(tmpAnswer)
            if (tmpAnswer <= 0) {
                break
            }
            retval += tmpAnswer
        }
    }
    return retval
}

function main() {
    let inputFile = `${dataDir}\\d1_input.txt`;
    // inputFile = testFile;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    part1(lines);
    part2(lines);
}

main();