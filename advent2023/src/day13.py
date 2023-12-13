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
    lavas = []
    for line in lines:
        if line:
            lavas.append(line)
        else:
            retval.append(lavas)
            lavas = []

    retval.append(lavas)
    retval = lines if len(retval) == 0 else retval
    return retval


def potentialReflection(lava, isPart2=False):
    retval = None
    for i in range(1, len(lava) - 1):
        if lava[i] == lava[0] or (isPart2 and sameSameButDifferent(lava[i], lava[0])):
            retval = findMirror(0, i, lava, isPart2)
            if retval:
                break

        if lava[i] == lava[-1] or (isPart2 and sameSameButDifferent(lava[i], lava[-1])):
            retval = findMirror(i, len(lava) - 1, lava, isPart2)
            if retval:
                break

    return retval


def sameSameButDifferent(compare1, compare2, strictTolerance=1):
    retval = False
    if len(compare1) == len(compare2):
        offCounter = 0
        for i in range(len(compare1)):
            if offCounter > strictTolerance:
                break
            if compare1[i] != compare2[i]:
                offCounter += 1

        retval = offCounter == 1
    return retval


def findMirror(start, end, lava, isPart2=False):
    retval = None
    middle = start + (end - start) // 2
    compare1 = ""
    compare2 = ""
    for i in range(start, middle + 1):
        compare1 += lava[i]

    for j in range(end, middle, -1):
        compare2 += lava[j]

    if isPart2:
        if compare1 and sameSameButDifferent(compare1, compare2):
            retval = middle + 1
    else:
        if compare1 and compare1 == compare2:
            retval = middle + 1

    return retval


def rotateLava(reflection):
    rotate = []
    for x in range(len(reflection[0])):
        collection = ""
        for y in range(len(reflection)):
            collection += reflection[y][x]
        rotate.append(collection)

    return rotate


def part1(input):
    answer = 0
    verticalRefs = []
    horizontalRefs = []
    for lava in input:
        reflection = potentialReflection(lava)
        if reflection:
            horizontalRefs.append(reflection)
        else:
            lava = rotateLava(lava)
            reflection = potentialReflection(lava)
            verticalRefs.append(reflection)

    print("verticals:", verticalRefs)
    print("horizontals:", horizontalRefs)

    answer = sum(verticalRefs) + sum(horizontalRefs) * 100

    print("answer part 1", answer)
    assert 33195 == answer, "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    verticalRefs = []
    horizontalRefs = []
    for lava in input:
        reflection = potentialReflection(lava, True)
        if reflection:
            horizontalRefs.append(reflection)
        else:
            lava = rotateLava(lava)
            reflection = potentialReflection(lava, True)
            verticalRefs.append(reflection)

    print("verticals:", verticalRefs)
    print("horizontals:", horizontalRefs)

    answer = sum(verticalRefs) + sum(horizontalRefs) * 100
    print("answer part 2", answer)
    assert 31836 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d13_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

part1(input)
part2(input)
