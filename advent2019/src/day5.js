import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}/advent${YEAR}`;
const dataDir = `${baseDir}/data`;
const testFile = `${baseDir}/data/test.txt`;

const STATE_ADD = 1
const STATE_MULT = 2
const STATE_INPUT = 3
const STATE_OUTPUT = 4

const STATE_END = 99

const PARAM_ADDR = 0
const PARAM_VALUE = 1



function part1(intProgram) {
    let answer;
    let input = 1;

    answer = runIntcode(input, intProgram)

    console.log(`Part 1: ${answer}`)
    const finalAnswer = 11933517
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);


}

function part2(input) {
    let answer;

    const expectedOutput = 19690720


    console.log(`Part 2: ${answer}`)

    const finalAnswer = 8298
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function runIntcode(input, intProgram) {
    let output = null
    for (let index = 0; index < intProgram.length; index) {
        const opcode = intProgram[index]

        const instruction = opcode % 100
        let paramValue_1
        switch (instruction) {
            case STATE_END:
                return output
            case STATE_INPUT:
                paramValue_1 = intProgram[index + 1]

                intProgram[paramValue_1] = input
                index += 2
                break
            case STATE_OUTPUT:
                paramValue_1 = intProgram[index + 1]

                output = intProgram[paramValue_1]


                index += 2
                break
            case STATE_ADD:
            case STATE_MULT:
                let isRaw = getPositionValue(opcode - instruction, 3) === PARAM_VALUE
                paramValue_1 = isRaw ? intProgram[index + 1] : intProgram[intProgram[index + 1]]
                if (opcode == 1101) {
                    let debug = 1
                }

                isRaw = getPositionValue(opcode - instruction, 4) === PARAM_VALUE
                const paramValue_2 = isRaw ? intProgram[index + 2] : intProgram[intProgram[index + 2]]
                const dest = intProgram[index + 3]
                intProgram[dest] = eval((paramValue_1 + (instruction === STATE_ADD ? "+" : "*") + paramValue_2))
                index += 4
                break
        }

       
    }

    return output
}

function getPositionValue(number, position) {
    return Math.floor(number / Math.pow(10, position - 1)) % 10;
}

function main() {
    let inputFile = `${dataDir}\\d5_input.txt`;
    // inputFile = testFile;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const input = lines[0].split(",").map(Number)
    part1(input.slice());
    part2(input.slice());
}

main();