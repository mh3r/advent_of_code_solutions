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
    emptyRows = []
    emptyColumns = []
    galaxies = []

    for x in range(len(lines[0])):
        verticalSlice = []
        for y, line in enumerate(lines):
            verticalSlice.append(line[x])
        if HASH not in verticalSlice:
            emptyColumns.append(x)

    for y, line in enumerate(lines):
        if HASH in line:
            for x, value in enumerate(line):
                if value == HASH:
                    galaxies.append([x, y])
        else:
            emptyRows.append(y)

    return galaxies, emptyRows, emptyColumns


def calculateDistancesWithExpansion(galaxies, emptyRows, emptyColumns, expansionFactor):
    galaxyLength = len(galaxies)
    answer = 0
    for i in range(galaxyLength):
        for j in range(i + 1, galaxyLength):
            sourceCoord = galaxies[i]
            destCoord = galaxies[j]
            answer += measureDistance(
                sourceCoord, destCoord, emptyRows, emptyColumns, expansionFactor
            )
    return answer


def measureDistance(a, b, emptyRows, emptyColumns, expansionFactor):
    retval = 0
    ax, ay = a
    bx, by = b
    # manhattan distance
    retval += abs(ax - bx) + abs(ay - by)

    for column in emptyColumns:
        if min(ax, bx) < column and max(ax, bx) > column:
            retval += expansionFactor

    for row in emptyRows:
        if min(ay, by) < row and max(ay, by) > row:
            retval += expansionFactor

    return retval


def part1(galaxies, emptyRows, emptyColumns):
    expansionFactor = 2 - 1
    answer = calculateDistancesWithExpansion(
        galaxies, emptyRows, emptyColumns, expansionFactor
    )

    print("Answer part 1:", answer)
    assert answer in [10289334], "total is wrong " + str(answer)
    pass


def part2(galaxies, emptyRows, emptyColumns):
    expansionFactor = 1000000 - 1
    answer = calculateDistancesWithExpansion(
        galaxies, emptyRows, emptyColumns, expansionFactor
    )
    print("Answer part 2:", answer)
    assert answer in [649862989626], "total is wrong " + str(answer)


filename = "..\\data\\d11_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

galaxies, emptyRows, emptyColumns = init(lines)
print("Empty rows:\t", emptyRows)
print("Empty columns:\t", emptyColumns)

part1(galaxies, emptyRows, emptyColumns)
part2(galaxies, emptyRows, emptyColumns)
