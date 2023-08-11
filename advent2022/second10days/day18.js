import * as tools from '../tools.js';

let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d18_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");



    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    let counter = countSides(lines);

    tools.cprint(counter);

}

function countSides(lines) {
    let retval = 0
    lines.forEach(line => {

        const splitted = line.split(",");
        const x = Number(splitted[0]);
        const y = Number(splitted[1]);
        const z = Number(splitted[2]);

        if (x == 0) retval++;
        else if (!lines.includes(`${x - 1},${y},${z}`)) {
            retval++;
        }

        if (!lines.includes(`${x + 1},${y},${z}`)) {
            retval++;
        }


        if (y == 0) retval++;
        else if (!lines.includes(`${x},${y - 1},${z}`)) {
            retval++;
        }

        if (!lines.includes(`${x},${y + 1},${z}`)) {
            retval++;
        }


        if (z == 0) retval++;
        else if (!lines.includes(`${x},${y},${z - 1}`)) {
            retval++;
        }

        if (!lines.includes(`${x},${y},${z + 1}`)) {
            retval++;
        }

    });
    return retval;
}



main();