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
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    pattern = r"mul\((\d+),(\d+)\)"
    grouping = re.findall(pattern, input[0])

    print(grouping)

    for group in grouping:
        first = int(group[0])
        second = int(group[1])
        answer += first * second
    print("answer part 1", answer)
    assert answer in [161, 155955228], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    pattern = r"mul\((\d+),(\d+)\)"
    grouping = re.finditer(pattern, input[0])

    numbers = []
    for group in grouping:
        numbers.append([group.start(), group.group()])

    # print(numbers)

    doPattern = r"(do\(\))"
    dontPattern = r"(don't\(\))"
    doMatches = re.finditer(doPattern, input[0])
    dontMatches = re.finditer(dontPattern, input[0])

    doInstructions = [0]

    for do in doMatches:
        doInstructions.append(do.start())

    dontInstructions = [0]

    for dont in dontMatches:
        dontInstructions.append(dont.start())

    for possibleMul in numbers:
        pos = possibleMul[0]

        # print (first)
        # print (second)

        lastDoInstruction = list(filter(lambda x: x < pos, doInstructions))[-1]

        lastDontInstruction = list(filter(lambda x: x < pos, dontInstructions))[-1]
        # print("--------------")
        # print(lastDoInstruction)
        # print(lastDontInstruction)

        if lastDoInstruction >= lastDontInstruction:
            theValue = possibleMul[1].replace("mul(", "").replace(")", "")
            splitted = theValue.split(",")
            first = int(splitted[0])
            second = int(splitted[1])
            answer += first * second

    # print(doInstructions)
    # print(dontInstructions)

    print("answer part 2", answer)
    assert answer in [48, 100189366], "answer is wrong " + str(answer)
    pass


filename = "..\\data\\d3_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)


'''
TODO 
clean up 
had to modify input so that its one line 


'''
part1()
part2()
