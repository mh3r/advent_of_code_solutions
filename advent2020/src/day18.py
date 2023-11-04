# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

PLUS = "+"


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def evaluate(input):
    input = input.replace("(", "").replace(")", "")
    splitted = input.split()
    while len(splitted) > 1:
        value = str(eval(splitted.pop(0) + splitted.pop(0) + splitted.pop(0)))
        splitted.insert(0, value)
    return str(splitted[0])


def evaluatePart2(input):
    input = input.replace("(", "").replace(")", "")
    splitted = input.split()

    while len(splitted) > 1:
        while PLUS in splitted:
            index = splitted.index(PLUS)
            value = str(
                eval(
                    splitted.pop(index - 1)
                    + splitted.pop(index - 1)
                    + splitted.pop(index - 1)
                )
            )
            splitted.insert(index - 1, value)
        if len(splitted) > 1:
            value = str(eval(splitted.pop(0) + splitted.pop(0) + splitted.pop(0)))
            splitted.insert(0, value)
    return str(splitted[0])


def findOpeningPair(openIndex, closeIndex):
    retval = None
    smallest = 100000000000
    targetIndex = closeIndex[0]
    for index in openIndex:
        diff = targetIndex - index
        if diff < smallest and diff > 0:
            smallest = diff
            retval = index
    return [retval, targetIndex]


def process(input, isPart2=False):
    while "(" in input:
        openIndex = [m.start() for m in re.finditer("\(", input)]
        closeIndex = [m.start() for m in re.finditer("\)", input)]
        firstPair = findOpeningPair(openIndex, closeIndex)

        middlePart = (
            evaluatePart2(input[firstPair[0] : firstPair[1] + 1])
            if isPart2
            else evaluate(input[firstPair[0] : firstPair[1] + 1])
        )
        input = input[: firstPair[0]] + middlePart + input[firstPair[1] + 1 :]

    return int(evaluatePart2(input)) if isPart2 else int(evaluate(input))


def part1():
    sums = []
    for line in lines:
        sums.append(process(line))

    print(sums)
    print("Total:", sum(sums))
    pass


def part2():
    sums = []
    for line in lines:
        sums.append(process(line, True))

    print(sums)
    print("Total:", sum(sums))
    pass


filename = "..\\data\\d18_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

# part1()
part2()
