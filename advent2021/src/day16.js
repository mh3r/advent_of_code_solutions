import { publicDecrypt } from 'crypto';
import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;
const LITERAL = "literal";
const OPERATION = "operation";

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d16_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();



    lines.forEach(line => {

    });


    let input = convertInitialHex(lines[0]);
    let output = [];
    processRec(input, output, 0);

    tools.printJson(output);

    let total = 0;
    output.forEach(x => total += x.version);


    tools.cprint(total);
    let debug = 1;

}

function processRec(originalInput, output, depth) {
    const nextDepth = depth + 1;
    let hexString = originalInput;
    let leftOver = "";

    let left = hexString.substring(0, 3);
    hexString = hexString.substring(left.length);
    const version = parseInt(left, 2);
    left = hexString.substring(0, 3);
    hexString = hexString.substring(left.length);
    const type = parseInt(left, 2);

    let typeMode;
    let value = 0;
    if (type == 4) {
        typeMode = LITERAL;
        let tmp = "";
        let isContinue = true;
        while (isContinue) {
            if ("0" == hexString.substring(0, 1)) {
                isContinue = false;
            }

            hexString = hexString.substring(1);
            tmp += hexString.substring(0, 4);
            hexString = hexString.substring(4);
        }
        value = parseInt(tmp, 2);
    } else {
        typeMode = OPERATION;
        left = hexString.substring(0, 1);
        hexString = hexString.substring(left.length);
        const mode = left;
        const infernalAffairs = [];
        if (mode == "0") {
            left = hexString.substring(0, 15);
            hexString = hexString.substring(left.length);
            const length = parseInt(left, 2);

            let total = 0;

            while (total < length) {
                let result = processRec(hexString, output, nextDepth);
                infernalAffairs.push(result);
                hexString = result.leftOver;
                total += result.size;
            }
        } else {
            left = hexString.substring(0, 11);
            hexString = hexString.substring(left.length);
            const length = parseInt(left, 2);

            for (let i = 0; i < length; i++) {
                let result = processRec(hexString, output, nextDepth);
                infernalAffairs.push(result);
                hexString = result.leftOver;
            }
        }

        // set value for each operations 
        let tmpValues = [];
        for (const affair of infernalAffairs) {
            tmpValues.push(affair.value);
        }

        switch (type) {
            case 0:
                value = tmpValues.reduce((a, b) => a + b, 0);
                break;
            case 1:
                value = tmpValues.reduce((a, b) => a * b, 1);
                break;
            case 2:
                value = Math.min(...tmpValues);
                break;
            case 3:
                value = Math.max(...tmpValues);
                break;

            case 5:
                value = tmpValues[0] > tmpValues[1] ? 1 : 0;
                break;

            case 6:
                value = tmpValues[0] < tmpValues[1] ? 1 : 0;
                break;
            case 7:
                value = tmpValues[0] == tmpValues[1] ? 1 : 0;
                break;
        }
    }

    leftOver = hexString;

    const retval = {
        version
        , type
        , typeMode
        , value
        , leftOver
        , size: originalInput.length - hexString.length
        , depth
    };

    output.push(retval);
    return retval;

}

function convertInitialHex(input) {
    let retval = "";

    for (const char of input) {
        retval += hex2bin(char);
    }
    return retval;
}

function hex2bin(hex) {
    return ("0000" + (parseInt(hex, 16)).toString(2)).substr(-4);
}

main();