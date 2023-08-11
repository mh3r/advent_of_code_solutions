import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d13_input.txt";
    console.log("File: " + fileName);
    console.log("\n\n");


    const pairs = tools.readFileFromLocal(fileName).split(/\r?\n\r?\n/).map(x => x.split(/\r?\n/).map(y => {
        // console.log(y)
        return eval(y);
    }

    ));

    // tools.cprint(pairs);
    // const checkedPairs = process(pairs);
    // tools.printJson(checkedPairs);
    // const sum = checkedPairs.reduce((acc, currentValue) => acc + currentValue, 0);
    // tools.printJson("Sum: " + sum);




    // 5546 too high 
    // 1203 is too low 
    // 5013 is correct 
    // part 2 25038 



    sorter(pairs);


// remember to remove/add 

// [[2]]
// [[6]]


}


function process(pairs) {
    const checkedPairs = [];
    for (let i = 0; i < pairs.length; i++) {

        const left = pairs[i][0];
        const right = pairs[i][1];
        let checked = false;
        console.log(`STARTING .................................................. ${i + 1} `);
        checked = checkPair(left, right, i + 1);
        if (checked >= 0) checkedPairs.push(i + 1);
    }

    return checkedPairs;

}


function sorter(pairs) {

    const sorts = [];
    for (let i = 0; i < pairs.length; i++) {
        const left = pairs[i][0];
        const right = pairs[i][1];
        sorts.push(left);
        sorts.push(right);
    }

    sorts.sort((a, b) => checkPair(a, b));
    sorts.reverse();
    tools.cprint(sorts);

    let i = 0;

    find(sorts);
}

function find(sorts) {
    let findA;
    let findB;
    for (let i = 0; i < sorts.length; i++) {
        const item = sorts[i];
        if (Array.isArray(item) && item.length == 1 && item[0].length == 1 && item[0][0] == 2) {
            findA = i + 1;
        }
        if (Array.isArray(item) && item.length == 1 && item[0].length == 1 && item[0][0] == 6) {
            findB = i + 1;
        }
    }

    console.log(`${findA} * ${findB}  = ${findA * findB}`);


}

function checkPair(left, right, caseNumber = 0) {
    for (let i = 0; i < left.length && i < right.length; i++) {
        let leftValue = left[i];
        let rightValue = right[i];

        if (Number.isInteger(leftValue) && Number.isInteger(rightValue)) {
            if (leftValue !== rightValue) {
                const retval = rightValue - leftValue;
                // console.log(` ${leftValue} vs ${rightValue} ... RETURNING ${retval}`);
                return retval;
            }
        } else {
            if (Number.isInteger(leftValue)) {
                leftValue = [leftValue];
            }
            if (Number.isInteger(rightValue)) {
                rightValue = [rightValue];
            }
            const test = checkPair(leftValue, rightValue, caseNumber);
            if (test !== 0) {
                return test;
            }
        }
    }
    return right.length - left.length;
}

function checkPair2(left, right, caseNumber) {
    let retval = true;

    if (Number.isInteger(left) && Number.isInteger(right)) {
        if (left == right) {
            console.log(`${left} vs ${right}  ... continuing`);
            return null;
        } else {
            retval = left < right;
            console.log(` ${left} vs ${right} ... RETURNING ${retval}`);
            return retval;
        }
    }

    if (Number.isInteger(left)) {
        left = [left];
    } else if (Number.isInteger(right)) {
        right = [right];
    }

    for (let i = 0; i < left.length; i++) {
        if (right.length == i) {
            console.log(`Right too short.`);
            return false;
        }

        let test = checkPair2(left[i], right[i], caseNumber);
        if (test != null) {
            return test;
        }
    }

    console.log(`\t\t\tCase ${caseNumber}: nothing wrong.`);
    return retval;
}


main();