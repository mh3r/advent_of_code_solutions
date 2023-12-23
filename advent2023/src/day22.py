# from parse import *
from functools import reduce
from collections import defaultdict
from copy import deepcopy, copy
from itertools import product
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
    # first element is gimmicky for initial sorting purposes
    # second element is an array of actual elements occupied
    blueprints = []
    tower = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
    superMaxX = 0
    superMaxY = 0
    superMaxZ = 0

    # brick construction
    for line in lines:
        left, right = line.split("~")
        x, y, z = list(map(int, left.split(",")))
        x1, y1, z1 = list(map(int, right.split(",")))

        lowerX, lowerY, lowerZ = min(x, x1), min(y, y1), min(z, z1)
        upperX, upperY, upperZ = (
            lowerX + abs(x - x1),
            lowerY + abs(y - y1),
            lowerZ + abs(z - z1),
        )
        superMaxX = max(abs(x - x1), superMaxX)
        superMaxY = max(abs(y - y1), superMaxY)
        superMaxZ = max(abs(z - z1), superMaxZ)

        brickAreaPopulation = []
        for zz in range(lowerZ, upperZ + 1):
            for xx in range(lowerX, upperX + 1):
                for yy in range(lowerY, upperY + 1):
                    tower[zz][xx][yy] = True
                    brickAreaPopulation.append([zz, xx, yy])

        blueprints.append([lowerZ, brickAreaPopulation])
    blueprints.sort()
    return blueprints, tower, superMaxZ * superMaxY * superMaxZ


def vanishBrick(cubes, tower, undo=True):
    for z, x, y in cubes:
        tower[z][x][y] = not undo


def isBrickSupported(cubes, towerOfGod):
    vanishBrick(cubes, towerOfGod)
    for z, x, y in cubes:
        if z - 1 < 1 or towerOfGod[z - 1][x][y]:
            vanishBrick(cubes, towerOfGod, False)
            return True

    return False


def freeFall(blueprints, towerOfGod, index, stop, isShortFall=False):
    canFreeFall = True
    while canFreeFall:
        blockFell = False
        stop = min(len(blueprints), stop)
        while index < stop:
            # print(i)
            z, cubes = blueprints[index]
            if isBrickSupported(cubes, towerOfGod):
                index += 1
            else:
                for coords in cubes:
                    zz, xx, yy = coords
                    coords[0] = zz - 1
                    towerOfGod[zz - 1][xx][yy] = True
                blockFell = True
                if isShortFall:
                    return True

        if not blockFell:
            canFreeFall = False
    return False


def part1(blueprints, towerOfGod, offset):
    answer = 0
    freeFall(blueprints, towerOfGod, 0, len(blueprints))
    for i in range(len(blueprints)):
        # print(i)
        humanTower = deepcopy(towerOfGod)
        blocks = blueprints[i][1]
        vanishBrick(blocks, humanTower)
        start = i + 1
        stop = i + 1 + offset
        # stop = len(blueprints)
        blockFell = freeFall(blueprints, humanTower, start, stop, True)

        if not blockFell:
            answer += 1
            print("added at >>>>  ", i, " total: ", answer)

    print("answer part 1", answer)
    # 480, 483 too high
    assert answer in [0, 5], "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d22_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")
blueprints, initialTower, offset = init(lines)

# print(blueprints)

part1(blueprints, initialTower, offset)
# part2(input)
