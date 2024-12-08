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
        if determineValidEquation(equation, operations):
            answer += equation[0]
    print("answer part 1:", answer)
    assert answer in [3749, 5512534574980], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    for equation in input:
        if determineValidEquation(equation, operations_2):
            answer += equation[0]

    print("answer part 2:", answer)
    assert answer in [11387, 328790210468594], "answer is wrong " + str(answer)
    pass


def determineValidEquation(equation, operations):
    lhs = equation[0]
    rhs = equation[1].split()
    potentialEquations = [rhs.pop(0)]

    while len(rhs) > 0:
        current = rhs.pop(0)
        tmpPotEqs = []

        for potentialEquation in potentialEquations:
            for operation in operations:
                tmpPotEqs.append(str(potentialEquation) + operation)

        potentialEquations.clear()
        for tmpPotEq in tmpPotEqs:

            value = eval(tmpPotEq + current)

            if value <= lhs:
                potentialEquations.append(value)

    for potentialEquation in potentialEquations:
        if lhs == potentialEquation:
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

'''
TODO dont do eval ... eval is evil 
takes too long ... just do calculation straight away 

'''

part1()
part2()
