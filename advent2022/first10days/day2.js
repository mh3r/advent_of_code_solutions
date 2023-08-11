import * as tools from '../tools.js';

const scoring = {
    "A": 1
    , "B": 2
    , "C": 3
    , "X": 1
    , "Y": 2
    , "Z": 3
};

function main() {
    const array = []

    let fileName = "D:/dled/advent2022/test.txt";
    fileName = "D:/dled/advent2022/d2_input.txt";

    let totalScore = 0;
    tools.readFileFromLocal(fileName).split(/\r?\n/).forEach(line => {
        array.push(line);

        // totalScore += countScore(line);
        totalScore += reAdjustStrategy(line);
    });

    // printJson(array);
    console.log(totalScore);
}

function countScore(data) {
    const player1 = data.split(" ")[0];
    const player2 = data.split(" ")[1];

    let score = scoring[player2];

    if (scoring[player2] - scoring[player1] == 1 || scoring[player2] - scoring[player1] == -2) {
        score += 6;
    } else if (scoring[player1] == scoring[player2]) {
        score += 3;
    }
    console.log(score)
    return score;
}

function reAdjustStrategy(input) {
    const player1 = input.split(" ")[0];
    const player2 = input.split(" ")[1];

    let score = 0;

    if (player2 == "X") {
        let player2Score = (scoring[player1] - 1);
        player2Score = player2Score == 0 ? 3 : player2Score;
        score = player2Score;
    } else if (player2 == "Y") {
        score = 3 + scoring[player1];
    } else {
        score = 6;
        let player2Score = (scoring[player1] + 1);
        player2Score = player2Score == 4 ? 1 : player2Score;
        score += player2Score;
    }

    return score;
}

main();