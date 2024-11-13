import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

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
    let answer = 0;
    const correctAnswer = 17790

    const seqInput = [0, 1, 2, 3, 4]
    const ampSeqs = generatePermutations(seqInput)



    const outputs = []




    for (const thrusterSequence of ampSeqs) {
        let input2 = 0
        for (const input1 of thrusterSequence) {
            input2 = runIntcode(input1, input2, intProgram)
        }
        outputs.push(input2)
    }

    // js sort is crap ... it sorts alphabetically
    outputs.sort(function (a, b) {
        return b - a;
    });

    answer = outputs[0]


    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(lines) {
    let answer = 0;
    const correctAnswer = undefined

    const seqInput = [5, 6, 7, 8, 9]
    const ampSeqs = generatePermutations(seqInput)



    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}


function runIntcode(input1, input2, intProgram) {
    let output = null
    let isFirstInput = true
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
                paramValue_3 = intProgram[index + 3]
                intProgram[paramValue_3] = eval((paramValue_1 + (instruction === STATE_ADD ? "+" : "*") + paramValue_2))
                index += 4
                break
            case STATE_INPUT:
                let input = isFirstInput ? input1 : input2
                paramValue_1 = intProgram[index + 1]
                intProgram[paramValue_1] = input
                index += 2
                isFirstInput = false
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
                paramValue_3 = intProgram[index + 3]
                const lessThanValue = paramValue_1 < paramValue_2 ? 1 : 0
                intProgram[paramValue_3] = lessThanValue
                index += 4
                break
            case STATE_EQUAL:
                paramValue_1 = getParameterValue(opcode, instruction, intProgram, index)
                paramValue_2 = getParameterValue(opcode, instruction, intProgram, index, 1)
                paramValue_3 = intProgram[index + 3]
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


function swapElement(input, a, b) {
    const retval = input.slice();
    retval[input.indexOf(a)] = b
    retval[input.indexOf(b)] = a
    return retval
}


function permute(twoDArray, element) {
    let retval = []
    for (const array of twoDArray) {
        retval.push([...array, element])
    }
    const retvalCopy = retval.slice()

    for (const x of twoDArray[0]) {
        for (const array of retvalCopy) {
            retval.push(swapElement(array, x, element))
        }
    }
    return retval
}


function generatePermutations(input) {

    let retval = []

    const rest = input.slice(1)

    let currentPermutation = [[input[0]]]
    for (let i = 0; i < rest.length; i++) {
        currentPermutation = permute(currentPermutation, rest[i])
    }
    return retval = [...currentPermutation]

}


function main() {
    let inputFile = `${dataDir}\\d7_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const input = lines[0].split(",").map(Number)


    part1(input.slice());
    part2(input.slice());
}


// console.log(generatePermutations([1, 2, 3, 4]))


// taken from chatgpt

// function generatePermutations2(arr) {
//     let results = [];

//     function permute2(index) {
//         if (index === arr.length) {
//             results.push([...arr]); // Copy current permutation
//             return;
//         }

//         for (let i = index; i < arr.length; i++) {
//             [arr[index], arr[i]] = [arr[i], arr[index]]; // Swap
//             permute2(index + 1);
//             [arr[index], arr[i]] = [arr[i], arr[index]]; // Backtrack (swap back)
//         }
//     }

//     permute2(0);
//     return results;
// }

// let arr = [1, 2, 3];
// console.log(generatePermutations2(arr));


main();