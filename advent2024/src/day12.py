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
        retval.append(list(line))
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    parsed = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if (y, x) in parsed:
                continue
            occupiedPlants = markOccupiedPlants(y, x, parsed)
            answer += calculatePerimeter(occupiedPlants)

    print("answer part 1:", answer)
    assert answer in [1930, 1433460], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    parsed = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if (y, x) in parsed:
                continue
            occupiedPlants = markOccupiedPlants(y, x, parsed)
            answer += calculateDiscPerimeter(occupiedPlants)

    print("answer part 2:", answer)
    assert answer in [1206, 855082], "answer is wrong " + str(answer)
    pass


def markOccupiedPlants(startingY, startingX, parsed):
    targetCharacter = input[startingY][startingX]

    paths = [(startingY, startingX)]
    occupiedPlants = []
    while len(paths) > 0:
        curY, curX = paths.pop()

        occupiedPlants.append((curY, curX))

        for dy, dx in util.ADJ_DIRS:
            nextY = curY + dy
            nextX = curX + dx

            if (
                nextY not in range(len(input))
                or nextX not in range(len(input[0]))
                or (nextY, nextX) in occupiedPlants
                or (nextY, nextX) in paths
            ):
                continue

            if input[nextY][nextX] == targetCharacter:
                paths.append((nextY, nextX))

    occupiedPlants.sort()
    parsed.extend(occupiedPlants)
    return occupiedPlants


def calculatePerimeter(occupiedPlants):
    boundaries = 0
    for plant in occupiedPlants:
        plantY, plantX = plant

        if (plantY, plantX - 1) not in occupiedPlants:
            boundaries += 1
        if (plantY, plantX + 1) not in occupiedPlants:
            boundaries += 1
        if (plantY - 1, plantX) not in occupiedPlants:
            boundaries += 1
        if (plantY + 1, plantX) not in occupiedPlants:
            boundaries += 1

    retval = boundaries * len(occupiedPlants)
    print(retval)
    return retval


def calculateDiscPerimeter(occupiedPlants):
    sides = 0

    lrCoords = []
    lrCoords2 = []
    tdCoords = []
    tdCoords2 = []

    for plant in occupiedPlants:
        plantY, plantX = plant

        # left
        if (plantY, plantX - 1) not in occupiedPlants:
            lrCoords.append((plantY, plantX - 1))
        # right
        if (plantY, plantX + 1) not in occupiedPlants:
            lrCoords2.append((plantY, plantX + 1))
        # top ... the switched the y n x orientation for easy simplify sides
        if (plantY - 1, plantX) not in occupiedPlants:
            tdCoords.append((plantX, plantY - 1))
        # bottom
        if (plantY + 1, plantX) not in occupiedPlants:
            tdCoords2.append((plantX, plantY + 1))

    sides += simplifySides(lrCoords)
    sides += simplifySides(lrCoords2)
    sides += simplifySides(tdCoords)
    sides += simplifySides(tdCoords2)

    retval = sides * len(occupiedPlants)
    print(retval)
    return retval


def simplifySides(lrCoords):
    sides = 0

    while len(lrCoords) > 0:
        y, x = lrCoords.pop()
        sides += 1

        for i in range(1, len(lrCoords) + 1):
            newY = y + i
            if (newY, x) in lrCoords:
                lrCoords.remove((newY, x))
            else:
                break

        for i in range(1, len(lrCoords) + 1):
            newY = y - i
            if (newY, x) in lrCoords:
                lrCoords.remove((newY, x))
            else:
                break

    return sides


filename = "..\\data\\d12_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

part1()
part2()
