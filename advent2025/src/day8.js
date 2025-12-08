import * as tools from '../../js-util/tools.js';

const YEAR = 2025;

function part1(config) {
    let answer = 0;
    const correctAnswer = 97384


    const junctions = []

    for (const line of config.raw) {
        junctions.push(new Junction(line))
    }

    for (const junction of junctions) {
        const name = junction.name
        const otherJunctions = junctions.filter(x => x.name != name)
        junction.populateDistances(otherJunctions)
    }


    let circuits = connectCircuits(junctions)
    circuits = assimilateCircuits(circuits)

    const circuitLengths = circuits.map(x => x.length)
    circuitLengths.sort((a, b) => b - a)

    answer = 1
    for (let i = 0; i < 3; i++) {
        answer *= circuitLengths[i]
    }

    console.log(`Part 1: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}


function assimilateCircuits(circuits) {
    let retval = [...circuits]

    let junctions = []
    retval.map(x => junctions.push(...x))

    let duplicates = findDuplicates(junctions)

    while (duplicates.length > 0) {
        let junction = duplicates.pop()

        let indexesToMerge = []

        for (let i = 0; i < retval.length; i++) {
            if (retval[i].includes(junction)) {
                indexesToMerge.push(i)
            }
        }

        const indexElements1 = [...retval[indexesToMerge[0]]]
        const indexElements2 = [...retval[indexesToMerge[1]]]

        retval[indexesToMerge[0]].length = 0
        retval[indexesToMerge[0]].push(...[...new Set([...indexElements1, ...indexElements2])])

        retval.splice(indexesToMerge[1], 1)

        junctions = []
        retval.map(x => junctions.push(...x))
        duplicates = findDuplicates(junctions)
    }

    return retval

}

function findDuplicates(arr) {
    return arr.filter((element, index) => {
        return arr.indexOf(element) !== index;
    });
};

function connectCircuits(junctions, repetition = 1000) {
    let currentMinRange = 0;
    let circuits = []

    const alreadyConnected = new Set()
    for (let i = 0; i < repetition; i++) {
        const mins = []

        // const filteredJunctions = junctions.filter(x => !alreadyConnected.has(x))

        for (const junction of junctions) {
            let closestJunctionTmp = junction.findNextClosestJunction(currentMinRange)
            if (closestJunctionTmp !== null) {
                closestJunctionTmp.from = junction.name
                mins.push(closestJunctionTmp)
            }
        }

        mins.sort((a, b) => a.distance - b.distance)

        if (mins.length > 0) {
            const key1 = mins[0].key
            const key2 = mins[0].from
            alreadyConnected.add(key1)
            alreadyConnected.add(key2)
            currentMinRange = mins[0].distance

            const tmpCircuits = []
            let isExistingCircuit = false
            for (let circuit of circuits) {

                if (circuit.includes(key1) || circuit.includes(key2)) {
                    circuit.push(key1, key2)
                    isExistingCircuit = true
                }
                tmpCircuits.push([...new Set(circuit)])
            }
            if (!isExistingCircuit) {
                tmpCircuits.push([key1, key2])
            }
            circuits = tmpCircuits

        }
        // console.log(mins)
    }
    return circuits
}




function part2(config) {
    let answer = 0;
    const correctAnswer = undefined

    console.log(`Part 2: ${answer}`)
    console.assert(correctAnswer === answer, `${answer} should have been ${correctAnswer}`);
}

function main() {
    const baseDir = `${process.cwd()}\\advent${YEAR}`;
    const dataDir = `${baseDir}\\data`;

    let inputFile = `${dataDir}\\d8_input.txt`;
    // inputFile = `${baseDir}\\data\\test.txt`;

    console.log("Input File: " + inputFile);
    const lines = tools.readFileFromLocal(inputFile).split(/\r?\n/).filter(x => x);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const config = {
        raw: lines
    }


    part1({ ...config });
    part2({ ...config });
}

class Junction {
    distances = {}
    constructor(input) {
        this.name = input
        const splitted = input.split(",");
        this.x = parseInt(splitted[0])
        this.y = parseInt(splitted[1])
        this.z = parseInt(splitted[2])

    }

    populateDistances(junctions) {
        for (const junction of junctions) {
            const dx = this.x - junction.x
            const dy = this.y - junction.y
            const dz = this.z - junction.z
            this.distances[junction.name] = Math.sqrt(dx * dx + dy * dy + dz * dz)
        }
    }

    findNextClosestJunction(minDistance) {
        let retval = null
        let tmpMinDistance = Infinity
        for (const key of Object.keys(this.distances)) {
            const distance = this.distances[key]

            if (distance < tmpMinDistance && distance > minDistance) {
                tmpMinDistance = distance
                retval = { key, distance }
            }
        }
        return retval;
    }

}

main();