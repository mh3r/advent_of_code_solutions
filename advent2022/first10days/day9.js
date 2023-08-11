import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d9_input.txt";

    let counter = 1;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const tailTracks = new Set();
    const nineTailTracks = new Set();
    const startingPoint = 10000;
    const tailCursor = [startingPoint, startingPoint];
    const headCursor = [startingPoint, startingPoint];
    tailTracks.add(tailCursor.join(":"));
    nineTailTracks.add(tailCursor.join(":"));

    const snake = Array(8).fill(0).map(x => [startingPoint, startingPoint]);

    lines.forEach(line => {
        headTails(line, headCursor, tailCursor, tailTracks, snake, nineTailTracks)
    });

    console.log(tailTracks.size);
    console.log(nineTailTracks.size);
    // 5883 
    // 2367 
    // 2121 your answer is too low.
    // 2268, 2355 is wrong try ........ 2367 
    // 2416 your answer is too high. 
    // console.log(Array.from(nineTailTracks));
    printBoard(Array.from(nineTailTracks));


}

function printBoard(data) {

    const xs = [];
    const ys = [];

    data.forEach(x => {
        xs.push(x.split(":")[0]);
        ys.push(x.split(":")[1]);
    });

    const smallestX = Math.min(...xs);
    const smallestY = Math.min(...ys);
    const biggestX = Math.max(...xs);
    const biggestY = Math.max(...ys);

    console.log(smallestX);
    console.log(smallestY);


    for (let y = biggestY; y >= smallestY; y--) {
        let line = "";
        for (let x = smallestX; x <= biggestX; x++) {
            line += (data.includes(x + ":" + y)) ? "#" : ".";
        }
        console.log(line);
    }



}

function headTails(instruction, headCursor, tailCursor, tailTracks, snake, nineTailTracks) {

    const dir = instruction.split(" ")[0];
    const steps = Number(instruction.split(" ")[1]);

    for (let i = 0; i < steps; i++) {
        if (dir == "R") {
            headCursor[0]++;
        }
        if (dir == "L") {
            headCursor[0]--;
        }
        if (dir == "U") {
            headCursor[1]++;
        }
        if (dir == "D") {
            headCursor[1]--;
        }
        // console.log(headCursor)
        // adjustTail(headCursor, tailCursor, tailTracks);
        if (Math.abs(headCursor[0] - tailCursor[0]) == 2) {
            const mod = (dir == "R") ? 1 : -1;
            tailCursor.push(tailCursor[0] + mod);
            tailCursor.push(headCursor[1]);
            tailCursor.shift();
            tailCursor.shift();
        }
        if (Math.abs(headCursor[1] - tailCursor[1]) == 2) {
            const mod = (dir == "U") ? 1 : -1;
            tailCursor.push(headCursor[0])
            tailCursor.push(tailCursor[1] + mod);
            tailCursor.shift();
            tailCursor.shift();
        }
        // console.log(headCursor + "    ----->  " + tailCursor)
        tailTracks.add(tailCursor.join(":"));

        propagateTail(tailCursor, snake[0]);

        for (let i = 0; i < snake.length - 1; i++) {
            propagateTail(snake[i], snake[i + 1]);
        }

        nineTailTracks.add(snake[7].join(":"));
    }
}

function propagateTail(head, tail,) {
    const horizontalDifference = Math.abs(head[0] - tail[0]);
    const verticalDifference = Math.abs(head[1] - tail[1]);

    if (horizontalDifference == 2 || verticalDifference == 2) {
        const hSign = (head[0] > tail[0]) ? -1 : 1;
        const vSign = (head[1] > tail[1]) ? -1 : 1;

        const newX = horizontalDifference == 2 ? head[0] + hSign : head[0];
        const newY = verticalDifference == 2 ? head[1] + vSign : head[1];

        tail.push(newX);
        tail.push(newY);

        tail.shift();
        tail.shift();
    }

}



main();