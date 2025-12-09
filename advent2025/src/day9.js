import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = 4786902990

    const tiles = []
    for (const line of config.raw) {
        tiles.push(new Tile(line))
    }

    for (let i = 0; i < tiles.length - 1; i++) {
        for (let j = i + 1; j < tiles.length; j++) {
            tiles[i].populateArea([tiles[j]])
        }
    }

    let biggest = 0
    for (const tile of tiles) {
         for (const key of Object.keys(tile.area)) {
            const area = tile.area[key]
            if (area > biggest) {
                biggest = area
            }
        }
    }

    // an attempt of part 2 ... trying to fill in boundary 
    // then flood fill it 
    // and then validate area against imaginary corners if they reside within the boundary
    let leastY = Infinity
    for (const tile of tiles) {
        if (tile.y < leastY) {
            leastY = tile.y
        }
    }

    console.log("Least Y: " + leastY)

    console.log(config.raw.filter(x => x.endsWith(`,${leastY}`)) )

    answer = biggest

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d9_input.txt`;
    inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    part1({ ...config });
    part2({ ...config });
}

class Tile {
    area = {}
    constructor(input) {
        this.name = input
        const splitted = input.split(",");
        this.x = parseInt(splitted[0])
        this.y = parseInt(splitted[1])
    }

    populateArea(tiles) {
        for (const tile of tiles) {
            const dx = Math.abs(this.x - tile.x) + 1
            const dy = Math.abs(this.y - tile.y) + 1

            this.area[tile.name] = dx * dy
        }
    }



}


main();