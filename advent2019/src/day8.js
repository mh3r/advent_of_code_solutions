import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

function part1(config) {
    let answer = 0;
    const correctAnswer = 2016

    config.pixel.width = 3
    config.pixel.height = 2
    const layers = layerOutData(config)

    let layerWithLeastZero
    let leastCount
    for (let i = 0; i < layers.length; i++) {
        const layer = layers[i]
        if (i === 0) {
            layerWithLeastZero = layer
            leastCount = countCharacter([layer], 0)
        } else {
            const currentCount = countCharacter([layer], 0)
            if (leastCount > currentCount) {
                leastCount = currentCount
                layerWithLeastZero = layer
            }
        }
    }

    console.log(layerWithLeastZero)
    answer = countCharacter([layerWithLeastZero], 1) * countCharacter([layerWithLeastZero], 2)


    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function layerOutData(config) {

    const retval = []
    const layerLength = config.pixel.width * config.pixel.height
    for (let i = 0; i < config.raw.length; i += layerLength) {
        retval.push(config.raw.slice(i, i + layerLength))

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
    inputFile = `${baseDir}\\data\\test.txt`;

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


    part1({ ...config });
    part2({ ...config });
}

main();


