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
    for line in lines:
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            character = grid[y][x]
            if character == "X":
                print (y, x)
                answer += getXmasPathRecur(y, x, 1, [[y, x]])

    print("answer part 1", answer)
    assert answer in [18, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print("answer part 2", answer)
    assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


# def getXmasPath(y, x):
    # getXmasPathRecur 

def getXmasPathRecur(y, x, charIndex, path):
    if len(path) == len(XMAS):
        print (path)
        return 1
    if len(XMAS) == charIndex:
        return 0
    for coords in getNextCoords (y, x, XMAS[charIndex]):
        pathCopy = path[:]
        pathCopy.append(coords)
        return getXmasPathRecur(coords[0], coords[1], charIndex + 1, pathCopy)



def getNextCoords(y, x, character):
    retval = []
    for dx, dy in util.ADJ_DIRS_2:
        tmpY = y + dy
        tmpX = x + dx

        if tmpY not in range(len(grid)) or tmpX not in range(len(grid[0])):
            continue

        if grid[tmpY][tmpX] == character:
            retval.append([tmpY, tmpX])
    return retval

filename = "..\\data\\d4_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)

grid = []
for line in lines:
    grid.append(list(line))

XMAS = list("XMAS")

print(grid)

part1()
part2()
