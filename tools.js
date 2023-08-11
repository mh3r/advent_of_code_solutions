import { readFile, readFileSync } from 'fs';

export const ADJ_DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]];
export const ADJ_DIRS_2 = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]];


export function readFileFromLocal(fileName) {
    return readFileSync(fileName, 'utf-8');
}


export function printJson(data) {
    console.log(JSON.stringify(data, null, 2));
}

export function cprint(data) {
    console.log(data);
}

export function printBoard(array) {
    for (const line of array) {
        cprint(line.join(""))
    }
}

function unusedStuff() {


    for (const [dy, dx] of ADJ_DIRS) {
        // comment these lines
        let y = 1;
        let x = 1;

        let tmpY = y + dy;
        let tmpX = x + dx;;
        if (tmpY >= 0
            && tmpX >= 0
            && tmpY < board.length
            && tmpX < board[0].length

            // && !visited.includes(tools.bindArray([tmpY, tmpX]))
        ) {


        }

    }

}


export function bindArray(array) {
    return `${array[0]}:${array[1]}`;
}

export function unbindArray(string) {
    const splitted = string.split(":");
    return [Number(splitted[0]), Number(splitted[1])];
}
//  let [y, x] = tools.unbindArray(bind);



let debug = 1;
