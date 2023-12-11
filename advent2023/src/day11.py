# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

HASH = "#"


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    # galaxies = []
    emptyRows = []
    emptyColumns = []
    for y, line in enumerate(lines):
        if HASH not in line:
            # for x, value in enumerate(line):
            #     if value == HASH:
            #         galaxies.append([x, y])
            # else:
            emptyRows.append(y)

    for x, value in enumerate(lines[0]):
        verticalSlice = []
        for y, line in enumerate(lines):
            verticalSlice.append(line[x])
        if HASH not in verticalSlice:
            emptyColumns.append(x)

    return emptyRows, emptyColumns


# not actually necessary ...
def expand(input, emptyRows, emptyColumns):
    newMap = input.copy()

    for i, row in enumerate(emptyRows):
        newIndex = row + i
        newMap.insert(newIndex, input[row])

    for i, column in enumerate(emptyColumns):
        newIndex = column + i
        for i, row in enumerate(newMap):
            row = row[:newIndex] + "." + row[newIndex:]
            newMap[i] = row

    return newMap


def part1(lines, emptyRows, emptyColumns):
    expanded = expand(lines, emptyRows, emptyColumns)

    galaxies = []
    for y, line in enumerate(expanded):
        if HASH in line:
            for x, value in enumerate(line):
                if value == HASH:
                    galaxies.append([x, y])

    answer = 0
    galaxyLength = len(galaxies)
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            answer += manhattanDistance(galaxies[i], galaxies[j])

    print("answer part 1", answer)
    assert 10289334 == answer, "total is wrong " + str(answer)
    pass


def additionalDistance(a, b, emptyRows, emptyColumns, expansionFactor=1):
    retval = 0
    ax, ay = a
    bx, by = b

    for column in emptyColumns:
        if min(ax, bx) < column and max(ax, bx) > column:
            retval += expansionFactor

    for row in emptyRows:
        if min(ay, by) < row and max(ay, by) > row:
            retval += expansionFactor

    return retval


def part2(lines, emptyRows, emptyColumns):
    galaxies = []
    for y, line in enumerate(lines):
        if HASH in line:
            for x, value in enumerate(line):
                if value == HASH:
                    galaxies.append([x, y])

    answer = 0
    galaxyLength = len(galaxies)
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            sourceCoord = galaxies[i]
            destCoord = galaxies[j]
            answer += manhattanDistance(sourceCoord, destCoord)
            answer += additionalDistance(
                sourceCoord, destCoord, emptyRows, emptyColumns, 1000000 - 1
            )
    print("answer part 2", answer)
    assert 649862989626 == answer, "total is wrong " + str(answer)
    pass


def manhattanDistance(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


filename = "..\\data\\d11_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

emptyRows, emptyColumns = init(lines)
print(emptyRows)
print(emptyColumns)

part1(lines, emptyRows, emptyColumns)
part2(lines, emptyRows, emptyColumns)
