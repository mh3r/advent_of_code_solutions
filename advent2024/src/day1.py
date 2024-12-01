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


def part1(list1, list2):
    answer = 0
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        answer += abs(list1[i] - list2[i])

    print("answer part 1", answer)
    assert answer in [1830467], "total is wrong " + str(answer)
    pass

def part2(list1, list2):
    answer = 0

    for i in range(len(list1)):
        first = list1[i]
        multiplier = list2.count(first)
        answer += first * multiplier

    print("answer part 2", answer)
    assert answer in [26674158], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d1_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

list1 = []
list2 = []

for line in lines:
    splitted = line.split()
    list1.append(int(splitted[0]))
    list2.append(int(splitted[1]))

part1(list1[:], list2[:])
part2(list1[:], list2[:])
