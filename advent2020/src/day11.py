# from parse import *
from functools import reduce
import util
import re
import json
import os
import copy

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def numberAdjacentOccupied(lines, y, x):
    retval = 0
    for coords in util.ADJ_DIRS_2:
        newX = x + coords[0]
        newY = y + coords[1]
        if (
            newX >= 0
            and newY >= 0
            and newX < len(lines[0])
            and newY < len(lines)
            and lines[newY][newX] == OCCUPIED
        ):
            retval += 1
    return retval


def numberExtendedOccupied(lines, y, x):
    retval = 0
    for coords in util.ADJ_DIRS_2:
        for i in range(1, 100):
            newX = x + i * coords[0]
            newY = y + i * coords[1]

            if not (
                newX >= 0 and newY >= 0 and newX < len(lines[0]) and newY < len(lines)
            ):
                break

            tmpValue = lines[newY][newX]

            if tmpValue == EMPTY:
                break
            elif tmpValue == FLOOR:
                continue
            elif tmpValue == OCCUPIED:
                retval += 1
                break
    return retval


def runCycle(lines, isFirst=True):
    seatTolerance = 4 if isFirst else 5
    retval = None
    tmpCopy = copy.deepcopy(lines)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == FLOOR:
                continue

            noOfOccupied = (
                numberAdjacentOccupied(lines, y, x)
                if isFirst
                else numberExtendedOccupied(lines, y, x)
            )

            if noOfOccupied == 0:
                tmpCopy[y][x] = OCCUPIED
            elif noOfOccupied >= seatTolerance:
                tmpCopy[y][x] = EMPTY

    if not tablesUnchanged(lines, tmpCopy):
        retval = tmpCopy
    return retval


def tablesUnchanged(table1, table2):
    retval = True
    for y in range(len(table1)):
        if "".join(table1[y]) != "".join(table2[y]):
            retval = False
            break
    return retval


def printTable(lines):
    for line in lines:
        print("".join(line))


def occupiedCounter(current):
    count = 0
    for line in current:
        count += "".join(line).count(OCCUPIED)
    print(count)


def part1(lines):
    current = copy.deepcopy(lines)
    while True:
        result = runCycle(current)
        if result == None:
            break
        else:
            current = result

    # printTable(current)
    occupiedCounter(current)


def part2(lines):
    current = copy.deepcopy(lines)
    while True:
        result = runCycle(current, False)
        if result == None:
            break
        else:
            current = result

    # printTable(current)
    occupiedCounter(current)


filename = "..\\data\\d11_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: list(x.strip()), lines))


part1(lines)
part2(lines)


