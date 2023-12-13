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


def potentialReflection(lava):
    retval = None
    for i in range(1, len(lava) - 1):
        if lava[i] == lava[0]:
            retval = findMirror(0, i, lava)
            if retval:
                break

        if lava[i] == lava[-1]:
            retval = findMirror(i, len(lava) - 1, lava)
            if retval:
                break

    return retval


def findMirror(start, end, lava):
    retval = None
    middle = start + (end - start) // 2
    compare1 = ""
    compare2 = ""
    for i in range(start, middle + 1):
        compare1 += lava[i]
        # print("i:", i)

    for j in range(end, middle, -1):
        compare2 += lava[j]
        # print("j:", j)

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
    print("answer part 2", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
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
