import * as tools from "../../js-util/tools.js";

const YEAR = 2025;

function run(config) {
  let answerPt1 = 0;
  let answerPt2 = 0;
  const correctAnswerPt1 = 97384;
  const correctAnswerPt2 = 9003685096;

  const circuits = config.circuits;
  const junctionDistances = [...config.junctionDistances];

  for (let i = 0; i < junctionDistances.length; i++) {
    const junctionDistance = junctionDistances[i];
    const junction1 = junctionDistance.junctions[0];
    const junction2 = junctionDistance.junctions[1];

    connectCircuits(circuits, junction1, junction2);

    if (i === config.reps) {
      answerPt1 = getPart1Answer(circuits);
    }

    if (circuits.size === 1) {
      const xCoord1 = parseInt(junction1.split(",")[0]);
      const xCoord2 = parseInt(junction2.split(",")[0]);
      answerPt2 = xCoord1 * xCoord2;
      break;
    }
  }

  console.log(`Part 1: ${answerPt1}`);
  console.assert(
    correctAnswerPt1 === answerPt1,
    `${answerPt1} should have been ${correctAnswerPt1}`,
  );

  console.log(`Part 2: ${answerPt2}`);
  console.assert(
    correctAnswerPt2 === answerPt2,
    `${answerPt2} should have been ${correctAnswerPt2}`,
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

function prepareConfig(lines, test) {
  const config = {
    raw: lines,
  };

  config.reps = test ? 10 : 1000;
  // adjusting for 0 index 
  config.reps -= 1;

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

  const circuits = new Map();
  for (const junction of config.raw) {
    circuits.set(junction, [junction]);
  }
  config.circuits = circuits;

  return config;
}

function connectCircuits(circuits, junction1, junction2) {
  const circuitName1 = findCircuitName(circuits, junction1);
  const circuitName2 = findCircuitName(circuits, junction2);

  if (circuitName1 === circuitName2) {
    return;
  }
  const circuit1Junctions = circuits.get(circuitName1);
  const circuit2Junctions = circuits.get(circuitName2);

  circuit1Junctions.push(...circuit2Junctions);
  circuits.delete(circuitName2);
}

function findCircuitName(circuits, junction) {
  if (circuits.get(junction) && circuits.get(junction).length === 1) {
    return junction;
  }

  for (const circuit of circuits.keys()) {
    if (circuits.get(circuit).includes(junction)) {
      return circuit;
    }
  }
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

function main() {
  const baseDir = `${process.cwd()}\\advent${YEAR}`;
  const dataDir = `${baseDir}\\data`;

  let test = false;
  // test = true;

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

  const config = prepareConfig(lines, test);

  run({ ...config });
}

main();
