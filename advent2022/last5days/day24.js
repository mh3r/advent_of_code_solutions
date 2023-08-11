import * as tools from '../tools.js';

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d24_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    snowFrog(lines);


}


function snowFrog(input) {

    const width = input[0].length;
    const length = input.length;

    // UP, RIGHT, DOWN, LEFT 
    const blizzardPatterns = [[], [], [], []];



    for (let y = 1; y < length - 1; y++) {
        for (let x = 1; x < width - 1; x++) {
            const current = input[y][x];
            switch (current) {
                case "^":
                    blizzardPatterns[0].push([y, x]);
                    break;
                case ">":
                    blizzardPatterns[1].push([y, x]);
                    break;
                case "v":
                    blizzardPatterns[2].push([y, x]);
                    break;
                case "<":
                    blizzardPatterns[3].push([y, x]);
                    break;
            }
        }
    }

    winterIsComing(width, length, blizzardPatterns);

    let debug = 1;
}

function populateBlizzardMap(blizzardPatterns, blizzardMap) {
    blizzardMap.clear();
    for (const directions of blizzardPatterns) {
        for (const coordinate of directions) {
            blizzardMap.add(elfWordBind(coordinate));
        }
    }
}

function winterIsComing(width, length, blizzardPatterns) {
    let minute = 0;
    const start = [0, 1];
    const end = [length - 1, width - 2];
    const blizzardMap = new Set();
    const possibleSteps = [[0, 0], [0, 1], [1, 0], [-1, 0], [0, -1]];
    let currentPositions = [elfWordBind(start)];

    let isContinue = true;
    let trip = 0;
    loop1:
    while (isContinue) {
        const nextPositions = new Set();
        simulateBlizzard(width, length, blizzardPatterns);
        populateBlizzardMap(blizzardPatterns, blizzardMap);

        for (const current of currentPositions) {
            const splitted = current.split(":");
            const y = Number(splitted[0]);
            const x = Number(splitted[1]);
            for (const [dx, dy] of possibleSteps) {
                let sumY = y + dy;
                let sumX = x + dx;

                if (sumY == end[0] && sumX == end[1]) {
                    trip++;
                    minute++;
                    if (trip == 1) {
                        currentPositions = [elfWordBind(end)];
                        end[0] = 0;
                        end[1] = 1;
                        continue loop1;
                    } else if (trip == 2) {
                        currentPositions = [elfWordBind(start)];
                        end[0] = length - 1;
                        end[1] = width - 2
                        continue loop1;
                    } else {
                        isContinue = false;
                    }
                }

                if (sumY > 0 && sumY < (length - 1) && sumX > 0 && sumX < (width - 1) && !blizzardMap.has(elfWordBind([sumY, sumX]))) {
                    nextPositions.add(elfWordBind([sumY, sumX]));
                } else if ((sumY == 0 && sumX == 1) || (sumY == (length - 1) && sumX == (width - 2))) {
                    nextPositions.add(elfWordBind([sumY, sumX]));
                }

            }
        }

        currentPositions = Array.from(nextPositions);

        minute++;

        if (minute == 17) {
            let debug = 1;
        }

    }

    // applies for part 2 ... otherwise just minute 
    tools.cprint(minute - 1);
}

function simulateBlizzard(width, length, blizzardPatterns) {

    for (let b = 0; b < 4; b++) {
        for (let i = 0; i < blizzardPatterns[b].length; i++) {
            let dx = 0;
            let dy = 0;

            switch (b) {
                case 0:
                    dy = -1;
                    break;

                case 1:
                    dx = 1;
                    break;

                case 2:
                    dy = 1;
                    break;

                case 3:
                    dx = -1;
                    break;

            }
            let sumY = blizzardPatterns[b][i][0] + dy;
            let sumX = blizzardPatterns[b][i][1] + dx;

            sumY = sumY == 0 ? length - 2 : sumY;
            sumY = sumY == length - 1 ? 1 : sumY;

            sumX = sumX == 0 ? width - 2 : sumX;
            sumX = sumX == width - 1 ? 1 : sumX;

            blizzardPatterns[b][i] = [sumY, sumX];
        }
    }
}

function elfWordBind(array) {
    return `${array[0]}:${array[1]}`;
}

main();