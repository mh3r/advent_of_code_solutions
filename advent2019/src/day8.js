import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;
const TRANSPARENT = 2

function part1(config) {
    let answer = 0;
    const correctAnswer = 2016

    // config.pixel.width = 3
    // config.pixel.height = 2

    let layerWithLeastZero
    let leastCount
    for (let i = 0; i < config.layers.length; i++) {
        const layer = config.layers[i]
        if (i === 0) {
            layerWithLeastZero = layer
            leastCount = countCharacter(layer, 0)
        } else {
            const currentCount = countCharacter(layer, 0)
            if (leastCount > currentCount) {
                leastCount = currentCount
                layerWithLeastZero = layer
            }
        }
    }
    // layerWithLeastZero.map(x => console.log(x))
    answer = countCharacter(layerWithLeastZero, 1) * countCharacter(layerWithLeastZero, 2)

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 'HZCZU'
    let pictureFrame = ''

    for (let y = 0; y < config.pixel.height; y++) {
        for (let x = 0; x < config.pixel.width; x++) {
            for (const layer of config.layers) {
                const character = Number(layer[y][x])
                if (character !== TRANSPARENT) {
                    pictureFrame += character == '1' ? '.' : ' '
                    break
                }
            }
        }
        pictureFrame += '\n'
    }

    console.log(pictureFrame)
    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function layerOutData(config) {
    const retval = []
    const layerLength = config.pixel.width * config.pixel.height
    for (let i = 0; i < config.raw.length; i += layerLength) {
        const row = []
        for (let j = i; j < i + layerLength; j += config.pixel.width)
            row.push(config.raw.slice(j, j + config.pixel.width))
        retval.push(row)
    }
    return retval
}

function countCharacter(layer, target) {
    let retval = 0
    for (const row of layer) {
        retval += row.split('').filter(x => x === target.toString()).length
    }
    return retval
}

function main() {
    let inputFile = `${dataDir}\\d8_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines.pop()
        , pixel: {
            width: 25
            , height: 6
        }
    }

    config.layers = layerOutData(config)

    part1({ ...config });
    part2({ ...config });
}

main();


