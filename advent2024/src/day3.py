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
    mulMatches = re.findall(mulPattern, input)

    for match in mulMatches:
        answer += int(match[0]) * int(match[1])
    print("answer part 1", answer)
    assert answer in [161, 155955228], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    grouping = re.finditer(anyPattern, input)

    isOperate = True
    for match in grouping:
        action = match.group()

        if "don" in action:
            isOperate = False
        elif "do" in action:
            isOperate = True
        elif isOperate:
            theValue = action.replace("mul(", "").replace(")", "")
            splitted = theValue.split(",")
            first = int(splitted[0])
            second = int(splitted[1])
            answer += first * second

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
input = "".join(input)

mulPattern = r"mul\((\d+),(\d+)\)"
anyPattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"

part1()
part2()
