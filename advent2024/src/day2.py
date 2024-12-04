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
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0

    for list in listing:
        answer += isSafe(list)

    print("answer part 1", answer)
    assert answer in [407], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    for list in listing:
        answer += isLooselySafe(list)

    print("answer part 2", answer)
    assert answer in [459], "answer is wrong " + str(answer)
    pass


# this was first attempt
# trying to jump and use 123081203 diff methods instead of having a plan
def isSafe_unused(input):

    stringifiedInput = "_".join(list(map(str, input)))
    listSorted = input[:]
    listSorted.sort()
    sorted = "_".join(list(map(str, listSorted)))
    reversedSOrted = input[:]
    reversedSOrted.sort(reverse=True)

    reversed = "_".join(list(map(str, reversedSOrted)))

    if stringifiedInput != sorted and stringifiedInput != reversed:
        return 0

    for i in range(len(input) - 1):
        current = input[i]
        next = input[i + 1]

        absDiff = abs(current - next)
        if absDiff < 1 or absDiff > 3:
            return 0

    return 1


def isSafe(input):
    # we rely on the first pair to determine sign
    if input[0] < input[1]:
        input.reverse()

    safeRange = list(range(1, 4))

    for i in range(len(input) - 1):
        if input[i] - input[i + 1] not in safeRange:
            return 0
    return 1


def isLooselySafe(input):

    if isSafe(input) == 1:
        return 1

    for i in range(len(input)):
        newList = input[:]
        del newList[i]

        if isSafe(newList):
            return 1

    return 0


filename = "..\\data\\d2_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

listing = []
for line in lines:
    splitted = line.split()
    listing.append(list(map(int, splitted)))


safeRange = list(range(1, 4))
part1()
part2()
