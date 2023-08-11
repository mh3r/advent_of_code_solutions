import * as tools from '../tools.js';

const ELF = "#";
const U = 1;
const D = 2;
const L = 4;
const R = 8;

const directions = [U, D, L, R];

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d23_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");



    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const elves = [];

    for (let y = 0; y < lines.length; y++) {
        for (let x = 0; x < lines[0].length; x++) {
            const char = lines[y].charAt(x);
            if (char == ELF) {
                elves.push([y, x]);
            }
        }
    }
    run(elves);
}


function run(elves) {
    // elves.forEach(x => tools.cprint(scanAdjacent(x, elfBound)));

    const rep = 1550;
    for (let iteration = 0; iteration < rep; iteration++) {
        const elfBound = [];
        elves.forEach(x => elfBound.push(elfWordBind(x)));

        let minScanResult = 15
        for (const elf of elves) {
            const scanResult = scanAdjacent(elf, elfBound);
            if (scanResult < minScanResult) {
                minScanResult = scanResult;
                break;
            }
        }
        if (minScanResult == 15) {
            tools.cprint("We must stop here:  " + (iteration + 1));
            break;
        }



        let direction = directions[(iteration % directions.length)];
        let approvedItinerary = scoutAhead(elves, elfBound, direction);

        for (let i = 0; i < elves.length; i++) {
            const nextMove = approvedItinerary[i];
            if (nextMove != null) {
                elves[i] = nextMove;
            }
        }

        if (iteration < 100 || iteration % 100 == 0) {
            const newLocations = [];
            elves.forEach(x => newLocations.push(elfWordBind(x)));
            tools.cprint(newLocations)

        }



    }


    const ys = [];
    const xs = [];
    for (const [y, x] of elves) {
        ys.push(y);
        xs.push(x);
    }

    const xMax = Math.max(...xs);
    const yMax = Math.max(...ys);
    const xMin = Math.min(...xs);
    const yMin = Math.min(...ys);

    const total = (xMax - xMin + 1) * (yMax - yMin + 1) - elves.length;
    tools.cprint(total);

    let debug = 0;

}

function elfWordBind(array) {
    return `${array[0]}:${array[1]}`;
}

function scanAdjacent(array, elfBound) {
    let retval = 0;
    const y = array[0];
    const x = array[1];

    const topLeft = elfWordBind([y - 1, x - 1]);
    const top = elfWordBind([y - 1, x]);
    const topRight = elfWordBind([y - 1, x + 1]);

    const left = elfWordBind([y, x - 1]);
    const right = elfWordBind([y, x + 1]);

    const bottomLeft = elfWordBind([y + 1, x - 1]);
    const bottom = elfWordBind([y + 1, x]);
    const bottomRight = elfWordBind([y + 1, x + 1]);

    if (!elfBound.includes(topLeft) && !elfBound.includes(top) && !elfBound.includes(topRight)) retval += U;
    if (!elfBound.includes(bottomLeft) && !elfBound.includes(bottom) && !elfBound.includes(bottomRight)) retval += D;
    if (!elfBound.includes(topLeft) && !elfBound.includes(left) && !elfBound.includes(bottomLeft)) retval += L;
    if (!elfBound.includes(topRight) && !elfBound.includes(right) && !elfBound.includes(bottomRight)) retval += R;

    return retval;
}

function scoutAhead(elves, elfBound, direction) {

    let itinerary = [];
    const itineraryHardCopy = [];
    const duplicate = [];

    for (const elf of elves) {
        const y = elf[0];
        const x = elf[1];
        let directionCopy = direction;
        const scanResult = scanAdjacent(elf, elfBound);
        if (scanResult == 15 || scanResult == 0) {
            itinerary.push(null);
            continue;
        }
        let proposedNext;
        let proposedNextBound;

        loop1:
        for (let i = 0; i < 4; i++) {

            switch (directionCopy) {
                case U:
                    proposedNext = [y - 1, x];
                    if ((scanResult & U) == 0) {
                        directionCopy = directions[((directions.indexOf(directionCopy) + 1) % 4)];
                        continue loop1;
                    }
                    break;
                case D:
                    proposedNext = [y + 1, x];
                    if ((scanResult & D) == 0) {
                        directionCopy = directions[((directions.indexOf(directionCopy) + 1) % 4)];
                        continue loop1;
                    }
                    break;
                case R:
                    proposedNext = [y, x + 1];
                    if ((scanResult & R) == 0) {
                        directionCopy = directions[((directions.indexOf(directionCopy) + 1) % 4)];
                        continue loop1;
                    }
                    break;
                case L:
                    proposedNext = [y, x - 1];
                    if ((scanResult & L) == 0) {
                        directionCopy = directions[((directions.indexOf(directionCopy) + 1) % 4)];
                        continue loop1;
                    }
                    break;
            }


            itinerary.push(proposedNext);

            proposedNextBound = elfWordBind(proposedNext);

            if (!itineraryHardCopy.includes(proposedNextBound)) {
                itineraryHardCopy.push(proposedNextBound);
            } else {
                duplicate.push(proposedNextBound);
            }
            break;

        }



    }


    for (let i = 0; i < itinerary.length; i++) {
        const coordinate = itinerary[i];
        if (coordinate != null) {
            const tmpWordBind = elfWordBind(coordinate);
            if (duplicate.includes(tmpWordBind)) {
                itinerary[i] = null;
            }

        }
    }

    return itinerary;
}


main();