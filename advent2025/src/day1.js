import * as tools from '../../js-util/tools.js';

const YEAR = 2025;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

function part1(config) {
    let answer = 0;
    const correctAnswer = 1141
    let cursor = 50
    for (let instruction of config.instructions) {
        instruction = instruction % 100
        cursor += instruction

        if (cursor < 0) {
            cursor += 100
        } else if (cursor >= 100) {
            cursor -= 100
        }
        if (cursor === 0) {
            answer++
        }
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 6634

    let cursor = 50
    for (let instruction of config.instructions) {
        const projection = cursor + instruction

        if (projection >= 0 && projection < 100) {
            cursor = projection
            if (cursor === 0) {
                answer++
            }
            continue
        }

        let rotations = Math.abs(Math.trunc(projection / 100))
        if (cursor > 0 && projection < 0) {
            rotations++
        }
        answer += rotations
        cursor = (projection % 100 + 100) % 100
    }

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    let inputFile = `${dataDir}\\d1_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const instructions = []
    for (const line of lines) {
        const modifier = (line[0] === 'L') ? -1 : 1
        instructions.push(modifier * parseInt(line.slice(1)))

    }
    config.instructions = instructions

    part1({ ...config });
    part2({ ...config });
}

main();