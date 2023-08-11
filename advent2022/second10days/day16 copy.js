import * as tools from '../tools.js';

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d16_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 1;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const valveMap = [];
    lines.forEach(line => {
        const splitLine = line.split(" ");

        const flow = Number(splitLine[4].replaceAll("rate=", "").replaceAll(";", ""));
        valveMap.push({
            name: splitLine[1]
            , flow: flow
            , value: 0
            , valves: splitLine.slice(9).map(x => x.replaceAll(",", ""))
            , isOpen: false
        })
    });


    process(valveMap);

}


function process(valveMap) {

    // let distance = dist(findValve("AA", valveMap), findValve("FF", valveMap), valveMap);
    // tools.cprint(distance);

    let from = findValve("AA", valveMap);
    let dest = findValve("HH", valveMap);
    let minute = 30;
    let value = evaluateValue(from, dest, minute, valveMap);
    tools.cprint(value)

    // let tmpValveMap = valveMap.filter(x => (!x.isOpen && x.flow > 0));


    tools.printJson(valveMap);

}

function pressureReleaseRec(valveMap, from, currentValve, output) {



}


function evaluateValuePathRec(from, destination, minute, valveMap, output) {

    if (destination. )
    const connectingValves = destination.valves.filter(x => x != from);

    for (const targetValve of connectingValves){

    }


}

function evaluateValue(from, destination, minute, valveMap) {
    const distance = dist(from, destination, valveMap);
    return Math.max(minute - distance - 1, 0) * destination.flow;
}

function evalutateCurrentValue(current, minute) {
    return Math.max(minute - 1, 0) * current.flow;
}

function findValve(target, valveMap) {
    let retval = null;
    for (const valve of valveMap)
        if (valve.name == target) {
            retval = valve;
            break;
        };
    return retval;
}

function dist(from, destination, valveMap) {
    let retval = 0;
    let queue = [[0, from]];
    let traversed = []

    if (from.name != destination.name) {
        while (queue.length > 0) {
            retval++;
            const item = queue.shift();
            traversed.push(item[1].name);
            let connectingValves = item[1].valves;
            if (connectingValves.includes(destination.name)) {
                retval = item[0] + 1;
                break;
            }

            connectingValves = connectingValves.filter(x => !traversed.includes(x));
            connectingValves = connectingValves.map(x => findValve(x, valveMap));
            connectingValves = connectingValves.map(x => [item[0] + 1, x]);
            queue.push(...connectingValves);
        }
    }

    return retval;
}

function distNameOnly(from, destination, valveMap) {
    let retval = 0;
    let queue = [[0, from]];
    let traversed = []

    if (from != destination && valveMap.filter(x => x.name == destination).length == 1) {
        while (queue.length > 0) {
            retval++;
            const item = queue.shift();
            traversed.push(item[1]);
            let connectingValves = valveMap.filter(x => x.name == item[1])[0].valves;
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