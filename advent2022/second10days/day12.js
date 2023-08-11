import * as tools from '../tools.js';

function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d12_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    lines.forEach(line => {
        array.push(line.split("").map(x => x.charCodeAt()));
    });

    if (fileName.includes("test")) printBoard(array);



    const start = new Date();
    const startingPoints = [];

    // yea i cheated - i notice all the b's only show up exclusively in 2nd column
    for (let i = 0; i < array.length; i++) {
        startingPoints.push([i, 1]);
    }

    // seeing others solutions ... they simply go from end to closest start 

    const destinationPoint = locate("E".charCodeAt(), array);

    const counters = []
    // const startingPoint = locate("S".charCodeAt(), inputMap);
    for (const startingPoint of startingPoints) {
        const counter = bfsHike(array, startingPoint, destinationPoint);
        // tools.cprint(counter);
        counters.push(counter);
    }

    const minSteps = Math.min(...counters);


    tools.cprint("\n\n");
    tools.cprint(minSteps + 1);

    const endDate = new Date();
    const seconds = (endDate.getTime() - start.getTime()) / 1000;
    tools.cprint(seconds + " seconds");



}


function locate(character, input) {
    const locate = []
    for (let y = 0; y < input.length; y++) {
        for (let x = 0; x < input[0].length; x++) {
            if (input[y][x] == character) {
                locate.push(y);
                locate.push(x);
                return locate;
            }
        }
    }
    return locate;

}

function bfsHike(inputMap2, startingPoint, destinationPoint) {
    const inputMap = inputMap2.slice();
    const queue = [];
    const visited = new Set();
    // const startingPoint = locate("S".charCodeAt(), inputMap);
    // const destinationPoint = locate("E".charCodeAt(), inputMap);
    inputMap[startingPoint[0]][startingPoint[1]] = 'b'.charCodeAt();
    inputMap[destinationPoint[0]][destinationPoint[1]] = 'z'.charCodeAt();

    queue.push(createWork(0, startingPoint[0], startingPoint[1]));

    let isFound = false;
    let counter = 0;

    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    do {
        const batches = queue.slice();
        queue.length = 0;
        for (const batch of batches) {
            const { depth, y, x } = batch;
            visited.add(y + "-" + x)
            const currentValue = inputMap[y][x];

            if (y == destinationPoint[0] && x == destinationPoint[1]) {
                isFound = true;
                counter = depth;
            }

            for (const [dy, dx] of directions) {

                let tmpY = y + dy;
                let tmpX = x + dx;;
                // up
                if (!visited.has(tmpY + "-" + tmpX)
                    && tmpY >= 0
                    && tmpY < inputMap.length
                    && tmpX >= 0
                    && tmpX < inputMap[0].length
                    && Math.max(1, inputMap[tmpY][tmpX] - currentValue) == 1) {
                    visited.add(tmpY + "-" + tmpX);
                    queue.push(createWork(depth + 1, tmpY, tmpX));
                }
            }
            if (currentValue == 115) {
                let anotherDebugPoint = 1;

            }
            let debug = 1;
        }

    } while (queue.length > 0 && !isFound)

    return counter;
}



function createWork(depth, y, x) {
    return { depth, y, x };
}

function printBoard(array) {
    for (const line of array) {
        tools.cprint(line.join(" "))
    }
}

main();