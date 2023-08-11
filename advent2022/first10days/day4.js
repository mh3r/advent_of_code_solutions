import * as tools from '../tools.js';

function main() {
    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d4_input.txt";

    let redundantCounter = 0;
    let overlapCounter = 0;
    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        redundantCounter += isRedundant(line);
        overlapCounter += hasOverlap(line);
    });

    console.log(redundantCounter);
    console.log(overlapCounter);
}

function isRedundant(input) {
    const array = input.replaceAll(",", "-").split("-").map(x => Number(x));

    const result = ((array[0] <= array[2]) && (array[1] >= array[3]))
        || ((array[0] >= array[2]) && (array[1] <= array[3]));

    // console.log(input + "   \t" + result);
    return result ? 1 : 0;
}

function hasOverlap(input) {
    const array = input.replaceAll(",", "-").split("-").map(x => Number(x));

    const result = (array[1] < array[2])
        || (array[0] > array[3]);

    // console.log(input + "   \t" + result);
    return result ? 0 : 1;
}

main();