import * as tools from "../../js-util/tools.js";

const YEAR = 2025;

// this is stupid
// there is no need to figure out 
// the most efficient shapes arrangements
// the data input was designed to be solvable by 
// treating all shapes to be a solid 3x3 blocks
function part1(instructions) {
  let answer = 0;
  const correctAnswer = 422;

  for (const instruction of instructions) {
    const area = instruction[0] * instruction[1];
    const sum = instruction[2].reduce((a, b) => a + b, 0) * 9;
    // console.log(`Area: ${area}, Sum: ${sum}`);

    if (sum <= area) {
      answer++;
    }
  }

  console.log(`Part 1: ${answer}`);
  console.assert(
    correctAnswer === answer,
    `${answer} should have been ${correctAnswer}`,
  );
}

function parseInstructions(lines) {
  const output = [];
  for (const line of lines) {
    if (!line.includes("x")) continue; // Skip empty lines

    const dimensions = line.split(":")[0].trim().split("x").map(Number);
    const data = line.split(":")[1].trim().split(" ").map(Number);
    output.push([...dimensions, data]);
  }

  return output;
}

function main() {
  const baseDir = `${process.cwd()}\\advent${YEAR}`;
  const dataDir = `${baseDir}\\data`;

  let inputFile = `${dataDir}\\d12_input.txt`;
  // inputFile = `${baseDir}\\data\\test.txt`;

  console.log("Input File: " + inputFile);
  const lines = tools
    .readFileFromLocal(inputFile)
    .split(/\r?\n/)
    .filter((x) => x);
  if (lines[lines.length - 1].length == 0) lines.pop();

  const config = {
    raw: lines,
    instructions: parseInstructions(lines),
  };
  part1([...config.instructions]);
}

main();
