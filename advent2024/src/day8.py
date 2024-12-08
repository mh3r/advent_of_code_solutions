# from parse import *
from functools import reduce
from collections import defaultdict
import sys
import re
import json
import os
import types
import math

sys.path.append(os.getcwd() + "\py-util")
import util


def switchToTest():
    global filename
    print("Testing ... ")
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            char = lines[y][x]
            if char != ".":
                if char not in starMap:
                    starMap[char] = []
                occupiedArea.append(util.stringifyCoord([y, x]))
                starMap[char].append([y, x])
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    antinodes = []
    for star in starMap:
        coords = starMap[star]

        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                populateAntinodes(coords[i], coords[j], antinodes)

    antinodes = set(antinodes)
    answer = len(antinodes)
    print("answer part 1:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    antinodes = []
    for star in starMap:
        coords = starMap[star]

        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                populateAntinodes2(coords[i], coords[j], antinodes)

    antinodes = set(antinodes)
    answer = len(antinodes)
    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def populateAntinodes2(a, b, antinodes):
    print(a, b, "============")

    ay, ax = a
    by, bx = b

    dy = abs(ay - by)
    dx = abs(ax - bx)

    1, 8
    2, 5

    forPoint = a if ay < by else b
    againstPoint = a if ay > by else b

    xOrientation = 1 if forPoint[1] < againstPoint[1] else -1
    dx = xOrientation * dx

    startingY, startingX = forPoint

    tmpY = startingY
    tmpX = startingX

    while True:
        tmpY = tmpY - dy
        tmpX = tmpX - dx

        if tmpY < 0 or tmpX not in range(len(input[0])):
            break

        startingY = tmpY
        startingX = tmpX

    1, 3

    tmpY = startingY
    tmpX = startingX
    antinodes.append(util.stringifyCoord([tmpY, tmpX]))
    while True:
        tmpY += dy
        tmpX += dx

        if tmpY not in range(len(input)) or tmpX not in range(len(input[0])):
            break
        print(util.stringifyCoord([tmpY, tmpX]))
        antinodes.append(util.stringifyCoord([tmpY, tmpX]))


def populateAntinodes(a, b, antinodes):
    print(a, b, "============")

    ay, ax = a
    by, bx = b

    dx = abs(ax - bx)
    dy = abs(ay - by)

    antiA = []
    antiB = []

    if ay > by:
        antiA.append(ay + dy)
        antiB.append(by - dy)
    else:
        antiA.append(ay - dy)
        antiB.append(by + dy)

    if ax > bx:
        antiA.append(ax + dx)
        antiB.append(bx - dx)
    else:
        antiA.append(ax - dx)
        antiB.append(bx + dx)

    if antiA[0] in range(len(input)) and antiA[1] in range(len(input[0])):
        antinodes.append(util.stringifyCoord(antiA))
        print(util.stringifyCoord(antiA))

    if antiB[0] in range(len(input)) and antiB[1] in range(len(input[0])):
        antinodes.append(util.stringifyCoord(antiB))
        print(util.stringifyCoord(antiB))


filename = "..\\data\\d8_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

occupiedArea = []
starMap = {}

input = init(lines)

# part1()
part2()
