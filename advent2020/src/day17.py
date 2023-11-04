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


def findExtremeties(inputMap):
    axis = []
    for i in range(0, inputMap[0].count("_") + 1):
        axis.append([])
    for coord in inputMap:
        splitted = coord.split("_")
        for i in range(0, len(splitted)):
            axis[i].append(int(splitted[i]))
    # print(axis)
    retval = []
    for axe in axis:
        retval.append([min(axe) - 1, max(axe) + 1])
    return retval


def populateNeighbours(coord, isPart2):
    splitted = coord.split("_")
    neighbours = []
    for x in range(-1 + int(splitted[0]), 2 + int(splitted[0])):
        for y in range(-1 + int(splitted[1]), 2 + +int(splitted[1])):
            for z in range(-1 + +int(splitted[2]), 2 + int(splitted[2])):
                if isPart2:
                    for a in range(-1 + +int(splitted[3]), 2 + int(splitted[3])):
                        tmp = "{0}_{1}_{2}_{3}".format(x, y, z, a)
                        if tmp != coord:
                            neighbours.append(tmp)
                else:
                    tmp = "{0}_{1}_{2}".format(x, y, z)
                    if tmp != coord:
                        neighbours.append(tmp)
    return neighbours


def countActiveNeighbours(coord, inputMap, isPart2):
    neighbours = populateNeighbours(coord, isPart2)
    return len(list((filter(lambda x: x in inputMap, neighbours))))


def isActive(coord, inputMap, isPart2):
    activeNeighbours = countActiveNeighbours(coord, inputMap, isPart2)
    return (
        activeNeighbours == 2 or activeNeighbours == 3
        if coord in inputMap
        else activeNeighbours == 3
    )


def populatePoi(extremities, isPart2):
    poiSet = set()
    for x in range(extremities[0][0], extremities[0][1] + 1):
        for y in range(extremities[1][0], extremities[1][1] + 1):
            for z in range(extremities[2][0], extremities[2][1] + 1):
                if isPart2:
                    for a in range(extremities[3][0], extremities[3][1] + 1):
                        poiSet.add("{0}_{1}_{2}_{3}".format(x, y, z, a))
                else:
                    poiSet.add("{0}_{1}_{2}".format(x, y, z))
    return poiSet


def cycle(inputMap, isPart2=False):
    extremeties = findExtremeties(inputMap)
    pointsOfInterest = populatePoi(extremeties, isPart2)
    newInputMap = []

    for poi in pointsOfInterest:
        if isActive(poi, inputMap, isPart2):
            newInputMap.append(poi)
    return newInputMap


def part1(inputMap):
    for i in range(0, 6):
        inputMap = cycle(inputMap)
    print(len(inputMap))
    pass


def part2(lines):
    inputMap = []
    y = 0
    z = 0
    a = 0
    for line in lines:
        for i in range(0, len(line.strip())):
            if line[i] == ACTIVE:
                inputMap.append("{0}_{1}_{2}_{3}".format(i, y, z, a))
        y += 1

    print(inputMap)
    for i in range(0, 6):
        inputMap = cycle(inputMap, True)
    print(len(inputMap))
    pass


filename = "..\\data\\d17_input.txt"
ACTIVE = "#"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

inputMap = []

y = 0
z = 0
for line in lines:
    for i in range(0, len(line.strip())):
        if line[i] == ACTIVE:
            inputMap.append("{0}_{1}_{2}".format(i, y, z))
    y += 1


# print(inputMap)

# part1(inputMap)
part2(lines)
