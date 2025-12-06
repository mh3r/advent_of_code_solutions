import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = 6299564383938

    for (let i = 0; i < config.data[0].length; i++) {

        const data = []
        for (let value of config.data) {
            data.push(value[i])
        }

        answer += calculate(config.operator[i], data)
        // console.log(answer)
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function calculate(operator, input) {
    if (operator === '+') {
        return input.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    } else {
        return input.reduce((accumulator, currentValue) => accumulator * currentValue, 1);

    }
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 11950004808442

    const gridData = []
    const operatorLine = config.raw[config.raw.length - 1]
    const operatorIndexes = [...getAllIndexes(operatorLine, '*'), ...getAllIndexes(operatorLine, '+')]
    operatorIndexes.sort((a, b) => a - b);
    for (let i = 0; i < config.raw.length; i++) {
        const line = config.raw[i]
        gridData.push(...line.split())
    }

    let grid
    for (let i = 0; i < operatorIndexes.length; i++) {
        const startIndex = operatorIndexes[i]
        const endIndex = i + 1 == operatorIndexes.length ? gridData[0].length : operatorIndexes[i + 1] -1

        grid = []
        for (let j = 0; j < gridData.length; j++) {
            grid.push(gridData[j].slice(startIndex, endIndex))
        }
        answer += extractAndCalculateGrid(grid)
    }

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function extractAndCalculateGrid(grid) {
    const operator = grid[grid.length - 1][0]
    let numbers = []

    for (let c = 0; c < grid[0].length; c++) {
    let numberStr = ''
        for (let r = 0; r < grid.length - 1; r++) {
            numberStr += grid[r][c]
        }
        numbers.push(parseInt(numberStr))
    }

    return calculate(operator, numbers)
}


function getAllIndexes(str, char) {
    const indices = [];
    let startIndex = 0;
    let index
    // Use indexOf in a loop, updating the start index after each find
    while ((index = str.indexOf(char, startIndex)) !== -1) {
        indices.push(index);
        startIndex = index + 1; // Start the next search from the position after the last found index
    }
    return indices;
}




function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d6_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const data = []

    let operator = []


    for (let i = 0; i < config.raw.length; i++) {
        if (i === config.raw.length - 1) {
            operator = tools.removeAllDoubleSpaces(config.raw[i].trim()).replaceAll("  ", " ").split(" ").filter(x => x)
        } else {
            data.push(tools.removeAllDoubleSpaces(config.raw[i].trim()).split(" ").map(x => parseInt(x)))
        }
    }
    config.data = data
    config.operator = operator

    // part1({ ...config });
    part2({ ...config });
}

main();