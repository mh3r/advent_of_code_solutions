import * as tools from '../tools.js';

let fileName;
let USELESS_VALVE_NUMBER = 0;
let VALVE_NUMBER = 0;

function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d16_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 1;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const valveMap = {};
    lines.forEach(line => {
        const splitLine = line.split(" ");

        const flow = Number(splitLine[4].replaceAll("rate=", "").replaceAll(";", ""));
        valveMap[splitLine[1]] = {
            // name: splitLine[1]
            flow: flow
            // , value: 0
            , valves: splitLine.slice(9).map(x => x.replaceAll(",", ""))
            // , isOpen: false
        }
    });


    process(valveMap);

}

function init(valveMap) {
    for (const [name, valve] of Object.entries(valveMap)) {
        VALVE_NUMBER++;
        if (valve.flow == 0) USELESS_VALVE_NUMBER++;
    }
}

function process(valveMap) {
    init(valveMap);

    const minute = 30;
    const current = "AA";
    const dest = "GG";



    let output = [];
    let previous = "";
    let openedOnes = [];
 
    const start  = new Date();
    pressureReleaseRec(valveMap, previous, current, minute, openedOnes, 0, output);
    tools.printJson(output);
    const endDate   = new Date();
    const seconds = (endDate.getTime() - start.getTime()) / 1000;
    tools.cprint( seconds);

    // let nextTargets = findValuableValves(current, minute, valveMap, openedOnes);

    // tools.printJson(nextTargets);

}

function pressureReleaseRec(valveMap, previous, current, minute, openedOnes, collection, output) {
    if (minute <= 1 || VALVE_NUMBER == USELESS_VALVE_NUMBER + openedOnes.length) {
        const max = (output.length == 0) ? collection : Math.max(collection, output[0]);
        output.length = 0;
        // tools.cprint(collection + " " + previous + " " + current);
        output.push(max);
        return;
    }
    const tmpOpenedOnes = openedOnes.slice();

    const value = openedOnes.includes(current) ? 0 : valveMap[current].flow * (minute - 1);
    if (value > 0) {
        tmpOpenedOnes.push(current);
        const tmpCollection = collection + value;
        pressureReleaseRec(valveMap, previous, current, minute - 1, tmpOpenedOnes, tmpCollection, output);
    } else {
        const nextTargets = findValuableValves(previous, current, minute, valveMap, tmpOpenedOnes);
        for (const target of nextTargets) {
            pressureReleaseRec(valveMap, current, target[0], minute - target[1], tmpOpenedOnes, collection, output);
        }
    }

    const max = (output.length == 0) ? collection : Math.max(collection, output[0]);
    output.length = 0;
    output.push(max);
}

function findValuableValves(previous, current, minute, valveMap, openedOnes) {
    let valuableValves = [];
    for (const [name, valve] of Object.entries(valveMap)) {
        if (valve.flow > 0 && !openedOnes.includes(name) && name != current && name != previous) {
            const distance = dist(current, name, valveMap);
            if (distance < minute - 1) {
                valuableValves.push([name, distance]);
            }
        }
    }

    return valuableValves;
}

function isThereMoar(current, minute, valveMap, openedOnes) {
    let retval = false;
    for (const [name, valve] of Object.entries(valveMap)) {
        if (valve.flow > 0 && !openedOnes.includes(name)) {
            if (dist(current, name, valveMap) < minute - 1) {
                retval = true;
                break;
            }
        }
    }
    return retval;
}

function isPathProfitable(from, destination, minute, valveMap, openedOnes = []) {
    const paths = [destination]
    let hasValue = false;
    const traversed = [from];
    while (paths.length > 0 && !hasValue) {
        const target = paths.shift();
        const distance = dist(from, target, valveMap);
        const value = openedOnes.includes(target) ? 0 : Math.max(minute - 1 - distance, 0) * valveMap[target].flow;
        if (value > 0) {
            hasValue = true;
            break;
        }
        traversed.push(target);
        let connectingValves = valveMap[target].valves.filter(x => !traversed.includes(x));
        paths.push(...connectingValves);
    }

    return hasValue;
}

function evaluateCurrentValue(flow, minute) {
    return Math.max(minute - 1, 0) * flow;
}

function dist(from, destination, valveMap) {
    let retval = 0;
    let queue = [[0, from]];
    let traversed = []

    if (from != destination) {
        while (queue.length > 0) {
            retval++;
            const item = queue.shift();
            traversed.push(item[1]);
            let connectingValves = valveMap[item[1]].valves;
            if (connectingValves.includes(destination)) {
                retval = item[0] + 1;
                break;
            }

            connectingValves = connectingValves.filter(x => !traversed.includes(x));
            connectingValves = connectingValves.map(x => [item[0] + 1, x]);
            queue.push(...connectingValves);
        }
    }

    return retval;
}



main();