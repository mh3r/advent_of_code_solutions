import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function findSmallestPossibilities(problem){
    const {pattern, buttons}  = problem;

    let debug = 1 


}


function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;
    
    let inputFile = `${dataDir}\\d10_input.txt`;
    inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }

    const problems = []

// [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    for (let line of lines) {
        line = line.replaceAll('[','')
        const firstSplit = line.split(']')
        let pattern = firstSplit[0]
        const rest = firstSplit[1].trim().replaceAll('(','').replaceAll(')','').split(' ')

        console.log(tools.getAllIndexes(line, '#'))
        pattern=tools.getAllIndexes(line, '#').join(',')
        const buttons = rest
        const joltage  = buttons.pop()

        problems.push({pattern : pattern.split(",").map(x=>parseInt(x))
            , buttons : buttons.map(x=>x.split(",").map(y=>parseInt(y)))
            , joltage});
    }

    config.problems = problems


    findSmallestPossibilities(config.problems[0])

    part1({ ...config });
    part2({ ...config });




}

const FENCE = '#'
main();