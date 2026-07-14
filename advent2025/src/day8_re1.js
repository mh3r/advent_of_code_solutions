import * as tools from "../../js-util/tools.js";

const YEAR = 2025;

function part1(config) {
  let answer = 0;
  const correctAnswer = 97384;

  const connectedJunctions = [];
  const circuits = new Map();

  const junctionDistances = [...config.junctionDistances];

  let connections = 0;
  for (const junctionDistance of junctionDistances) {
    const junction1 = junctionDistance.junctions[0];
    const junction2 = junctionDistance.junctions[1];

    const circuit1 = findCircuit(circuits, junction1);
    const circuit2 = findCircuit(circuits, junction2);

    connections += connectCircuits(circuits, circuit1, circuit2);

    if (connections === 9) {
      answer = getPart1Answer(circuits);
      break;
    }
  }

  console.log(`Part 1: ${answer}`);
  console.assert(
    correctAnswer === answer,
    `${answer} should have been ${correctAnswer}`,
  );
}

function part2(config) {
  let answer = 0;
  const correctAnswer = undefined;

  console.log(`Part 2: ${answer}`);
  console.assert(
    correctAnswer === answer,
    `${answer} should have been ${correctAnswer}`,
  );
}

function getPart1Answer(circuits) {
  const sizes = [];
  for (const circuit of circuits.values()) {
    sizes.push(circuit.length);
  }

  sizes.sort((a, b) => b - a);
  return sizes[0] * sizes[1] * sizes[2];
}

function main() {
  const baseDir = `${process.cwd()}\\advent${YEAR}`;
  const dataDir = `${baseDir}\\data`;

  let test = false;
  test = true;

  let inputFile = `${dataDir}\\d8_input.txt`;
  if (test) {
    inputFile = `${baseDir}\\data\\test.txt`;
  }

  console.log("Input File: " + inputFile);
  const lines = tools
    .readFileFromLocal(inputFile)
    .split(/\r?\n/)
    .filter((x) => x);
  if (lines[lines.length - 1].length == 0) lines.pop();

  const config = {
    raw: lines,
  };

  prepare(config);

  part1({ ...config });
  part2({ ...config });
}

function prepare(config) {
  const junctionDistances = [];
  for (let i = 0; i < config.raw.length - 1; i++) {
    for (let j = i + 1; j < config.raw.length; j++) {
      junctionDistances.push(
        new JunctionDistance(config.raw[i], config.raw[j]),
      );
    }
  }

  junctionDistances.sort((a, b) => a.distance - b.distance);
  config.junctionDistances = junctionDistances;
}

function connectCircuits(circuits, circuit1, circuit2) {
  if (circuit1 === circuit2) {
    return 0;
  }
  const circuit1Junctions = circuits.get(circuit1);
  const circuit2Junctions = circuits.get(circuit2);

  circuit1Junctions.push(...circuit2Junctions);

  circuits.delete(circuit2);
  return 1;
}

function findCircuit(circuits, junction) {
  for (const circuit of circuits.keys()) {
    if (circuits.get(circuit).includes(junction)) {
      return circuit;
    }
  }
  circuits.set(junction, [junction]);
  return junction;
}

class JunctionDistance {
  distance = 0;
  junctions = [];

  constructor(junction1, junction2) {
    this.junctions = [junction1, junction2];
    const junctionData1 = junction1.split(",").map((x) => parseInt(x));
    const junctionData2 = junction2.split(",").map((x) => parseInt(x));

    const dx = junctionData1[0] - junctionData2[0];
    const dy = junctionData1[1] - junctionData2[1];
    const dz = junctionData1[2] - junctionData2[2];
    this.distance = Math.hypot(dx, dy, dz);
  }
}

main();
