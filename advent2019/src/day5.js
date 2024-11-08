import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}/advent${YEAR}`;
const dataDir = `${baseDir}/data`;
const testFile = `${baseDir}/data/test.txt`;

const STATE_ADD = 1
const STATE_MULT = 2
const STATE_INPUT = 3
const STATE_OUTPUT = 4
const STATE_JIT = 5
const STATE_JIF = 6
const STATE_LESS_THAN = 7
const STATE_EQUAL = 8

const STATE_END = 99

const MODE_VALUE = 1

function part1(intProgram) {
    let answer;
    let input = 1;

    answer = runIntcode(input, intProgram)

    console.log(`Part 1: ${answer}`)
    const finalAnswer = 11933517
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);


}

function part2(intProgram) {
    let answer;

    const expectedOutput = 19690720

    let input = 5

    input = 5
    intProgram = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

    answer = runIntcode(input, intProgram)


    console.log(`Part 2: ${answer}`)

    const finalAnswer = 8298
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function runIntcode(input, intProgram) {
    let output = null
    for (let index = 0; index < intProgram.length;) {
        const opcode = intProgram[index]

        const instruction = opcode % 100
        let paramValue_1
        let paramValue_2
        let paramValue_3
        switch (instruction) {
            case STATE_END:
                return output
            case STATE_ADD:
            case STATE_MULT:
                paramValue_1 = getParameterValue(opcode, instruction, intProgram, index)
                paramValue_2 = getParameterValue(opcode, instruction, intProgram, index, 1)
                paramValue_3 = intProgram [index + 3]
                intProgram[paramValue_3] = eval((paramValue_1 + (instruction === STATE_ADD ? "+" : "*") + paramValue_2))
                index += 4
                break
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
            case STATE_JIT:
                paramValue_1 = getParameterValue(opcode, instruction, intProgram, index)
                if (paramValue_1 !== 0) {
                    paramValue_2 = getParameterValue(opcode, instruction, intProgram, index, 1)
                    index = paramValue_2
                } else {
                    index += 3
                }

                break
            case STATE_JIF:
                paramValue_1 = getParameterValue(opcode, instruction, intProgram, index)
                if (paramValue_1 === 0) {
                    paramValue_2 = getParameterValue(opcode, instruction, intProgram, index, 1)
                    index = paramValue_2
                } else {
                    index += 3
                }
                break
            case STATE_LESS_THAN:
                paramValue_1 = getParameterValue(opcode, instruction, intProgram, index)
                paramValue_2 = getParameterValue(opcode, instruction, intProgram, index, 1)
                paramValue_3 = intProgram [index + 3]
                const lessThanValue = paramValue_1 < paramValue_2 ? 1 : 0
                intProgram[paramValue_3] = lessThanValue
                index += 4
                break
            case STATE_EQUAL:
                paramValue_1 = getParameterValue(opcode, instruction, intProgram, index)
                paramValue_2 = getParameterValue(opcode, instruction, intProgram, index, 1)
                paramValue_3 = intProgram [index + 3]
                const equalValue = paramValue_1 === paramValue_2 ? 1 : 0
                intProgram[paramValue_3] = equalValue
                index += 4
                break
        }
    }

    return output
}

function getParameterValue(opcode, instruction, intProgram, index, offset = 0) {   
    const isRaw = getPositionValue(opcode - instruction, 3 + offset) === MODE_VALUE
    const retval = isRaw ? intProgram[index + 1 + offset] : intProgram[intProgram[index + 1 + offset]]
    return retval
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