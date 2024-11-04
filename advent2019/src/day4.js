import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;
const testFile = `${baseDir}\\data\\test.txt`;

const lowerLimit = 234208
const upperLimit = 765869


function part1(input) {
    let answer = 0;


    for (let i = lowerLimit; i <= upperLimit; i++) {
        if (isGoodPassword(i)) answer++
    }

    console.log(`Part 1: ${answer}`)
    const finalAnswer = 1246
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function part2(input) {
    let answer = 0;

    for (let i = lowerLimit; i <= upperLimit; i++) {
        if (isGoodPassword(i, true)) answer++
    }

    console.log(`Part 2: ${answer}`)
    const finalAnswer = 814
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

function isGoodPassword(input, isPartTwo = false) {
    const inputStr = String(input)
    const uniqueNumber = (new Set(inputStr.split(''))).size
    if (uniqueNumber === 6) return false


    for (let i = 0; i < inputStr.length - 1; i++) {
        const current = Number(inputStr[i])
        const next = Number(inputStr[i + 1])
        if (current > next) return false
    }


    if (isPartTwo) {

        const occurrences = inputStr.split('').reduce(function (acc, curr) {
            return acc[curr] ? ++acc[curr] : acc[curr] = 1, acc
        }, {});


        const hasTwoORFour = Object.values(occurrences).some(x => Number(x) === 2)

        if (!hasTwoORFour) return false

        // for (const key of Object.keys(occurrences)) {
        //     const occurence = Number(occurrences[key])
        //     if (occurence % 2 !== 0 && occurence !== 1) {
        //         let debug = 1
        //         return false
        //     }
        // }

    }


    return true
}



main();