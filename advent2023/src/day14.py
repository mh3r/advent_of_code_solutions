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
    rocks = []
    blocks = []
    for y, line in enumerate(lines):
        for x, char in enumerate([*line]):
            if char == "O":
                rocks.append([y, x])
            elif char == "#":
                blocks.append([y, x])
    retval = lines if len(retval) == 0 else retval
    return rocks, blocks


def rockCanMove(rock, rocks, blocks):
    y, x = rock
    newCoord = [y - 1, x]
    return y > 0 and newCoord not in rocks and newCoord not in blocks


def part1(rocks, blocks):
    answer = 0

    rocksCopy = rocks.copy()

    while len(rocksCopy) > 0:
        rock = rocksCopy.pop(0)
        isKeepGoing = True
        while  isKeepGoing:
            if rockCanMove(rock, rocks, blocks):
                rocks.remove(rock)
                rock = [rock[0] -1 , rock[1]]
                rocks.append(rock)
            else: 
                isKeepGoing = False

    print(rocks)

     
    for y, x in rocks:
        answer += totalLength - y

    print("answer part 1", answer)
    assert 107053 == answer, "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    print("answer part 2", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d14_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")
totalLength = len(lines)
rocks, blocks = init(lines)
print(rocks)
print(blocks)
part1(rocks, blocks)
part2(input)
