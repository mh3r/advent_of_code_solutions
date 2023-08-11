import * as tools from '../tools.js';

const FIVE = 5;
let fileName;
function main() {
    let array = [];

    fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d25_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    let total = 0
    lines.forEach(line => {
        total += snafuToDecimal(line);
        // tools.cprint(total);
    });

    let snafu = backToSnafu(total);


    if (fileName.includes("test")) {
        if (snafu == "2=-1=0") {
            tools.cprint("YAY!!!")
        } else {
            tools.cprint("Booooooooooo");
        }
    }

}

function snafuToDecimal(data) {
    let retval = 0;
    const length = data.length;
    let quant;

    for (let i = 0; i < length; i++) {
        const char = data[i];

        const power = five(data.length - 1 - i);
        if (char == "=") {
            quant = -2;
        } else if (char == "-") {
            quant = -1;
        } else {
            quant = Number(char);
        }
        retval += quant * power;
    }
    return retval;
}

function backToSnafu(data) {
    let retval = "";
    // data = 198

    const power = geigerCounter(data);
 

    for (let i = power; i >= 0; i--) {
        let quant = ringarde(data, i);
        data = quant[1];
        retval += quant[0];
    }

    tools.cprint(retval);
    return retval;

}

function geigerCounter(data) {
    let biggestPower = 0;
    let found = false;
    while (!found) {
        if (data < five(biggestPower)) {
            break;
        }
        biggestPower++;
    }
    biggestPower--;
    return (data > 2 * five(biggestPower)) ? biggestPower + 1 : biggestPower;
}


function five(quant) {
    return FIVE ** quant;
}

function ringarde(data, power) {
    let retval = "";
    let remainder = 0;
    const dataAbs = Math.abs(data);
    if (data == 0 || dataAbs <= 2 * five(power - 1)) return ["0", data];

    if (data > 0) {
        if (data >= five(power) - 2 * five(power - 1) && data <= five(power) + 2 * five(power - 1)) {
            remainder = data - five(power);
            retval = "1";
        } else {
            remainder = data - 2 * five(power);
            retval = "2";
        }
    } else {
        if (dataAbs >= five(power) - 2 * five(power - 1) && dataAbs <= five(power) + 2 * five(power - 1)) {
            remainder = data + five(power);
            retval = "-";
        } else {
            remainder = data + 2 * five(power);
            retval = "=";
        }
    }

    return [retval, remainder];
}


main();