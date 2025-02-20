# from parse import *
from functools import reduce
from collections import defaultdict
import sys
import re
import json
import os
import types
import math
from functools import cache


sys.path.append(os.getcwd() + "\py-util")
import util


def switchToTest():
    global filename
    print("Testing ... ")
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:

        if "," in line:
            stripes.update(line.split(", "))
        elif len(line) > 0:
            patterns.append(line.strip())

        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    practicalPatterns = []
    for pattern in patterns:
        if isPractical(pattern):
            practicalPatterns.append(pattern)
            answer += 1

    patterns.clear()
    patterns.extend(practicalPatterns)
    print("answer part 1:", answer)
    assert answer in [6, 313], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    for pattern in patterns:
        answer += waysToCreateCurry(pattern)

    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def isPractical(pattern):

    subPatterns = [pattern]
    analysed = []
    for subPattern in subPatterns:
        for stripe in stripes:
            if subPattern.startswith(stripe):
                tmp = subPattern[len(stripe) :]
                if len(tmp) == 0:
                    return True
                else:
                    if tmp not in analysed:
                        analysed.append(tmp)
                        subPatterns.append(tmp)

    return False


@cache
def waysToCreateCurry(pattern):
    retval = 0
    if len(pattern) == 0:
        return 1
    for stripe in stripes:
        if pattern.startswith(stripe):
            tmp = pattern[len(stripe) :]
            retval += 1 * waysToCreateCurry(tmp)

    return retval


filename = "..\\data\\d19_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")
stripes = set()
patterns = []
input = init(lines)

part1()
part2()
