import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = 500

    for (const problem of config.problems) {
        answer += findSmallestPossibilities(problem)
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function findSmallestPossibilities(problem) {
    const { pattern, buttons } = problem;
    const strPattern = pattern.join(',')
    let retval = 0
    for (retval = 1; retval <= buttons.length; retval++) {
        const currentCombos = getUniqueCombo(buttons.length, retval)
        for (const combo of currentCombos) {
            let tempValue = []
            for (const index of combo) {
                tempValue = mergeArrays(tempValue, buttons[index])
            }
            tempValue.sort((a, b) => a - b)
            if (tempValue.join(',') == strPattern) {
                return retval
            }
        }
    }
}

function getUniqueCombo(length, limit) {
    const key = `${length}|${limit}`
    if (uniqueCombos[key]) return uniqueCombos[key];

    if (limit == 1) {
        Array.from({ length }, (value, index) => index).forEach(x => {
            uniqueCombos[key] = uniqueCombos[key] || []
            uniqueCombos[key].push([x])
        })
        return uniqueCombos[key]
    }

    const retval = []

    for (const value of uniqueCombos[`${length}|${limit - 1}`]) {
        let max = Math.max(...value)
        for (let i = max + 1; i < length; i++) {
            retval.push([...value, i])
        }
    }
    uniqueCombos[key] = retval;
    return uniqueCombos[key]

}

function mergeArrays(array1, array2) {
    const commonElements = array1.filter(value => array2.includes(value));
    const retval = [...array1, ...array2].filter(x => !commonElements.includes(x))

    return retval
}

function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d10_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const problems = []

    // [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    for (let line of lines) {
        line = line.replaceAll('[', '')
        const firstSplit = line.split(']')
        let pattern = firstSplit[0]
        const rest = firstSplit[1].trim().replaceAll('(', '').replaceAll(')', '').split(' ')

        pattern = tools.getAllIndexes(line, FENCE).join(',')
        const buttons = rest
        const joltage = buttons.pop()

        problems.push({
            pattern: pattern.split(",").map(x => parseInt(x))
            , buttons: buttons.map(x => x.split(",").map(y => parseInt(y)))
            , joltage
        });
    }

    config.problems = problems

    part1({ ...config });
    part2({ ...config });
}

const FENCE = '#'
const uniqueCombos = {}
main();