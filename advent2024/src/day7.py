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
        l, r = line.split(":")
        retval.append([int(l), r])
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    for equation in input:
        if determineValidEquation(equation):
            answer += equation[0]
    print("answer part 1:", answer)
    assert answer in [3749, 5512534574980], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    for equation in input:
        if determineValidEquation(equation, False):
            answer += equation[0]
    print("answer part 2:", answer)
    assert answer in [11387, 328790210468594], "answer is wrong " + str(answer)
    pass


def determineValidEquation(equation, isPart1=True):
    lhs = int(equation[0])
    rhs = equation[1].split()
    currentTotals = [int(rhs.pop(0))]
    tmpTotals = []

    while len(rhs) > 0:
        current = int(rhs.pop(0))

        for currentTotal in currentTotals:
            plus = currentTotal + current
            mult = currentTotal * current
            if plus <= lhs:
                tmpTotals.append(plus)

            if mult <= lhs:
                tmpTotals.append(mult)
            if not isPart1:
                combine = int(str(currentTotal) + str(current))
                if combine <= lhs:
                    tmpTotals.append(combine)

        currentTotals = tmpTotals[:]
        tmpTotals.clear()

    for currentTotal in currentTotals:
        if lhs == currentTotal:
            return True

    return False


filename = "..\\data\\d7_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

operations = ["+", "*"]
operations_2 = ["+", "*", ""]

input = init(lines)

"""
NOTE dont do eval ... eval is evil 
"""

part1()
part2()
