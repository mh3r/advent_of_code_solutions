# from parse import *
from functools import reduce
import util
import re
import os
import types
import math


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines, pattern):
    coords = []
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if re.search(pattern, lines[y][x]) is None:
                coords.append([x, y])
    print(coords)
    return coords


def part1(symbols, lines):
    total = 0
    tmpString = ""
    startX = None
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if re.search("\d", lines[y][x]) is not None:
                if startX is None:
                    startX = x

                tmpString += lines[y][x]

            nextX = x + 1
            if nextX == len(lines) or re.search("\d", lines[y][nextX]) is None:
                if startX != None:
                    tmpNumber = int(tmpString)
                    print(tmpNumber)

                    endX = startX + len(tmpString) - 1
                    if (
                        inProximation(symbols, y, startX) is not None
                        or inProximation(symbols, y, endX) is not None
                    ):
                        total += tmpNumber

                    tmpString = ""
                    startX = None

    print("answer ", total)
    assert total == 519444, "total is wrong " + str(total)
    pass


def part2(symbols, lines):
    total = 0
    tmpString = ""
    startX = None
    pairings = {}
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if re.search("\d", lines[y][x]) != None:
                if startX is None:
                    startX = x
                tmpString += lines[y][x]

            nextX = x + 1
            # could have used Python String isdigit() Method
            if nextX == len(lines) or re.search("\d", lines[y][nextX]) is None:
                if startX != None:
                    tmpNumber = int(tmpString)
                    print(tmpNumber)

                    endX = startX + len(tmpString) - 1
                    key = inProximation(symbols, y, startX)

                    if key is None:
                        key = inProximation(symbols, y, endX)

                    if key is not None:
                        if key not in pairings:
                            pairings[key] = []
                        pairings[key].append(tmpNumber)

                    tmpString = ""
                    startX = None

    util.printJson(pairings)

    for key in pairings:
        if len(pairings[key]) > 1:
            total += pairings[key][0] * pairings[key][1]
    print("answer ", total)
    assert total == 74528807, "total is wrong " + str(total)
    pass


def inProximation(symbols, y, x):
    for symbolCoord in symbols:
        for coord in util.ADJ_DIRS_2:
            if symbolCoord[0] + coord[0] == x and symbolCoord[1] + coord[1] == y:
                return util.stringifyCoord(symbolCoord)


filename = "..\\data\\d3_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

symbols = init(lines, "\d|\.")
gears = init(lines, "^((?!\*).)*$")


part1(symbols, lines)
part2(gears, lines)

