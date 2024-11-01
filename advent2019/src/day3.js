import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;
const testFile = `${baseDir}\\data\\test.txt`;

const origin = [0, 0]

function traverse(paths) {
    let current = origin.slice()
    const retval = []

    for (const path of paths) {
        const direction = path.slice(0, 1)
        const range = Number(path.slice(1, path.length))

        for (let i = 0; i < range; i++) {
            const tmp = tools.ADJ_DIRS[tools.DIRS.indexOf(direction)]
            current = [current[0] + tmp[0], current[1] + tmp[1]]

            retval.push(tools.bindArray(current))
        }
    }
    return retval
}

function part1(input) {
    let answer;

    const totalDistances = input.map(x => tools.manhattanDistance(origin, tools.unbindArray(x)))
    console.log(totalDistances)

    answer = Math.min(...totalDistances)

    console.log(`Part 1: ${answer}`)

    const finalAnswer = 3229
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function part2(input, firstSteps, secondSteps) {
    let answer;

    const stepsArray = input.map(x => firstSteps.indexOf(x) + secondSteps.indexOf(x) + 2)

    console.log(stepsArray)
    answer = Math.min(...stepsArray)

    console.log(`Part 2: ${answer}`)
    const finalAnswer = 32132
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function main() {
    let inputFile = `${dataDir}\\d3_input.txt`;
    inputFile = testFile;

    console.log("Input File: " + inputFile);
    const input = tools.readFileFromLocal(inputFile).split(/\r?\n/);

    const firstSteps = traverse(Array.from(input[0].split(",")));
    const secondSteps = traverse(Array.from(input[1].split(",")));

    const intersections = firstSteps.filter(x => secondSteps.includes(x))
    console.log(intersections)

    part1(intersections);
    part2(intersections, firstSteps, secondSteps);
}

main();


