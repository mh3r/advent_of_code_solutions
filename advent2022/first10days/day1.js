import * as tools from '../tools.js';

function main() {
    const array = []
    const tmpArray = [];
    const addArray = []

    let fileName = "D:/dled/advent2022/test.txt";
    fileName = "advent2022/data/d1_input.txt";

    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        if (line.length == 0) {
            array.push(tmpArray.slice());
            tmpArray.length = 0;
        } else {
            tmpArray.push(parseInt(line));
        }
    });

    array.forEach(x => {
        const sum = x.reduce((partialSum, a) => partialSum + a, 0);
        addArray.push(sum);
    })

    addArray.sort((function (a, b) {
        return a - b;
    }));
    const sumOfTop3 = addArray.slice(-3).reduce((partialSum, a) => partialSum + a, 0);

    printJson(addArray);

    const answer = Math.max(...addArray);

    printJson(answer);
    printJson(sumOfTop3);
}

function printJson(data) {
    console.log(JSON.stringify(data, null, 2));
}

main();