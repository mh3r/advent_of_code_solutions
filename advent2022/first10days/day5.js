import * as tools from '../tools.js';

function main() {
    let array = [];
    const instructions = [];
    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d5_input.txt";

    let counter = 1;
    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        if (line.includes("move")) {
            instructions.push(line);
        } else {
            array.push(line);
        }
    });

    array.splice(array.length - 1);
    const barrels = populateBarrels(array);

    // instructions.forEach(x => moveBarrels(barrels, x));
    instructions.forEach(x => moveBarrelsEffectively(barrels, x));

    console.log(JSON.stringify(barrels, null, 2));

    let barrelWordSkim = "";

    for (const [key, value] of Object.entries(barrels)) {
        if (value.length > 0) {
            barrelWordSkim += value[value.length - 1];
        }
    }

    console.log(barrelWordSkim);


    let test = [];
    test.push("N", "Z")
    test.push("M", "C", "D")
    test.push("P")

}

function populateBarrels(array) {
    const barrels = {};
    const numberOfBarrels = array.pop().trim().split(" ").pop();
    console.log(numberOfBarrels);

    for (const line of array) {
        let charCounter = 0;
        let tmpChar = "";
        for (const char of line) {

            if (char != '[' && char != ']' && char != " ") {
                tmpChar = char;
                // }
                // if (charCounter % 4 == 0 && tmpChar != "") {
                const barrelNumber = Math.ceil(charCounter / 4);
                const tmp = barrels[barrelNumber];
                if (tmp == null) {
                    barrels[barrelNumber] = [];
                }

                barrels[barrelNumber].push(tmpChar);
                tmpChar = "";
            }
            charCounter++;
        }
    }

    for (let i = 1; i <= numberOfBarrels; i++) {
        barrels[i].reverse();
    }

    return barrels;
}

function moveBarrels(barrels, instruction) {
    let move = instruction.replaceAll("move ", "").replaceAll("from ", "").replaceAll("to ", "").split(" ");

    for (let i = 0; i < move[0]; i++) {
        barrels[move[2]].push(barrels[move[1]].pop());
    }
}


function moveBarrelsEffectively(barrels, instruction) {
    let [amount, from, to] = instruction.replaceAll("move ", "").replaceAll("from ", "").replaceAll("to ", "").split(" ");

    const reverseNumber = barrels[from].length - amount;
    barrels[to].push(...barrels[from].slice(reverseNumber));
    barrels[from] = barrels[from].slice(0, reverseNumber);
}




main();