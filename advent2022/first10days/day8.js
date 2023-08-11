import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d8_input.txt";

    let counter = 1;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    lines.forEach(line => {
        array.push([...line].map(x => Number(x)));
    });

    // console.log(JSON.stringify(array, null, 2))


    console.log(peepingTom(array));
    console.log(scenicScore(array));

    // 1597 is wrong 
    // 374556 is wrong 

    // for (let x = 0; x < array[0].length; x++) {
    //     console.log(array[1][x] + " --> " + horizontalScenicScore(array[1], x));

    // }

    // tools.printJson(constructVertically(array, 3));

}


function peepingTom(input) {
    let counter = 0;
    for (let y = 0; y < input.length; y++) {
        for (let x = 0; x < input[0].length; x++) {

            if (isVisibleHorizontally(input[y], x) || isVisibleHorizontally(constructVertically(input, x), y)) {
                // console.log(` ${y} ${x}  `);
                counter++;
            }
        }
    }

    return counter;

}

function scenicScore(input) {
    let counter = [];
    for (let y = 0; y < input.length; y++) {
        for (let x = 0; x < input[0].length; x++) {
            const first = horizontalScenicScore(input[y], x);
            const second = horizontalScenicScore(constructVertically(input, x), y);
            // console.log(` ${y} ${x}   ${first} * ${second}`);

            counter.push(first * second);
        }
    }

    return Math.max(...counter);

}

function constructVertically(array, index) {
    const tmp = [];
    for (let y = 0; y < array.length; y++) {
        tmp.push(array[y][index]);
    }
    return tmp;
}

function isVisibleHorizontally(array, index) {
    const value = array[index];
    const left = array.slice(0, index);
    const right = array.slice(index + 1);

    return left.length == 0
        || right.length == 0
        || Math.max(...left, value - 1) < value
        || Math.max(...right, value - 1) < value;

}

function horizontalScenicScore(array, index) {
    const value = array[index];
    const left = array.slice(0, index);
    left.reverse();
    const right = array.slice(index + 1);
    return rightScenicCounter(right, value) * rightScenicCounter(left, value);
}

function rightScenicCounter(array, value) {
    let counter = 0;
    for (const x of array) {
        counter++;
        if (x >= value) {
            break;
        }
    }

    // counter = Math.max(counter, 1);
    return counter;
}


main();