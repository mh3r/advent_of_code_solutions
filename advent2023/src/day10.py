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
    sCoord = None
    for count, line in enumerate(lines):
        retval.append([*line])
        if "S" in line:
            sCoord = [line.index("S"), count]
        pass
    retval = lines if len(retval) == 0 else retval
    return [retval, sCoord]


def move(sCoord, theMap):
    path = []
    x, y = sCoord

    current = sCoord
    previousCoord = None
    while util.stringifyCoord(sCoord) != util.stringifyCoord(current) or len(path) == 0:
        x, y = findNext(previousCoord, current, theMap)
        previousCoord = util.stringifyCoord(current)
        path.append(previousCoord)
        # print(previousCoord + "    " + theMap[current[1]][current[0]])
        current = [x, y]
    return path


def findNext(previousCoord, current, theMap):
    retval = None
    x, y = current
    possiblePaths = []

    currentSymbol = theMap[y][x]

    if currentSymbol == "|":
        possiblePaths.append(util.stringifyCoord([x, y - 1]))
        possiblePaths.append(util.stringifyCoord([x, y + 1]))

    if currentSymbol == "-":
        possiblePaths.append(util.stringifyCoord([x + 1, y]))
        possiblePaths.append(util.stringifyCoord([x - 1, y]))

    if currentSymbol == "L":
        possiblePaths.append(util.stringifyCoord([x + 1, y]))
        possiblePaths.append(util.stringifyCoord([x, y - 1]))

    if currentSymbol == "J":
        possiblePaths.append(util.stringifyCoord([x - 1, y]))
        possiblePaths.append(util.stringifyCoord([x, y - 1]))

    if currentSymbol == "7":
        possiblePaths.append(util.stringifyCoord([x, y + 1]))
        possiblePaths.append(util.stringifyCoord([x - 1, y]))

    if currentSymbol == "F":
        possiblePaths.append(util.stringifyCoord([x + 1, y]))
        possiblePaths.append(util.stringifyCoord([x, y + 1]))

    if currentSymbol == "S":
        y1 = y
        x1 = x + 1
        if theMap[y1][x1] in ["-", "J", "7"]:
            possiblePaths.append(util.stringifyCoord([x1, y1]))
        y1 = y
        x1 = x - 1
        if theMap[y1][x1] in ["-", "F", "L"]:
            possiblePaths.append(util.stringifyCoord([x1, y1]))
        y1 = y + 1
        x1 = x
        if theMap[y1][x1] in ["|", "J", "L"]:
            possiblePaths.append(util.stringifyCoord([x1, y1]))
        y1 = y - 1
        x1 = x
        if theMap[y1][x1] in ["|", "F", "7"]:
            possiblePaths.append(util.stringifyCoord([x1, y1]))

    if previousCoord is not None:
        possiblePaths.remove(previousCoord)

    retval = list(map(lambda x: int(x), possiblePaths[0].split("_")))

    return retval


def part1(sCoord, input):
    answer = 0

    path = move(sCoord, input)
    answer = int(len(path) / 2)
    # print(path)
    print(*path )

    print("answer part 1:", answer)
    assert 6649 == answer, "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    print("answer part 2:", answer)
    assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d10_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

symbols = ["|", "-", "L", "J", "7", "F", "."]
newSymbols = ["┃", "━", "┗", "┛", "┓", "┏", "x"]

newInput = []
for line in lines:
    for count, symbol in enumerate(symbols):
        line = line.replace(symbols[count], newSymbols[count])
    newInput.append(line)


print(*newInput, sep="\n")

input, sCoord = init(lines)
 
# print(*input, sep="\n")
print(sCoord)

# part1(sCoord, input)
# part2(input)


path = move(sCoord, input)
# lines[sCoord[1]][sCoord[0]] = "J"

# below is someone elses code .... 
# its using a method called ray casting algorithm
start_is_vert = False
area = 0
for y in range(len(lines)):
    odd_parity = False
    for x in range(len(lines[0])):
        if util.stringifyCoord([x, y]) in path:
            if lines[y][x] in "|JL" or (lines[y][x] == 'S' and start_is_vert):
                odd_parity = not odd_parity
        else:
            area += 1 if odd_parity else 0

print(area)

