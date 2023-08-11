import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;


function main() {
    let array = [];

    let data;
    const input = {
        x: {
            min: 20
            , max: 30
        },
        y: {
            min: -10
            , max: -5
        }
    }

    const input2 = {
        x: {
            min: 155
            , max: 182
        },
        y: {
            min: -117
            , max: -67
        }
    }

    data = input2;

    let maxHeight = 0;
    let counter = 0;

    for (let y = 3000; y > -3000; y--) {
        for (let x = 1; x <= data.x.max; x++) {
            const result = projectProjection(x, y, data);

            if (result != null) {
                maxHeight = maxHeight < result ? result : maxHeight;
                counter++;
            }
        }
    }

    tools.cprint(maxHeight);
    tools.cprint(counter);
}


function projectProjection(x, y, input) {
    let madeIt = false;
    let maxHeight = 0;

    let isContinue = true;
    let currentX = 0;
    let currentY = 0;

    while (isContinue) {
        currentX += x;
        currentY += y;

        maxHeight = maxHeight < currentY ? currentY : maxHeight;
        if (currentX >= input.x.min
            && currentX <= input.x.max
            && currentY <= input.y.max
            && currentY >= input.y.min
        ) {
            madeIt = true;
            isContinue = false;
        }

        x = Math.max(x - 1, 0);
        y--;

        isContinue = currentY > input.y.min;
    }

    return madeIt ? maxHeight : undefined;
}


main();