import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d10_input.txt";

    console.log("File: " + fileName);
    let counter = 1;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    let cycle = 1;
    let value = 1;
    const instructions = [];
    const history = [];

    let lineCounter = 0;

    const maxCycle = lines.filter(x => x.includes("noop")).length + lines.filter(x => x.includes("addx")).length * 2 + 1;
    // console.log(maxCycle)

    let noAction = 0;
    let line = null;
    for (let i = 0; i < maxCycle; i++) {

        if (noAction <= 0) {
            line = lines[lineCounter];
            lineCounter++;


            if (line != null && line.startsWith("addx")) {
                instructions.push(cycle + 2)
                instructions.push(Number(line.split(" ")[1]));
                // console.log(instructions)
                noAction = 2;
            }

        }

        if (instructions.length > 0 && instructions[0] == cycle) {
            value += instructions[1];
            instructions.shift();
            instructions.shift();
        }

        history.push([cycle, value]);

        noAction--;
        cycle++;
    };

    // history.forEach(([x, y]) =>
    //     console.log(x + " --> " + y)
    // );

    // 20th, 60th, 100th, 140th, 180t, 220
    //     const interestedCycles = [20, 60, 100, 140, 180, 220];

    //     let strengthCounter = 0;
    //     interestedCycles.forEach(x => {
    //         strengthCounter += x * history[x][1];
    //     })

    //    tools. print(strengthCounter);

    // tools.cprint(history.length)

    printScreen(history);



}

function printScreen(history) {

    // history.slice(0, 40).forEach(([x, y]) => {
    //     console.log(x + " --> " + y);
    // }
    // );

    let screen = Array(240).fill(" ");

    for (let pixel = 0; pixel < history.length; pixel++) {
        if (Math.abs(history[pixel][1] - pixel % 40) <= 1) {
            // tools.cprint("at pixel " + pixel + "    " + Math.abs(history[pixel][1] - pixel % 40))

            screen[pixel] = '#';
        }
    }

    let line = "";

    while (screen.length > 0) {
        line = screen.slice(0, 40).join("");
        screen = screen.slice(40)
        tools.cprint(line)
    }

}


main();