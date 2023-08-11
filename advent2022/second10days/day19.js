import * as tools from '../tools.js';

const ORE = 0;
const CLAY = 1;
const OBS = 2;
const GEO = 3;

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d19_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    const rawLines = [];
    lines.forEach(line => {
        line = line.replaceAll("Blueprint ", "").replaceAll(": Each ore robot costs ", ",")
            .replaceAll(" ore. Each clay robot costs ", ",")
            .replaceAll(" ore. Each obsidian robot costs ", ",")
            .replaceAll(" ore and ", ",")
            .replaceAll(" clay. Each geode robot costs ", ",")
            .replaceAll(" obsidian.", "")

        // tools.cprint(line);
        rawLines.push(line.split(",").map(x => Number(x)))
    });

    // start(rawLines);

    tools.cprint( 9 * 25* 12);

}

class Factory {
    constructor(x) {
        this.id = x[0];
        this.oreReq = [x[1], 0, 0];
        this.clayReq = [x[2], 0, 0];
        this.obsReq = [x[3], x[4], 0];
        this.geodeReq = [x[5], 0, x[6]];
        this.maxOre = Math.max(x[1], x[2], x[3], x[5]);
        this.maxClay = Math.max(0, x[4]);
        this.maxObs = Math.max(0, x[6]);
    }

    canBuild(resources, type) {
        let comparison = this.getType(type);
        return (resources[0] >= comparison[0]
            && resources[1] >= comparison[1]
            && resources[2] >= comparison[2]);
    }

    getType(type) {
        let retval;
        switch (type) {
            case ORE:
                retval = this.oreReq;
                break;
            case CLAY:
                retval = this.clayReq;
                break;
            case OBS:
                retval = this.obsReq;
                break;
            default:
                retval = this.geodeReq;
        }
        return retval;
    }

    buildRobot(resources, type) {
        let comparison = this.getType(type)
        resources[0] = resources[0] - comparison[0];
        resources[1] = resources[1] - comparison[1];
        resources[2] = resources[2] - comparison[2];
    }

    waitAbout(resources, robots, type) {
        let retval = -1;
        let comparison = this.getType(type);

        let maxAmount = Math.max(comparison[0], comparison[1], comparison[2]);

        let [ore, clay, obs] = resources;
        for (let i = 0; i <= maxAmount; i++) {
            if (this.canBuild([ore, clay, obs], type)) {
                retval = i;
                break;
            }
            ore = ore + robots[0];
            clay = clay + robots[1];
            obs = obs + robots[2];
        }
        return retval;
    }

}

function start(rawLines) {
    const bluePrints = []
    rawLines.forEach(x => {
        let blueprint = new Factory(x)
        bluePrints.push(blueprint);
    }
    )

    const result = [];
    for (const factory of bluePrints) {
        const resources = [0, 0, 0, 0];
        const robots = [1, 0, 0, 0];
        // const minutes = 24;
        const minutes = 32;

        const output = [];
        const instructions = null;
        const start = new Date();
        mineRec(resources, robots, instructions, minutes, factory, output);
        // tools.printJson(output);
        const endDate = new Date();
        const seconds = (endDate.getTime() - start.getTime()) / 1000;
        tools.cprint(seconds + " seconds");
        result.push(output[0]);
    }



    tools.printJson(result);

    let total = 0;
    for (let i = 0; i < result.length; i++) {
        if (result[i] != null) {
            total += (i + 1) * result[i];
        }
    }

    tools.printJson(total);


    /*
    test file 
    Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
    Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
    
    */




}

function mineRec(resources, robots, instruction, minutes, factory, output) {
    let stillHaveTime = false;
    if (minutes <= 0) {
        if (output.length == 0) {
            output.push(resources[3]);
        } else {
            const max = Math.max(resources[3], output.shift());
            output.push(max);
        }
        return;
    }

    if (minutes == 22 && robots[1] == 0) {
        let debugPoint = 0;
    }

    const resourcesCopy = resources.slice();
    const robotsCopy = robots.slice();
    if (instruction != null) {
        minutes--;
        resourcesCopy[0] += robotsCopy[0];
        resourcesCopy[1] += robotsCopy[1];
        resourcesCopy[2] += robotsCopy[2];
        resourcesCopy[3] += robotsCopy[3];
        factory.buildRobot(resourcesCopy, instruction);

        robotsCopy[instruction]++;

    }

    const nextTimeSequence = [ORE, CLAY, OBS, GEO].map(x => factory.waitAbout(resourcesCopy, robotsCopy, x));

    // put arbitrary rule
    if (robotsCopy[0] > factory.maxOre) nextTimeSequence[0] = -1;
    if (robotsCopy[1] > factory.maxClay) nextTimeSequence[1] = -1;
    if (robotsCopy[2] > factory.maxObs) nextTimeSequence[2] = -1;

    for (let i = 0; i < nextTimeSequence.length; i++) {
        const wait = nextTimeSequence[i];
        if (wait >= 0 && minutes > wait) {
            const tmpResources = resourcesCopy.slice();
            stillHaveTime = true;

            tmpResources[0] += wait * robotsCopy[0];
            tmpResources[1] += wait * robotsCopy[1];
            tmpResources[2] += wait * robotsCopy[2];
            tmpResources[3] += wait * robotsCopy[3];

            mineRec(tmpResources, robotsCopy, i, minutes - wait, factory, output);
        }
    }

    if (!stillHaveTime) {
        if (robotsCopy[3] > 0) {
            const geoMined = resourcesCopy[3] + (minutes * robotsCopy[3]);
            if (output.length == 0) {
                output.push(geoMined);
            } else {
                const max = Math.max(geoMined, output.shift());
                output.push(max);
            }
        }
    }

}



main();