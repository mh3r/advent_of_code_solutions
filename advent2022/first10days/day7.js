import * as tools from '../tools.js';


function main() {
    let array = [];

    let fileName = "D:/advent2022/data/test.txt";
    fileName = "D:/advent2022/data/d7_input.txt";

    let counter = 1;
    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        array.push(line);
    });

    analyseStructure(array);
}


function analyseStructure(input) {
    const pc = {};
    const currentPath = [];

    for (const line of input) {
        if (line.includes("$")) {
            if (line.includes("cd")) {
                let dest = line.split(" ")[2];
                dest = dest == "/" ? "root" : dest;
                if (line.includes("..")) {
                    currentPath.pop();
                } else {
                    currentPath.push(dest);
                }
            }
        } else {
            let word1 = line.split(" ")[0];
            if (word1 != "dir") {
                const size = Number(line.split(" ")[0]);

                let tmpPath = "";
                for (const path of currentPath) {
                    tmpPath += path;
                    pc[tmpPath] ??= 0;
                    pc[tmpPath] += size;
                    tmpPath += "/";
                }
            }
        }
    }


    console.log(JSON.stringify(pc, null, 2));

    const value = Object.values(pc).filter(x => x < 100000).reduce((partialSum, a) => partialSum + a, 0);
    console.log(value);

    const values = Object.values(pc).filter(x => x > 1111105).sort();

    console.log(Math.min (...values));

    // 100000
    // 1111105 
    // part 1 1543140
    // part 2 1117448

}



main();