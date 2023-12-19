# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        lineArray = []
        for char in [*line]:
            lineArray.append(int(char))
        retval.append(lineArray)

    retval = lines if len(retval) == 0 else retval
    return retval


def travel(initialValues):
    global minValues

    queue = initialValues
    seen = []
    minValueDestination = None
    while queue:
        current = queue.pop(0)
        seen.append(current)
        y, x, dy, dx = current

        if y == 1 and x == 3:
            debugggg = 1

        currentStr = util.stringifyCoord([y, x])
        currentValue = calculateValue(current)

        if currentStr not in minValues:
            minValues[currentStr] = currentValue

        if minValues[currentStr] > currentValue:
            minValues[currentStr] = currentValue

        if (
            y == len(input) - 1
            and x == len(input[0]) - 1
            and (minValueDestination is None or minValueDestination > currentValue)
        ):
            minValueDestination = currentValue

        for y1, x1 in util.ADJ_DIRS:
            newY = y + y1
            newX = x + x1

            if (
                newY >= 0
                and newY < len(input)
                and newX >= 0
                and newX < len(input[0])
                and ([-1 * y1, -1 * x1] != [dy, dx])
            ):
                if (
                    dy == y1
                    and dx == x1
                    and [y - dy, x - dx, dy, dx] in seen
                    and [y - 2 * dy, x - 2 * dx, dy, dx] in seen
                    and [y - 3 * dy, x - 3 * dx, dy, dx] in seen
                ):
                    continue
                proposedInstruction = [newY, newX, y1, x1]
                projectedValue = currentValue + input[newY][newX]
                proposedKey = util.stringifyCoord([newY, newX])
                if (
                    proposedKey not in minValues
                    or minValues[proposedKey] > projectedValue
                ) and proposedInstruction not in queue:
                    queue.append(proposedInstruction)

        if minValueDestination is not None:
            tmpQueue = []
            for instruction in queue:
                value = calculateValue(instruction)
                if value < minValueDestination:
                    tmpQueue.append(instruction)
            queue = tmpQueue

        queue.sort(key=calculateValueWithDistance)

    return minValues[util.stringifyCoord([len(input) - 1, len(input[0]) - 1])]


def part1(input):
    answer = 0

    answer = travel([[0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0]])
    util.printJson(minValues)
    print("answer part 1", answer)
    # assert answer in [0, 102], "total is wrong " + str(answer)
    pass


def calculateValue(instruction):
    y, x, dy, dx = instruction
    coord = [y, x]
    prevCoordStr = util.stringifyCoord([y - dy, x - dx])

    prevValue = 0

    if prevCoordStr in minValues:
        prevValue = minValues[prevCoordStr]

    return prevValue + input[y][x]


def calculateValueWithDistance(instruction):
    y, x, dy, dx = instruction
    coord = [y, x]
    return calculateValue(instruction) + util.manhattanDistance(
        coord, [len(input) - 1, len(input[0]) - 1]
    )


def part2(input):
    answer = 0

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d17_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)
minValues = {}
minValues[util.stringifyCoord([0, 0])] = 0

# print(input)


part1(input)
# part2(input)

arrows = [
    [0, 1],
    [0, 2],
    [0, 5],
    [0, 6],
    [0, 7],
    [0, 8],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [1, 8],
    [2, 8],
    [2, 9],
    [2, 10],
    [3, 10],
    [4, 10],
    [4, 11],
    [5, 11],
    [6, 11],
    [7, 11],
    [7, 12],
    [8, 12],
    [9, 12],
    [10, 11],
    [10, 12],
    [11, 11],
    [12, 11],
    [12, 12],
]


# for y, line in enumerate(lines):
#      for x, char in enumerate([*line]):
#         if char in ">^v<":
#             arrows.append([y,x])

# print(arrows)

# testme = {}
# value = 0
# for coord in arrows:
#     y, x = coord
#     value  = int(input[y][x])
#     testme[util.stringifyCoord(coord)] = value

# util.printJson(testme)


# result = {
#     "0_1": 4,
#     "0_2": 5,
#     "0_5": 8,
#     "0_6": 10,
#     "0_7": 13,
#     "0_8": 14,
#     "1_2": 15,
#     "1_3": 20,
#     "1_4": 24,
#     "1_5": 29,
#     "1_8": 32,
#     "2_8": 37,
#     "2_9": 41,
#     "2_10": 43,
#     "3_10": 47,
#     "4_10": 52,
#     "4_11": 55,
#     "5_11": 60,
#     "6_11": 66,
#     "7_11": 71,
#     "7_12": 74,
#     "8_12": 81,
#     "9_12": 84,
#     "10_11": 90,
#     "10_12": 93,
#     "11_11": 96,
#     "12_11": 99,
#     "12_12": 102,
# }
# trythis = {}
# trythis["ASD"] = 4
# trythis[util.stringifyCoord([3, 5])] = 3

# print(trythis)
# print(util.decryptCoord("3_5"))
