import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
    let array = [];

    fileName = "advent2021/data/test.txt";
    fileName = "D:/aoc/advent2021/data/d8_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");

    const isTest = fileName.includes("test");

    let counter = 0;
    const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
    if (lines[lines.length - 1].length == 0) lines.pop();

    let test = ` 
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
`
    const displays = [];
    lines.forEach(line => {
        displays.push(new DigitalDisplay(line));
    });

    // tools.printJson(displays);

    process(displays);
}

class DigitalDisplay {
    constructor(line) {
        const splitted = line.split(" | ");
        const numbers = splitted[0].split(" ");
        const outputNumbers = splitted[1].split(" ");
        this.rawData = [];
        this.outputs = [];
        this.decodedOutputs = [];
        this.mapping = {};

        for (const char of numbers) {
            const tmp = [...char].sort();
            this.rawData.push(tmp.join(""));
        }
        this.createMapping();

        for (const char of outputNumbers) {
            const tmp = [...char].sort();
            const key = tmp.join("")
            this.outputs.push(key);
            this.decodedOutputs.push(this.mapping[key]);
        }
    }

    createMapping() {

        let key = this.rawData.filter(x => x.length == 2)[0];
        const one = key;
        this.mapping[key] = "1";

        key = this.rawData.filter(x => x.length == 3)[0];
        this.mapping[key] = "7";

        key = this.rawData.filter(x => x.length == 4)[0];
        const four = key;
        this.mapping[key] = "4";

        key = this.rawData.filter(x => x.length == 7)[0];
        this.mapping[key] = "8";

        let sixes = this.rawData.filter(x => x.length == 6);
        let fives = this.rawData.filter(x => x.length == 5);

        // 0, 6, 9
        // compare 1 and 4 to get b, d 
        // compare 0, 6, 9 all but one must have b, d 
        // compare the rest with 1 

        // find BD Wong 
        let bd = [];

        for (const char of four) {
            if (!one.includes(char)) {
                bd.push(char);
            }
        }

        let zero;
        for (const six of sixes) {
            if (!bd.every(x => six.includes(x))) {
                zero = six;
            }
        }
        this.mapping[zero] = "0";

        sixes = sixes.filter(x => x != zero);

        let nine;
        for (const six of sixes) {
            if (one.split("").every(x => six.includes(x))) {
                nine = six;
            }
        }

        this.mapping[nine] = "9";

        let six = sixes.filter(x => x != nine)[0];
        this.mapping[six] = "6";

        // 2, 3, 5
        // to get 3, compare 2,3,5 against 1 
        // compare 5 and 6 

        let three;
        let five;
        for (const five_ of fives) {
            if (one.split("").every(x => five_.includes(x))) {
                this.mapping[five_] = "3";
                three = five_;
            }

            if (five_.split("").every(x => six.includes(x))) {
                five = five_;
                this.mapping[five] = "5";
            }

        }

        let two = fives.filter(x => x != three).filter(x => x != five)[0];
        this.mapping[two] = "2";

        let debug = 1;
    }
}

function process(displays) {
    let total = 0;
    let superTotal = 0;

    const interestedNumbers = ["1", "4", "7", "8"];

    for (const display of displays) {

        for (const decoded of display.decodedOutputs) {
            if (interestedNumbers.includes(decoded)) {
                total++;
            }
        }

        superTotal += Number(display.decodedOutputs[0]) * 1000
            + Number(display.decodedOutputs[1]) * 100
            + Number(display.decodedOutputs[2]) * 10
            + Number(display.decodedOutputs[3]);

    }
    tools.cprint(total);
    tools.cprint(superTotal);
}


main();