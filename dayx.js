import * as tools from '../tools.js';

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    // fileName = "D:/advent2022/data/d21_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    lines.forEach(line => {


    });
    tools.cprint(counter);
}



main();