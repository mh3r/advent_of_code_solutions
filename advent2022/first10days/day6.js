import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d6_input.txt";

    let counter = 1;
    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        console.log(markerDetection(line));
    });
   

    
}

function markerDetection(input) {
    for (let i = 0; i < input.length; i++) {
        let tmpArray = [];
        tmpArray.push(input[i]);
        for (let j = 1; j < 14; j++) {
            if (!tmpArray.includes(input[i + j])) {
                tmpArray.push(input[i + j])
                if (j == 13) {
                    return i + 14;
                }
            } else {
                break;
            }
        }

    }
}


main();