import * as tools from '../../js-util/tools.js';

const YEAR = 2025;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

function part1(config) {
    let answer = 0;
    const correctAnswer = 12599655151

    for (let item of config.data) {
        let start = parseInt(item[0]);
        let end = parseInt(item[1]);

        for (let i = start; i <= end; i++) {
            answer += isInvalidPart1(i.toString());
        }
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 20942028255

    for (let item of config.data) {
        let start = parseInt(item[0]);
        let end = parseInt(item[1]);

        for (let i = start; i <= end; i++) {
            answer += isInvalidPart2(i.toString());
        }
    }

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function isInvalidPart1(input) {
    if (input.length % 2 == 1)
        return 0

    let mid = input.length / 2;

    let midstr = input.substring(0, mid);
    if (input === midstr + midstr) {
        return parseInt(input);
    }

    return 0
}


function isInvalidPart2(input) {
    const inputLength = input.length;
    let repeats = [1, 2, 3, 4, 5];

    for (let repeat of repeats) {
        if (Math.trunc(inputLength / repeat) !== inputLength / repeat) continue

        let mult = Math.trunc(inputLength / repeat);
        if (mult == 1) continue;
        let segment = input.substring(0, repeat);
        if (segment.repeat(mult) === input)
            return parseInt(input);

    }
    return 0
}

function main() {
    let inputFile = `${dataDir}\\d2_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines,
        data: []
    }

    for (let data of config.raw[0].split(',')) {
        let split = data.split('-');
        config.data.push([parseInt(split[0]), parseInt(split[1])]);
    }


    part1({ ...config });
    part2({ ...config });
}

main();

