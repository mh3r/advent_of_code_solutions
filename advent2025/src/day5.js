import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = 773

    for (const ingredient of config.ingredients) {
        for (const [min, max] of config.ranges) {
            if (ingredient >= min && ingredient <= max) {
                answer++;
                break;
            }
        }
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 332067203034711
    const cleanedRanges = mergeRanges(config.ranges);

    for (const [min, max] of cleanedRanges) {
        answer += max - min + 1;
    }

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function mergeRanges(ranges) {
    const retval = [];
    const copyRange = [...ranges]
    copyRange.sort((a, b) => a[0] - b[0]);
    for (const [min, max] of copyRange) {
        if (retval.length == 0) {
            retval.push([min, max]);
            continue;
        }
        let merged = false;
        for (const range of retval) {
            if ((min >= range[0] && min <= range[1])
                || (max >= range[0] && max <= range[1])

            ) {
                range[0] = Math.min(range[0], min);
                range[1] = Math.max(range[1], max);
                merged = true;
                break;
            }
        }
        if (!merged) {
            retval.push([min, max]);
        }
    }

    return retval
}


function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d5_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const ranges = [];
    const ingredients = [];


    for (const line of lines) {
        if (line.includes('-')) {
            const [part1, part2] = line.split('-');
            ranges.push([parseInt(part1), parseInt(part2)]);
            continue;
        }

        if (line.trim().length > 0) {
            ingredients.push(parseInt(line));
            continue
        }
    }

    config.ranges = ranges;
    config.ingredients = ingredients;

    part1({ ...config });
    part2({ ...config });
}

main();