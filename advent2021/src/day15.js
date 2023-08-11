import { cp } from 'fs';
import * as tools from '../../tools.js';

let fileName;
let PART = 1;
const TWO = 2;

function main() {
  let array = [];

  fileName = "advent2021/data/test.txt";
  // fileName = "D:/aoc/advent2021/data/d15_input.txt";
  console.log("File: " + fileName);
  console.log("\n\n");

  const isTest = fileName.includes("test");

  let counter = 0;
  const lines = tools.readFileFromLocal(fileName).split(/\r?\n/);
  if (lines[lines.length - 1].length == 0) lines.pop();


  let board = []
  lines.forEach(line => {
    board.push(line.split("").map(x => Number(x)));
  });

  board = expandBoard(4, board);

  // tools.printBoard(board);


  aStarMethod(board);


  
  let debug = 1;
}

function expandBoard(rep, board) {
  let retval = [];
  let rowRetval = board.slice();

  let y = 0;
  for (let row of board) {

    for (let i = 0; i < rep; i++) {
      let increment = 1;
      row = row.map(x => {
        let tmp = x + increment;
        tmp = tmp > 9 ? tmp % 9 : tmp;
        return tmp;
      })
      let debug = 1;
      rowRetval[y].push(...row);
      increment++;
    }

    y++;
  }

  let i = 0;
  Array.from(Array(rep + 1)).forEach(() => {

    for (let row of rowRetval) {
      row = row.map(x => {
        let tmp = x + i;
        tmp = tmp > 9 ? tmp % 9 : tmp;
        return tmp;
      })
      retval.push(row);
    }
    i++;
  });


  return retval;
}

function init(board) {
  const djikstraMap = {};

  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[0].length; x++) {
      const dist = (board.length - 1 - y) + (board.length - 1 - x);
      const key = tools.bindArray([y, x]);

      djikstraMap[key] = {
        dist
        , originalDistance: dist
        , value: Infinity
      };
    }
  }
  return djikstraMap;

}

function aStarMethod(board) {
  let retval = 0;
  const djikstraMap = init(board);
  const startKey = tools.bindArray([0, 0]);
  djikstraMap[startKey].value = 0;

  const visited = [];
  const queue = [];
  queue.push(startKey);
  let finished = false;

  while (queue.length > 0) {
    queue.sort((a, b) => djikstraMap[a].dist - djikstraMap[b].dist);

    const currentKey = queue.shift();
    visited.push(currentKey);
    const splitted = currentKey.split(":");
    const y = Number(splitted[0]);
    const x = Number(splitted[1]);

    if (currentKey == '0:4') {
      let breakpt = 1;
    }


    for (const [dy, dx] of tools.ADJ_DIRS) {

      let tmpY = y + dy;
      let tmpX = x + dx;
      const nextKey = tools.bindArray([tmpY, tmpX]);

      if (tmpY >= 0
        && tmpX >= 0
        && tmpY < board.length
        && tmpX < board[0].length
        && !visited.includes(nextKey)
      ) {
        const newValue = djikstraMap[currentKey].value + board[tmpY][tmpX];

        // tools.cprint(nextKey);
        if (!queue.includes(nextKey)) {
          queue.push(nextKey);
        }

        const nextDjikstra = djikstraMap[nextKey];
        if (nextDjikstra.value > newValue) {
          nextDjikstra.value = newValue;
          nextDjikstra.dist = newValue + nextDjikstra.originalDistance;
        }

        if ((tmpX == board.length - 1) && (tmpY == board.length - 1)) {
          finished = true;
          break;
        }

      }


    }

  }

  tools.cprint( djikstraMap[tools.bindArray([board.length - 1, board.length - 1])].value);



}

main();