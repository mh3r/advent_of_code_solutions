import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}/advent${YEAR}`;
const dataDir = `${baseDir}/data`;
const testFile = `${baseDir}/data/test.txt`;

const STATE_ADD = 1
const STATE_MULT = 2
const STATE_INPUT = 3
const STATE_OUTPUT = 4
const PARAM_ADDR = 0
const PARAM_VALUE = 1

const END_STATE = 99


function part1(intProgram) {
    let answer;
    let input = 1;

    answer = runIntcode(input, intProgram, 12, 2)


    console.log(`Part 1: ${answer}`)
    const finalAnswer = 3562624
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);


}

function part2(input) {
    let answer;

    const expectedOutput = 19690720

 
    console.log(`Part 2: ${answer}`)

    const finalAnswer = 8298
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function runIntcode(input, intProgram, noun, verb) {
    input = input
    output = 0

    intProgram[1] = noun
    intProgram[2] = verb

    for (let i = 0; i < intProgram.length; i += 4) {
        const opcode = intProgram[i]
        const addr1 = intProgram[i + 1]
        const addr2 = intProgram[i + 2]
        const dest = intProgram[i + 3]

        if (END_STATE === opcode) return intProgram[0]

        intProgram[dest] = eval((intProgram[addr1] + (opcode === STATE_ADD ? "+" : "*") + intProgram[addr2]))
    }

    return intProgram[0]
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