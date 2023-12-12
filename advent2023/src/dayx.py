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
    for line in lines:
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1(input):
    answer = 0
    print("answer part 1", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    print("answer part 2", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\dx_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)

part1(input)
part2(input)
