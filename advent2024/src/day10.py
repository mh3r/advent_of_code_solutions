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
    global answer1
    global answer2

    retval = []
    starters = []

    for line in lines:
        retval.append(list(map(int, list(line))))
    retval = lines if len(retval) == 0 else retval

    for i in range(len(retval)):
        for j in range(len(retval[0])):
            if retval[i][j] == 0:
                starters.append([i, j])

    for y, x in starters:
        answers = hillCounter(y, x, retval)
        answer1 += answers[0]
        answer2 += answers[1]

    return retval


def part1():
    answer = 0

    answer = answer1
    print("answer part 1:", answer)
    assert answer in [36, 822], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    answer = answer2

    print("answer part 2:", answer)
    assert answer in [81, 1801], "answer is wrong " + str(answer)
    pass


def hillCounter(y, x, input):
    hills = []
    paths = [[y, x, 0]]

    while len(paths) > 0:
        path = paths.pop()
        y, x, current = path
        current += 1
        for dy, dx in util.ADJ_DIRS:
            newY = y + dy
            newX = x + dx

            if newY not in range(len(input)) or newX not in range(len(input[0])):
                continue

            if input[newY][newX] == current:
                if current == 9:
                    hills.append((newY, newX))
                    continue

                paths.append([newY, newX, current])

    return len(list(set(hills))), len(hills)


filename = "..\\data\\d10_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")


answer1 = 0
answer2 = 0

input = init(lines)

part1()
part2()
