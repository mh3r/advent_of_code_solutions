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
    global dimension
    print("Testing ... ")
    filename = "..\\data\\test.txt"
    dimension = 7


def init(lines):
    retval = []
    for line in lines:
        splitted = line.split(",")
        retval.append((int(splitted[1]), int(splitted[0])))
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1(allCorrupted):
    answer = 0

    limit = 1024
    if "test" in filename:
        limit = 12

    ideals = {start: 1, end: math.inf}
    blocks = allCorrupted[0:limit]

    runner(ideals, blocks)

    answer = ideals[end]
    print("answer part 1:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def runner(ideals, blocks):

    paths = [start]

    while len(paths) > 0:

        path = paths.pop(0)

        # check if end is reached
        if path == end:
            return

        # traverse box ADJ_DIRS

        for dir in util.ADJ_DIRS:
            newY = path[0] + dir[0]
            newX = path[1] + dir[1]

            if (
                newY in range(dimension)
                and newX in range(dimension)
                and (newY, newX) not in blocks
            ):
                if (newY, newX) not in ideals:
                    ideals[(newY, newX)] = ideals[path] + 1
                    paths.append((newY, newX))
                elif ideals[(newY, newX)] > ideals[path] + 1:
                    ideals[(newY, newX)] = ideals[path] + 1
                    paths.append((newY, newX))



        # sort by score manhattanDistance
        pass

    pass

def cmpAStarScore()


filename = "..\\data\\d18_input.txt"
dimension = 71
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

start = (0, 0)
end = (dimension - 1, dimension - 1)


part1(input[:])
part2()
