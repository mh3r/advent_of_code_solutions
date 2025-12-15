import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = 749
    const parsedPath = { [`${FINISH}`]: 1 }

    while (Object.keys(parsedPath).includes(START) === false) {
        // potentially can optimise if we sort this by length of values
        const unparsedKeys = Object.keys(config.paths).filter(x => Object.keys(parsedPath).includes(x) === false);
        for (const key of unparsedKeys) {
            const values = config.paths[key];
            const canResolve = values.every(x => Object.keys(parsedPath).includes(x));
            let total = 0
            if (canResolve) {
                for (const v of values) {
                    total += parsedPath[v];
                }
                parsedPath[key] = total;
            }
        }
    }
    answer = parsedPath[START];
    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    // tried to list out all possible paths 
    // got memory issues trying when parsing input

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d11_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const spaghetti = {}

    for (const line of lines) {
        const splitted = line.split(':');
        const key = splitted[0].trim();
        const value = splitted[1].trim();
        spaghetti[key] = value.split(" ");
    }

    config.paths = spaghetti

    part1({ ...config });
    part2({ ...config });
}

const START = 'you'
const FINISH = 'out'
const SERVER = 'svr'
const DAC = 'dac'
const FFT = 'fft'

main();