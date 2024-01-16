# from parse import *
from functools import reduce
import util
import re
import os
import types
import math
from collections import defaultdict


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    """
    numberCollections is a 2d array
    first indicates row number for easy referencing to symbols coordinates
    second indicates array of tuples containing number starting index and value

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    would become
    [
    [(0, 467), (5, 114)]
    ,[]
    ,[(2, 35), (6, 633)]
    ,[]
    ,[(0, 617)]
    ,[(7, 58)]
    ,[(2, 592)]
    ,[(6, 755)]
    ,[]
    ,[(1, 664), (5, 598)]
    ]
    """
    numberCollections = []
    symbols = defaultdict(list)

    for y, line in enumerate(lines):
        rowInfo = []
        numberMode = False
        partialNumber = ""
        startingIndex = 0
        for x, char in enumerate(line):
            if not numberMode and char.isdigit():
                startingIndex = x

            numberMode = char.isdigit()

            if numberMode:
                partialNumber += char

            if (not numberMode or x == len(lines[y]) - 1) and partialNumber:
                rowInfo.append((startingIndex, int(partialNumber)))
                partialNumber = ""

            if not char.isdigit() and char != ".":
                symbols[char].append((y, x))
        numberCollections.append(rowInfo)
    # print(symbols)
    # print(*numberCollections, sep="\n")
    return symbols, numberCollections


def part1(symbols, numberCollections):
    total = 0
    for symbol in symbols:
        for coord in symbols[symbol]:
            y, x = coord
            total += sum(getProximation(numberCollections, y, x))

    print("answer ", total)
    assert total in [519444, 4361, 0], "total is wrong " + str(total)
    pass


def part2(symbols, numberCollections):
    total = 0
    targetSymbol = "*"
    for coord in symbols[targetSymbol]:
        y, x = coord
        numberProximates = getProximation(numberCollections, y, x)
        if len(numberProximates) == 2:
            total += numberProximates[0] * numberProximates[1]

    print("answer ", total)
    assert total in [74528807, 0, 467835], "total is wrong " + str(total)
    pass


def getProximation(numberCollections, y, x):
    retval = []
    for y1 in range(y - 1, y + 2):
        if y1 >= 0 and y1 < len(lines):
            for numberInfo in numberCollections[y1]:
                start, number = numberInfo
                end = start + len(str(number)) - 1
                if x in range(start - 1, end + 2):
                    retval.append(number)

    return retval


filename = "..\\data\\d3_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

symbols, numberCollections = init(lines)

part1(symbols, numberCollections)
part2(symbols, numberCollections)
