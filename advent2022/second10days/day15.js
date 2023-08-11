import * as tools from '../tools.js';

const AIR = ".";
const HASH = "#";
const VERTICAL_PADDING = 15;
const HORIZONTAL_PADDING = 15;
let fileName;

function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d15_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 1;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const locations = []
    lines.forEach(line => {
        parseInput(locations, line);
        // console.log(line);
    });

    const bases = findBases(locations);
    // tools.printJson(locations);
    tools.printJson(bases);
    const board = terraform(locations, bases);
    // tools.printBoard(board)

    // 4838163 too low 

}

function parseInput(locations, line) {
    const uselessWords = ["Sensor at x=", " y=", "x="];
    uselessWords.forEach(x => line = line.replaceAll(x, ""));
    // tools.cprint(line)
    const split = line.split(": closest beacon is at ");
    const sensor = split[0].split(",").map(x => Number(x));
    const beacons = split[1].split(",").map(x => Number(x));
    locations.push([sensor, beacons]);
}

function terraform(locations, bases) {
    const board = [];
    let yMarker = fileName.includes("test") ? 10 : 2000000;
    locations = filterLocations(locations, yMarker);

    // locations = [locations.pop()];
    tools.cprint(`Important locations: ${locations.length} filtered against ${yMarker}`);

    // yMarker += bases[5];
    // thx keeper ... got me a star!!!
    let counter = new Set();
    locations.forEach(i => {
        const sensor = i[0];
        const beacon = i[1];

        const radius = Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);
        let y = sensor[1] - yMarker;
        for (let x = -1 * radius; x <= radius; x++) {

            if (((x + sensor[0]) == beacon[0] && (sensor[1] - y) == beacon[1])
                || (x == 0 && y == 0)) {
                continue;
            }
            if (Math.abs(y) + Math.abs(x) <= radius) {
                counter.add(sensor[0] + x);
            }
        }
    }

    );
    tools.cprint(`Hashes number: ${counter.size}`);

    return board
}



function terraform2(locations, bases) {
    const board = [];
    const rows = Array(bases[1] - bases[0] + 1 + 2 * bases[4]).fill(AIR);
    const columns = bases[3] - bases[2] + 1 + 2 * bases[5];

    Array.from(Array(columns)).forEach(() => {
        board.push(rows.slice());
    })

    // console.log(board[0].length)
    // console.log(board.length)


    let yMarker = fileName.includes("test") ? 10 : 2000000;


    locations = filterLocations(locations, yMarker);

    tools.cprint(`Important locations: ${locations.length} filtered against ${yMarker}`);

    yMarker += bases[5];

    locations.forEach(i => {
        const sensor = i[0];
        const beacon = i[1];

        const sensorLocationX = sensor[0] - bases[0] + bases[4];
        const sensorLocationY = sensor[1] - bases[2] + bases[5];

        const beaconLocationX = beacon[0] - bases[0] + bases[4];
        const beaconLocationY = beacon[1] - bases[2] + bases[5];

        board[sensorLocationY][sensorLocationX] = "S";
        board[beaconLocationY][beaconLocationX] = "B";

        drawRadiation(board, [sensorLocationX, sensorLocationY], [beaconLocationX, beaconLocationY], yMarker);
    }

    );

    // board[yMarker][0] = "o";
    let counter = 0;
    for (const i of board[yMarker]) {
        if (i == HASH) counter++;
    }

    tools.cprint(counter);

    // let floorLevel = bases[3] - bases[2] + 2 + bases[5];
    // console.log(floorLevel);
    // board[floorLevel] = board[floorLevel].map(x => ROCK);

    // bluePrint.push([[0, bases[3] + 2], [board[0].length - 1, bases[3] + 2]]);

    // bluePrint.forEach(x => construct(board, x, bases));
    return board
}


function filterLocations(locations, yMarker) {
    const newLocations = [];
    locations.forEach(i => {
        const sensor = i[0];
        const beacon = i[1];

        const radius = Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);

        if (sensor[1] - radius <= yMarker && sensor[1] + radius >= yMarker) {
            newLocations.push(i);
        }


    });
    return newLocations;
}

function drawRadiation(board, sensor, beacon, interestedRow) {
    const radius = Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);
    for (let y = -1 * radius; y <= radius; y++) {
        for (let x = -1 * radius; x <= radius; x++) {

            if ((x + sensor[0] == beacon[0] && y + sensor[1] == beacon[1]) || (x == 0 && y == 0)) {
                continue;
            }
            if (Math.abs(y) + Math.abs(x) <= radius && sensor[1] + y == interestedRow) {
                board[sensor[1] + y][sensor[0] + x] = HASH;
            }

        }
    }
}


function findBases(locations) {
    let xMin, xMax, yMin, yMax;

    locations.forEach(a => a.forEach(
        task => {
            const x = task[0];
            const y = task[1];
            xMin ??= x;
            xMax ??= x;
            yMin ??= y;
            yMax ??= y;

            xMin = Math.min(xMin, x);
            xMax = Math.max(xMax, x);
            yMin = Math.min(yMin, y);
            yMax = Math.max(yMax, y);
        }));

    return [xMin, xMax, yMin, yMax, HORIZONTAL_PADDING, VERTICAL_PADDING];
}

main();