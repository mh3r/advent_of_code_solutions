import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}/advent${YEAR}`;
const dataDir = `${baseDir}/data`;
const testFile = `${baseDir}/data/test.txt`;

const STATE_ADD = 1
const STATE_MULT = 2
const STATE_INPUT = 3
const STATE_OUTPUT = 4

const END_STATE = 99


function part1(input) {
    let answer;


    answer = runIntcode(input, 12, 2)


    console.log(`Part 1: ${answer}`)
    const finalAnswer = 3562624
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);


}

function part2(input) {
    let answer;

    const expectedOutput = 19690720

    loop1:
    for (let noun = 99; noun >= 0; noun--) {
        for (let verb = 99; verb >= 0; verb--) {

            const output = runIntcode(input.slice(), noun, verb)
            console.log(output)
            if (expectedOutput === output) {
                answer = 100 * noun + verb
                break loop1
            }
        }
    }
    console.log(`Part 2: ${answer}`)

    const finalAnswer = 8298
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function runIntcode(input, noun, verb) {
    input[1] = noun
    input[2] = verb

    for (let i = 0; i < input.length; i += 4) {
        const opcode = input[i]
        const addr1 = input[i + 1]
        const addr2 = input[i + 2]
        const dest = input[i + 3]

        if (END_STATE === opcode) return input[0]

        input[dest] = eval((input[addr1] + (opcode === STATE_ADD ? "+" : "*") + input[addr2]))
    }

    return input[0]
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