import * as tools from '../../js-util/tools.js';

const YEAR = 2025;
const SPLITTER = "^"


function part1(config) {
    let answer = 0;
    const correctAnswer = 1642
    const totalLength = config.data.length
    let currentBeams = [config.startIndex]

    for (let i = 0; i < totalLength; i++) {
        let newBeams = []
        if (i + 1 < totalLength) {
            const nextLine = config.data[i + 1];
            for (const beam of currentBeams) {

                if (nextLine[beam] === SPLITTER) {
                    answer += 1
                    newBeams.push(beam - 1)
                    newBeams.push(beam + 1)
                } else {
                    newBeams.push(beam)
                }
            }
            currentBeams = [...new Set(newBeams)]
        }
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = 47274292756692
    const totalLength = config.data.length

    let noOfPossibleVisitMap = {}
    noOfPossibleVisitMap[`0-${config.startIndex}`] = 1


    for (let i = 1; i < totalLength; i++) {
        const line = config.data[i];
        const lastNumbers = Object.keys(noOfPossibleVisitMap).filter(x => x.startsWith(`${i - 1}-`)).map(x => { return x.split("-")[1] }).map(Number)

        for (const lastNumber of lastNumbers) {
            const parentTotal = noOfPossibleVisitMap[`${i - 1}-${lastNumber.toString()}`]
            const records = (line[lastNumber] === SPLITTER) ? [lastNumber - 1, lastNumber + 1] : [lastNumber]

            for (const record of records) {

                const key = `${i}-${record}`

                if (Object.keys(noOfPossibleVisitMap).includes(key)) {
                    noOfPossibleVisitMap[key] += parentTotal
                } else {
                    noOfPossibleVisitMap[key] = parentTotal
                }
            }
        }
    }

    const lastLevels = Object.keys(noOfPossibleVisitMap).filter(x => x.startsWith(`${totalLength - 1}-`))

    for (const lastLevel of lastLevels) {
        answer += noOfPossibleVisitMap[lastLevel]
    }

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}




function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d7_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const startIndex = lines[0].indexOf("S")
    config.startIndex = startIndex
    const data = []
    for (let i = 0; i < lines.length; i += 2) {
        data.push(lines[i])
    }
    config.data = data


    part1({ ...config });
    part2({ ...config });
}


main();