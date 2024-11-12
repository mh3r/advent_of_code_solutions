import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

function part1(lines) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(lines) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    let inputFile = `${dataDir}\\d7_input.txt`;
    inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    part1(lines);
    part2(lines);
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

        // for (const permutation of currentPermutation) {
        //     retval.push([...permutation, ...rest.slice(i + 1)])
        // }


    }
    return retval = [...currentPermutation]

}


console.log(generatePermutations([1, 2, 3, 4]))



function generatePermutations2(arr) {
    let results = [];

    function permute2(index) {
        if (index === arr.length) {
            results.push([...arr]); // Copy current permutation
            return;
        }

        for (let i = index; i < arr.length; i++) {
            [arr[index], arr[i]] = [arr[i], arr[index]]; // Swap
            permute2(index + 1);
            [arr[index], arr[i]] = [arr[i], arr[index]]; // Backtrack (swap back)
        }
    }

    permute2(0);
    return results;
}

let arr = [1, 2, 3];
console.log(generatePermutations2(arr));


main();