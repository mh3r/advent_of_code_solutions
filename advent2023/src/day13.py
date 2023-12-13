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
    starts = []
    stops = []
    for i in range(len(lava) - 1):
        for j in range(len(lava) - 1, 0, -1):
            if lava[i] == lava[j] and i != j and j not in starts:
                starts.append(i)
                stops.append(j)

    startsCopy = starts.copy()
    stopsCopy = stops.copy()

    while starts and stops:
        allRanges = list(set(starts + stops))
        allRanges.sort()
        minValue = min(allRanges)
        maxValue = max(allRanges)
        if (minValue == 0 or maxValue == len(lava) - 1) and allRanges == list(
            range(minValue, maxValue + 1)
        ):
            retval = starts[-1] + 1
        starts.pop(0)
        stops.pop(0)

    while startsCopy and stopsCopy:
        allRanges = list(set(startsCopy + stopsCopy))
        allRanges.sort()
        minValue = min(allRanges)
        maxValue = max(allRanges)
        if (minValue == 0 or maxValue == len(lava) - 1) and allRanges == list(
            range(minValue, maxValue + 1)
        ):
            retval = startsCopy[-1] + 1
        startsCopy.pop()
        stopsCopy.pop()

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

    print(verticalRefs)
    print(horizontalRefs)
    
    answer  = sum(verticalRefs) + sum(horizontalRefs) * 100

    print("answer part 1", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    print("answer part 2", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d13_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)

# part1(input)
part2(input)

print(*input, sep="\n")


print(potentialReflection(rotateLava(input[0])))
