import * as tools from '../tools.js';

let fileName;


function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d21_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    // business(lines);

     tools.cprint(3006709231504 + 960);
}

class Monkey {
    value = null;
    monkey1 = null;
    monkey2 = null;

    constructor(name, instruction) {
        this.name = name;
        this.instruction = instruction;
        const OPERATIONS = ["*", "-", "+", "/"];
        if (!OPERATIONS.some(x => instruction.includes(x))) {
            this.value = Number(instruction.split(":")[1]);
        } else {
            this.monkey1 = instruction.substring(6, 10);
            this.monkey2 = instruction.substring(13);
        }

        // if (this.name == "humn") {
        //     this.value = 0;
        // }
        // cgdh 43962603708340        
        // qhpl 19157252549620

        //      43962603717448
        //      19157252549620

    }

    processFunction(a, b) {
        if (a == null || b == null) return;

        if (this.instruction.includes("*")) {
            this.value = a * b;
        }

        if (this.instruction.includes("/")) {
            this.value = a / b;
        }

        if (this.instruction.includes("+")) {
            this.value = a + b;
        }

        if (this.instruction.includes("-")) {
            this.value = a - b;
        }
    }

    reverseAging(parent, other) {
        if (parent.instruction.includes("*")) {
            this.value = parent.value / other.value;
        }

        if (parent.instruction.includes("/")) {
            if (parent.monkey1 == this.name) {
                this.value = parent.value * other.value;
            } else {
                this.value = other.value / parent.value;
            }
        }

        if (parent.instruction.includes("+")) {
            this.value = parent.value - other.value;
        }

        if (parent.instruction.includes("-")) {
            if (parent.monkey1 == this.name) {
                this.value = parent.value + other.value;
            } else {
                this.value = other.value - parent.value;
            }
        }
    }

}




function business(input) {
    const target = "root";
    const monkeys = {};

    for (const line of input) {
        // const monkeyName = line.substring(0, 4);
        const name = line.substring(0, 4);
        monkeys[name] = new Monkey(name, line);
    }


    let i = 0;
    const monkeySet = new Set();

    monkeySet.add(target);
    let counter = 0;

    while (monkeySet.size > 0) {
        const monkeyNames = Array.from(monkeySet);
        const monkeyName = monkeyNames.shift();
        const realMonkey = monkeys[monkeyName];
        if (realMonkey.value == null) {

            const realMonkey1 = monkeys[realMonkey.monkey1];

            const realMonkey2 = monkeys[realMonkey.monkey2];

            realMonkey.processFunction(realMonkey1.value, realMonkey2.value);

            if (realMonkey.value != null) {
                continue;
            }

            if (realMonkey1.value == null) {
                monkeyNames.push(realMonkey1.name);
            }

            if (realMonkey2.value == null) {
                monkeyNames.push(realMonkey2.name);
            }

            monkeyNames.push(monkeyName);

            if (counter % 100000 == 0) tools.cprint("Counter ... " + counter);

            counter++;
        }
        monkeySet.clear();
        monkeyNames.forEach(item => monkeySet.add(item));

    }

    const targetMonkey = monkeys[target];
    const expectedValue = fileName.includes("test") ? 150 : 19157252549620;
    const actualValue = targetMonkey.value / 2;
       
    tools.cprint(actualValue);


    if (actualValue != expectedValue) {
        tools.cprint("Tried: " + monkeys["humn"].value);
        tools.cprint("Difference .. " + (expectedValue - actualValue));
    } else {
        tools.cprint("welp ... its correct?");
    }


    // tools.cprint(targetMonkey);
    // tools.cprint(monkeys[targetMonkey.monkey1].value);
    // tools.cprint(monkeys[targetMonkey.monkey2].value);



    const influencedMonkey = fileName.includes("test") ? "pppw" : "cgdh";
    const HUMN = "humn";

    let tmpTarget = HUMN;
    let humnHierarchy = [];

    while (tmpTarget != influencedMonkey) {
        humnHierarchy.unshift(tmpTarget);

        for (const [name, monkey] of Object.entries(monkeys)) {
            if (monkey.monkey1 == tmpTarget || monkey.monkey2 == tmpTarget) {
                tmpTarget = monkey.name;
                break;
            }
        }

    }
    humnHierarchy.unshift(influencedMonkey);
    // humnHierarchy.unshift("root");
    tools.cprint(humnHierarchy);

    resolveMonkeyAncestry(humnHierarchy, monkeys);

    const interestedParent = monkeys[humnHierarchy[humnHierarchy.length - 2]];
    const other = monkeys[findOtherMonkey(interestedParent, HUMN)];

    tools.printJson(interestedParent);
    tools.printJson(other);


}


function resolveMonkeyAncestry(humnHierarchy, monkeys) {
    monkeys[humnHierarchy[0]].value = monkeys[monkeys['root'].monkey2].value;

    for (let i = 0; i < humnHierarchy.length - 1; i++) {
        if (i == 0) continue;
        const tmpParent = monkeys[humnHierarchy[i - 1]];
        const current = monkeys[humnHierarchy[i]];

        current.reverseAging(tmpParent, monkeys[findOtherMonkey(tmpParent, current.name)]);

        let iaafafa = 0;

    }

}

function findOtherMonkey(parent, name) {
    return parent.monkey1 == name ? parent.monkey2 : parent.monkey1;
}

main();