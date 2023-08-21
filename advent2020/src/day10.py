# from parse import *
from functools import reduce
import util
import re
import json
import os


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def part1(lines):
    diff_1 = []
    diff_3 = []

    length = len(lines)
    previous = 0
    for index, jolt in enumerate(lines):
        # if index == length - 1:
        #     diff_3.append(jolt)
        #     break
        if index != 0:
            previous = lines[index - 1]
        if jolt - previous == 1:
            diff_1.append(jolt)
        elif jolt - previous == 3:
            diff_3.append(jolt)
    print("\n\n")
    print(len(diff_1))
    print(len(diff_3) + 1)

    pass


def part2():
    pass


filename = "..\\data\\d10_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: int(x.strip()), lines))
lines.sort()

# print (*lines, sep= "\n")

part1(lines)
part2()
