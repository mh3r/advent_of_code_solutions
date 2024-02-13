# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

BROKEN = "#"
QUESTION = "?"
WORKING = "."


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        sampleInput, numbers = line.split(" ")

        retval.append(
            (list(filter(lambda x: x, sampleInput.split("."))), numbers.split(","))
        )
    retval = lines if len(retval) == 0 else retval
    return retval


def part1(input):
    answer = 0

    print("answer part 1", answer)
    assert answer in [7195, 0], "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d12_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))


input = init(lines)
print(*input, sep="\n")

part1(input)
part2(input)

# sampleInput, numbers = lines[1].split(" ")
# test = []

# test.append((list(filter(lambda x: x, sampleInput.split("."))), numbers.split(",")))
# print(test)
