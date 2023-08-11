import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;
const LEFT = "L";
const RIGHT = "R";
const ROOT = "r00t";

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    // fileName = "D:/aoc/advent2021/data/d18_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();


    const input = [];
    lines.forEach(line => {
        input.push(eval(line));
    });


    let testinput = [[[[[9, 8], 1], 2], 3], 4];

    let test = new Pair(testinput);

    let test2 = test.l.l.l;
    tools.printJson(test2.findNext(LEFT).getValue());

    let debug = 1;

    tools.printJson(test.getValue());


}



class Value {
    constructor(input) {
        this.value = input;
    }

    getValue() {
        return this.value;
    }
}

class Pair {

    constructor(input, parent = null, depth = 0, position = ROOT) {
        const left = input[0];
        const right = input[1];

        this.origin = position;
        this.input = input
        this.l = Array.isArray(left) ? new Pair(left, this, depth + 1, LEFT) : new Value(left);
        this.r = Array.isArray(right) ? new Pair(right, this, depth + 1, RIGHT) : new Value(right);
        this.depth = depth;
        this.parent = parent;
    }


    getValue() {
        return [this.l.getValue(), this.r.getValue()];
    }


    findNext(wantedOrigin) {
        let retval = null;
        const rOrigin = this.reverseOrigin(wantedOrigin);

        let firstParent = this.findFirstPairOfOrigin(rOrigin);

        if (firstParent != null) {
            let branch = firstParent.getChild(wantedOrigin);
            retval = this.findFirstValueOfOrigin(branch, rOrigin);
        }

        return retval;
    }

    findFirstValueOfOrigin(object, origin) {
        let retval = null;

        if (object instanceof Value) {
            retval = object;
        } else {
            let tmp = object.getChild(origin);
            while (true) {
                if (tmp instanceof Value) {
                    retval = tmp;
                    break;
                }
                tmp = tmp.getChild(origin);
            }
        }

        return retval;
    }

    getChild(origin) {
        return origin == LEFT ? this.l : this.r;
    }

    findFirstPairOfOrigin(wantedOrigin) {
        let retval = null;
        const rOrigin = this.reverseOrigin(wantedOrigin);
        let isContinue = true;
        let parent = this.parent;

        if (this.origin == wantedOrigin) {
            retval = this.parent;
        } else {
            while (isContinue) {
                if (parent.origin == wantedOrigin) {
                    retval = parent;
                    isContinue = false;
                    continue;
                }
                if (parent.origin == ROOT) {
                    isContinue = false;
                    continue;
                }
                if (parent.origin == rOrigin) {
                    parent = parent.parent;
                    continue;
                }
            }
        }
        return retval;
    }

    reverseOrigin(origin) {
        return origin == LEFT ? RIGHT : LEFT;
    }


    explode() {
        let retval = false;

        let queue = [];



        return retval;
    }

    process() {

        // step 1
        // find anything that can explode
        // explode
        // if explodes; redo step one 

        // split 
        // redo step 1


    }


}

main();