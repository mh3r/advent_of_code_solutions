# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

DIRS = ["R", "L", "D", "U"]


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    directions, steps, hexCodes = [], [], []
    width = 0
    height = 0
    leftOffset = 0
    topOffset = 0
    for line in lines:
        direction, number, hexCode = line.split()
        number = int(number)

        if isPart2:
            hexCode = hexCode.replace("(#", "0x").replace(")", "")
            number = int(hexCode[:-1], 0)
            leftOver = hexCode[-1:]
            if leftOver == "0":
                direction = DIRS[2]
            elif leftOver == "1":
                direction = DIRS[0]
            elif leftOver == "2":
                direction = DIRS[1]
            elif leftOver == "3":
                direction = DIRS[3]

        # print(int("0x70c71", 0))

        directions.append(direction)
        steps.append(number)
        hexCodes.append(hexCode)
        if direction == "R":
            width += number
            height += 1

        if direction == "D":
            width += 1
            height += number

        if direction == "U":
            topOffset += number

        if direction == "L":
            leftOffset += number

    retval = lines if len(retval) == 0 else retval

    return (
        directions,
        steps,
        hexCodes,
        width + leftOffset,
        height + topOffset,
        topOffset,
        leftOffset,
    )


def part1(input):
    answer = 0

    newTable = []

    for y in range(height):
        line = []
        for x in range(width):
            line.append(".")
        newTable.append(line)

    startingPoint = [topOffset, leftOffset]
    y, x = startingPoint
    newTable[y][x] = "#"
    for i, direction in enumerate(directions):
        for j in range(steps[i]):
            dy, dx = util.ADJ_DIRS[DIRS.index(direction)]
            y += dy
            x += dx
            newTable[y][x] = "#"

    # printTable(newTable)

    # seen = []
    next = [[topOffset + 1, leftOffset + 1]]

    while next:
        coord = next.pop()
        y, x = coord
        newTable[y][x] = "#"
        # seen.append(coord)
        if y == 6 and x == 3:
            debugTime = 0

        for dy, dx in util.ADJ_DIRS:
            newY = y + dy
            newX = x + dx
            if (
                newY < 0
                or newY >= height
                or newX < 0
                or newX >= width
                or newTable[newY][newX] == "#"
            ):
                continue
            if newTable[newY][newX] == ".":
                next.append([newY, newX])

    # printTable(newTable)

    for y in range(height):
        for x in range(width):
            if newTable[y][x] == "#":
                answer += 1

    print("answer part 1", answer)
    assert answer in [0, 62, 49578], "total is wrong " + str(answer)
    pass


def printTable(newTable):
    for y in range(len(newTable)):
        print("".join(newTable[y]))


# need to use shoelace algorithm
# https://www.youtube.com/watch?app=desktop&v=sNPh8jgngE0&ab_channel=ChenHongming        
def part2(input):
    answer = 0

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d18_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

isPart2 = False
directions, steps, hexCodes, width, height, topOffset, leftOffset = init(lines)

part1(input)
part2(input)


# print(directions, steps, hexCodes)

# thehextcode = "(#70c710)"

# thehextcode = thehextcode.replace("(#", "0x").replace(")", "")
# print(thehextcode[:-1])


# print(thehextcode[-1:])


# print(int("0x70c71", 0))
