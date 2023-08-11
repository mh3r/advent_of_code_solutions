import * as tools from '../tools.js';

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d20_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 0;
    let lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const decriptionKey = 811589153;
    lines = lines.map(x => Number(x) * decriptionKey);


    // FOR 2 stars .. need to account for a premixed list index 
    let rep = 2;
    let newArray = lines;
    for (let i = 0; i < rep; i++) {
        newArray = mix(newArray);
    }

    let testData1 = [0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153];
    let testData2 = [0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153];

    if (fileName.includes("test") &&
        (JSON.stringify(testData1) == JSON.stringify(newArray)
            || JSON.stringify(testData2) == JSON.stringify(newArray))
    ) {
        tools.cprint("CORRECT RESULT  ... ");
    } else {
        tools.cprint("INCORRECT RESULT  ... :(");
    }

    tools.cprint(newArray);

    let zeroPos = newArray.indexOf(0);

    let totalSum = newArray[(zeroPos + 1000) % newArray.length]
        + newArray[(zeroPos + 2000) % newArray.length]
        + newArray[(zeroPos + 3000) % newArray.length];

    tools.cprint(totalSum);



}

function mix(lines) {
    lines = lines.slice();
    let dataPositionArray = Array.from(Array(lines.length).keys());
    tools.cprint(dataPositionArray);

    let printLimit = 10;
    for (let i = 0; i < dataPositionArray.length; i++) {
        move(i, lines[i] % (dataPositionArray.length - 1), dataPositionArray);
        if (i < printLimit) tools.cprint(dataPositionArray);
    }

    const newArray = dataPositionArray.map(x => lines[x]);
    return newArray;
}

function move(relativeIndex, magnitude, dataPositionArray) {
    if (magnitude == 0) return;

    let positionIndex = dataPositionArray.indexOf(relativeIndex);

    let effectiveIndex = (positionIndex + magnitude) % (dataPositionArray.length - 1);

    if (effectiveIndex == 0) {
        effectiveIndex = dataPositionArray.length - 1;
    }


    if (positionIndex + magnitude < 0) {
        effectiveIndex = positionIndex + dataPositionArray.length - 1 - (Math.abs(magnitude) % (dataPositionArray.length - 1));
    }


    let start = Math.min(effectiveIndex, positionIndex);
    let end = Math.max(effectiveIndex, positionIndex);


    if (magnitude == 4) {
        let debugPoint = 1;
    }

    let sign = start != effectiveIndex ? 1 : -1;

    if ((positionIndex + magnitude) > (dataPositionArray.length - 1)) {
        sign = -1;

    }

    let dataPosArrayCopy = dataPositionArray.slice();
    for (let i = start; i <= end; i++) {
        dataPosArrayCopy[i] = dataPositionArray[(i + sign) % (dataPositionArray.length)];
    }

    dataPosArrayCopy[effectiveIndex] = relativeIndex;


    dataPositionArray.length = 0;
    dataPositionArray.push(...dataPosArrayCopy);

    // indexArray[effectiveIndex ] = refIndex;

    // Initial arrangement:
    //   1, 2, -3, 3, -2, 0, 4
    //>> 0, 1,  2, 3,  4, 5, 6 



    // FIRST 
    // 1 moves between 2 and -3:
    //   2, 1, -3, 3, -2, 0, 4
    //>> 1, 0, 2, 3, 4, 5, 6 

    // SECOND 
    // 2 moves between -3 and 3:
    //   1, -3, 2, 3, -2, 0, 4
    //>> 0,  2, 1, 3,  4, 5, 6 

    // THIRD 
    // -3 moves between -2 and 0:
    //   1, 2, 3, -2, -3, 0, 4
    //>> 0, 1, 3,  4,  2, 5, 6 

    // 3 moves between 0 and 4:
    //   1, 2, -2, -3, 0, 3, 4
    //>> 0, 1,  4,  2, 5, 3, 6 

    // -2 moves between 4 and 1:
    // 1, 2, -3, 0, 3, 4, -2
    // 0, 1,  2, 5, 3, 6,  4

    // 0 does not move:
    // 1, 2, -3, 0, 3, 4, -2
    // 0, 1,  2, 5, 3, 6,  4

    // 4 moves between -3 and 0:
    // 1, 2, -3, 4, 0, 3, -2
    // 0, 1,  2, 6, 5, 3,  4 



}

main();