# from parse import *
from functools import reduce
from collections import defaultdict
import util
import re
import json
import os
import types
import math
import random


ADJ_DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
DIR_CHARS = [">", "<", "v", "^"]
DOT = "."


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    intersections = []
    isPart2 = True
    retval = []
    start, end = [], []
    for y, line in enumerate(lines):
        tmpLine = []

        for x, char in enumerate([*line]):
            if isPart2 and char in DIR_CHARS:
                char = "."
            tmpLine.append(char)
            if y == 0 and char == ".":
                start = [y, x]
            elif y == len(line) - 1 and char == ".":
                end = [y, x]
        retval.append(tmpLine)
    retval = lines if len(retval) == 0 else retval

    for y in range(len(retval)):
        for x in range(len(retval[0])):
            if retval[y][x] == DOT:
                neighbourCounter = 0
                for [dy, dx] in util.ADJ_DIRS:
                    newY = y + dy
                    newX = x + dx
                    if (
                        0 > newY
                        or newY >= len(retval)
                        or 0 > newX
                        or newX >= len(retval[0])
                    ):
                        continue
                    nextChar = retval[newY][newX]
                    if nextChar == DOT:
                        neighbourCounter += 1
                if neighbourCounter > 2:
                    intersections.append([y, x])
                    if neighbourCounter == 4:
                        print("wowser ", [y, x])
    print(intersections)

    return retval, start, end


def gogo(maze, start, end):
    ends = []
    paths = [[start]]
    counter = 0
    currentMax = 0
    while paths:
        # number = random.randint(1, 10)
        # if number > 5:
        seen = paths.pop()
        # else:
        #     seen = paths.pop(0)
        current = seen[-1]
        while True:
            y, x = current
            # if y == 5:
            #     debugit = 1

            possibleSteps = []
            for i, [dy, dx] in enumerate(util.ADJ_DIRS):
                newY = y + dy
                newX = x + dx
                if (
                    0 > newY
                    or newY > len(maze) - 1
                    or 0 > newX
                    or newX > len(maze[0]) - 1
                    or [newY, newX] in seen
                ):
                    continue
                nextChar = maze[newY][newX]
                if (
                    nextChar == "."
                    or nextChar in DIR_CHARS
                    # and i == DIR_CHARS.index(nextChar)
                ):
                    possibleSteps.append([newY, newX])

            if len(possibleSteps) == 0:
                break
            elif len(possibleSteps) > 1:
                # print(current)
                for step in possibleSteps:
                    paths.append(seen + [step])
                break
            else:
                current = possibleSteps[0]
                seen.append(possibleSteps[0])

                if current == end:
                    currentMax = max(currentMax, len(seen) - 1)
                    ends.append(seen)
                    break
        counter += 1

        if counter % 500 == 0:
            print("currentMax", currentMax)

    return ends


def part1(maze, start, end):
    answer = 0
    ends = gogo(maze, start, end)

    for end in ends:
        answer = max(answer, len(end) - 1)
    print("answer part 1", answer)
    assert answer in [0, 94, 2042], "total is wrong " + str(answer)
    pass


def part2(maze, start, end):
    answer = 0
    ends = gogo(maze, start, end)

    for end in ends:
        answer = max(answer, len(end) - 1)
    print("answer part 1", answer)
    assert answer in [0, 154], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d23_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input, start, end = init(lines)


# part1(input, start, end)
part2(input, start, end)

# for i in range(13):
#     number = random.randint(0, 1)
#     print(number)
