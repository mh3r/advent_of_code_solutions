import * as tools from '../../js-util/tools.js';

const YEAR = 2019;
const baseDir = `${process.cwd()}\\advent${YEAR}`;
const dataDir = `${baseDir}\\data`;

const SEPARATOR = ")"
const COM = "COM"
const YOU = "YOU"
const SANTA = "SAN"

function part1(distanceMap) {
    let answer = 0;
    const finalAnswer = 144909

    answer = Object.values(distanceMap).reduce((acc, value) => acc + value, 0)

    console.log(`Part 1: ${answer}`)
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function part2(orbitMap, distanceMap) {
    let answer = 0;
    const finalAnswer = 259

    const commonAncestor = findCommonAncestor(orbitMap, YOU, SANTA, distanceMap)
    answer = distanceMap[YOU] + distanceMap[SANTA] - distanceMap[commonAncestor] * 2 - 2
    // tools.printJson(distanceMap)
    // console.log(commonAncestor)

    console.log(`Part 2: ${answer}`)
    console.assert(finalAnswer === answer, `${answer} should have been ${finalAnswer}`);
}

function calculateDistances(orbitMap, unique) {
    const distanceMap = {}
    distanceMap[COM] = 0
    for (const key of unique) {
        calculateDistanceCurry(orbitMap, key, distanceMap)
    }
    return distanceMap
}

function calculateDistanceCurry(orbitMap, object, distanceMap) {
    if (Object.keys(distanceMap).includes(object)) return

    const parent = getOrbitParent(orbitMap, object)
    if (!Object.keys(distanceMap).includes(parent)) {
        calculateDistanceCurry(orbitMap, parent, distanceMap)
    }

    for (const kid of Object.values(orbitMap[parent])) {
        distanceMap[kid] = distanceMap[parent] + 1
    }
}

function getOrbitParent(orbitMap, target) {
    if (COM === target) return null
    return Object.entries(orbitMap).filter(([key, value]) => value.includes(target))[0][0]
}

function findCommonAncestor(orbitMap, a, b, distanceMap) {
    const distA = distanceMap[a]
    const distB = distanceMap[b]
    const ancestries = {
        [a]: [a]
        , [b]: [b]
    }

    while (true) {
        const isActorA = distA - ancestries[a].length > distB - ancestries[b].length

        const actor = isActorA ? a : b
        const opponent = !isActorA ? a : b
        const parent = getOrbitParent(orbitMap, ancestries[actor].at(-1))

        if (ancestries[opponent].includes(parent)) {
            return parent
        }
        ancestries[actor].push(parent)
    }
}

function mapOrbit(input) {

    const orbitMap = {}
    const unique = new Set()
    for (const line of input) {

        const [key, value] = line.split(SEPARATOR)
        unique.add(key)
        unique.add(value)
        if (Object.keys(orbitMap).includes(key)) {
            orbitMap[key].push(value)
        } else {
            orbitMap[key] = [value]
        }

    }
    return [orbitMap, unique]
}

function main() {
    let inputFile = `${dataDir}\\d6_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const [orbitMap, unique] = mapOrbit(lines)
    const distanceMap = calculateDistances(orbitMap, unique)

    part1(distanceMap);
    part2(orbitMap, distanceMap);
}

main();


