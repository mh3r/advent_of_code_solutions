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


def rotate(items):
    itemsCopy = items.copy()
    itemsCopy = list(
        map(lambda coord: [coord[1], totalLength - 1 - coord[0]], itemsCopy)
    )
    return itemsCopy

#  rotate is just data = [list(i[::-1]) for i in [*zip(*data)]]


def init(lines):
    retval = []
    rocks = []
    blocks = []
    for y, line in enumerate(lines):
        for x, char in enumerate([*line]):
            if char == "O":
                rocks.append([y, x])
            elif char == "#":
                blocks.append([y, x])
    retval = lines if len(retval) == 0 else retval
    return rocks, blocks


def rockCanMove(rock, rocks, blocks):
    y, x = rock
    newCoord = [y - 1, x]
    return y > 0 and newCoord not in rocks and newCoord not in blocks


def calculateValue(rocks):
    answer = 0
    for y, x in rocks:
        answer += totalLength - y
    return answer


# take second element for sort
def takeFirst(elem):
    return elem[0]


# way too slow .. need to redo this part
def moveRocks(rocks, blocks):
    rocksCopy = rocks.copy()
    rocksCopy.sort(key=takeFirst)

    while len(rocksCopy) > 0:
        rock = rocksCopy.pop(0)
        isKeepGoing = True
        while isKeepGoing:
            if rockCanMove(rock, rocks, blocks):
                rocks.remove(rock)
                rock = [rock[0] - 1, rock[1]]
                rocks.append(rock)
            else:
                isKeepGoing = False


def newMove(rocks, blocks):
    retval = []
    for x in range(totalLength):
        filteredRocks = list(filter(lambda xxx: xxx[1] == 1, rocks))
        filteredRocks.sort()
        lastBlock = -1
        for y in range(totalLength):
            coord = [y, x]
            if coord in blocks:
                lastBlock = y
            elif coord in rocks:
                for j in range(lastBlock + 1, totalLength):
                    if [j, x] not in retval:
                        retval.append([j, x])
                        break

    return retval


def part1(rocks, blocks):
    answer = 0

    # moveRocks(rocks, blocks)
    rocks = newMove(rocks, blocks)
    answer = calculateValue(rocks)
    print("haiya", rocks)

    print("answer part 1", answer)
    assert answer in (0, 136, 107053), "total is wrong " + str(answer)
    pass


def part2(rocks, blocks):
    answer = 0
    values = []

    for i in range(4 * 200):
        # moveRocks(rocks, blocks)
        rocks = newMove(rocks, blocks)
        rocks = rotate(rocks)
        blocks = rotate(blocks)
        if i % 4 == 3:
            value = calculateValue(rocks)
            print(value)
            values.append(value)

    for i, value in enumerate(values):
        print(i, "------------", value)

    start = 2
    end = 8
    frequecy = end - start
    indexAnswer = (1000_000_000 % frequecy) + start - 1
    print(indexAnswer)
    answer = values[indexAnswer]
    print("answer part 2", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d14_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")
# the input and sample are square in shape
totalLength = len(lines)

rocks, blocks = init(lines)
print(rocks)
print(blocks)

# part1(rocks, blocks)
part2(rocks, blocks)

# print(rotate(rocks, 4))


testData = rocks.copy()


filteredRock = list(filter(lambda x: x[1] == 0, testData))
filteredRock.append([2, 0])
print(filteredRock)
filteredRock.sort()
print("sorted", filteredRock)
# print(list(filter(lambda x: x not in filteredRock, testData)))

# theblocks = [1, 4, 6]

# for i, block in enumerate(theblocks):
#     start = 0
#     end = block
#     if i > 0:
#         start = 0
#         end = block

#     for j in range(start, end):
#             print(j)
