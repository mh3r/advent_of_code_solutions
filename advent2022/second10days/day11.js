import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d11_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");
    let repetition = 20;

    const lines = tools.readFileFromLocal(fileName)

    let monkeys = [];

    monkeyParser(lines, monkeys);


    const commonModulus = (monkeys.reduce(
        (accumulator, currentValue) => accumulator * currentValue.divisibleBy,
        1
    ));

    for (let monkey of monkeys) {
        monkey.commonModulus = commonModulus;
    }

    // tools.printJson(monkeys);
    let round = 1;
    Array.from(Array(repetition)).forEach(() => {
        for (let monkey of monkeys) {
            monkey.process(monkeys)
        }
        let i = 0;

        round++;
    }
    )

    monkeys.sort((a, b) => b.processCounter - a.processCounter);

    let firstTwo = 2;
    let product = 1;
    for (const monkey of monkeys) {
        if (firstTwo > 0) product *= monkey.processCounter;
        firstTwo--;
        tools.cprint(monkey.processCounter);
        tools.cprint(monkey.items)
    }

    tools.cprint("Product: " + product);

    // tools.printJson(monkeys);

    // wrong ... 32397120063 your answer is too high.
    // try  32395860120 failed 
    // 32396400099 also wrong 
}



class Monkey {
    processCounter = 0;
    commonModulus;

    constructor(id, items, operation, test, pass, fail, divisibleBy) {
        this.id = id;
        this.items = items;
        this.operation = operation;
        this.test = test;
        this.pass = pass;
        this.fail = fail;
        this.divisibleBy = divisibleBy;
    }

    process(monkeys) {
        while (this.items.length > 0) {
            const item = this.items.shift();
            let value = this.operation(item);
            value = value % this.commonModulus;
            value = Math.floor(value / 3);
            const passingTo = this.test(value) ? this.pass : this.fail;
            this.processCounter++;
            monkeys[passingTo].items.push(value);
        }
    }
}


function monkeyParser(lines, monkeys) {
    for (const monkeyLines of (lines.split("\r\n\r\n"))) {
        let monkey;
        let items;
        let operation;
        let test;
        let pass;
        let fail;
        let id;
        let divisibleBy;
        for (const line of monkeyLines.split("\n")) {

            if (line.startsWith("Monkey")) {
                id = Number(line.replaceAll(":", "").split(" ")[1]);
            }

            if (line.includes("Starting")) {
                items = line.replaceAll("  Starting items: ", "").split(",").map(x => Number(x));
            }

            if (line.includes("Operation")) {
                let op = line.replaceAll("  Operation: new = ", "").replaceAll("\r", "").replaceAll("\n", "");
                let opSplit = op.split(" ");

                if (opSplit[1] == "+") {
                    operation = function (old) { return old + Number(opSplit[2]) };
                } else if (opSplit[1] == "*") {
                    if (opSplit[2] == "old") {
                        operation = function (old) { return old * old };
                    } else {
                        operation = function (old) { return old * Number(opSplit[2]) };
                    }
                }

            }

            if (line.includes("Test")) {
                const splits = line.split(" ");
                divisibleBy = Number(splits[splits.length - 1]);
                test = function (x) { return (x % divisibleBy == 0) };
            }

            if (line.includes("true")) {
                pass = Number(line.replaceAll("\r", "").replaceAll("\n", "").slice(-1));
            }

            if (line.includes("false")) {
                fail = Number(line.slice(-1));
                monkey = new Monkey(id, items, operation, test, pass, fail, divisibleBy);
                monkeys.push(monkey);
            }
        }
    }

}

main();