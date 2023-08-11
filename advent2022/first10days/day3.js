import * as tools from '../tools.js';

const alphabet = ['0'
    , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

function main() {
    let array = [];
    const subArray = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d3_input.txt";

    let counter = 1;
    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        subArray.push(line);

        if (counter % 3 == 0) {
            array.push(subArray.slice());
            subArray.length = 0;
        }
        counter++;
    });

    printJson(array);
    let rucksackCounter = 0;
    array.forEach(x => rucksackCounter += rucksacksSorter(x))
    console.log(rucksackCounter);
}

function printJson(data) {
    console.log(JSON.stringify(data, null, 2));
}

function findCommonCharacter(input) {
    const firstFragment = input.slice(0, input.length / 2);
    const secondFragment = input.slice(input.length / 2);

    for (let char of firstFragment) {
        if (secondFragment.includes(char))
            return char;
    }
}

function rucksacksSorter(data) {
    let commonChar;
    for (const char of data[0]) {
        if (data[1].includes(char) && data[2].includes(char)) {
            commonChar = char;
            break;
        }
    }
    console.log(commonChar);
    return alphabet.indexOf(commonChar);
}

main();