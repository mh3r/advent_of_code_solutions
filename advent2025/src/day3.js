import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function getMaxBattery(input, targetLength) {
    let tmpInput = input
    let retval = ''
    for (let i = 0; i < targetLength; i++) {
        const matrix = getMaxMatrix(tmpInput, targetLength - i)
        tmpInput = tmpInput.slice(matrix[1] + 1)
        retval += matrix[0]
    }
    return parseInt(retval)
}

function getMaxMatrix(input, expectedLeftOverLength) {
    const length = input.length
    const splitted = input.split('').map(e => parseInt(e))
    let max = Math.max(...splitted)
    let index = splitted.indexOf(max)

    const exclusionList = []
    while (index + expectedLeftOverLength > length) {
        exclusionList.push(max)
        max = Math.max(...splitted.filter(x => !exclusionList.includes(x)))
        index = splitted.indexOf(max)
    }

    return [max.toString(), index]
}

function part1(config) {
    let answer = 0;
    const correctAnswer = 17346
    const targetLength = 2
    for (let line of config.raw) {
        answer += getMaxBattery(line, targetLength)
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 172981362045136
    const targetLength = 12

    for (let line of config.raw) {
        answer += getMaxBattery(line, targetLength)
    }

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;
    let inputFile = `${dataDir}\\d3_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

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