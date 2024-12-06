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
        retval.append(list(line))

    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    pos = startPos

    dir = 0
    uniqueSteps = {util.stringifyCoord(pos)}
    while True:

        newY = pos[0] + STEPS[dir][0]
        newX = pos[1] + STEPS[dir][1]

        if newY not in range(len(input)) or newX not in range(len(input[0])):
            break

        if input[newY][newX] == "#":
            dir = (dir + 1) % len(STEPS)
        else:
            pos = [newY, newX]
            print(newY, newX)
            uniqueSteps.add(util.stringifyCoord(pos))

    answer = len(uniqueSteps)
    print("answer part 1:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    for i in range(len(input)):
        for j in range(len(input[0])):
            char = input[i][j]
            if char == "#" or (i == startPos[0] and j == startPos[1]):
                continue

            newInput = [row[:] for row in input]
            newInput[i][j] = "#"
            answer += isIndefinite(newInput)
 
    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def isIndefinite(input):
    pos = startPos
    dir = 0
    uniqueSteps = {util.stringifyCoord(pos) + "_" + str(dir)}
    while True:

        newY = pos[0] + STEPS[dir][0]
        newX = pos[1] + STEPS[dir][1]

        if newY not in range(len(input)) or newX not in range(len(input[0])):
            break

        if input[newY][newX] == "#":
            dir = (dir + 1) % len(STEPS)
        else:
            pos = [newY, newX]
            # print(newY, newX)
            oldSteps = len(uniqueSteps)
            uniqueSteps.add(util.stringifyCoord(pos) + "_" + str(dir))
            if oldSteps == len(uniqueSteps):
                return 1

    return 0


filename = "..\\data\\d6_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

startPos = []
STEPS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(len(input)):
    for j in range(len(input[0])):
        char = input[i][j]
        if char == "^":
            startPos = [i, j]
            break


'''
part 2 is brute force ... definitely needs fixing :) 

'''

part1()
part2()
