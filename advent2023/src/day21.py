# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

plots = []
barriers = []
ADJ_DIRS = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for y, line in enumerate(lines):
        for x, char in enumerate([*line]):
            if char == "#":
                barriers.append([y, x])
            elif char == "S":
                plots.append([y, x])
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def adventure(steps):
    for i in range(steps):
        newPlots = []
        for plot in plots:
            y, x = plot
            for dy, dx in ADJ_DIRS:
                newY = y + dy
                newX = x + dx
                coord = [newY, newX]

                ## use this to limit this box
                # if newY < 0 or newY == sideLength or newX < 0 or newX == sideLength:
                #     continue

                if (
                    [newY % sideLength, newX % sideLength] not in barriers
                    # coord not in barriers
                    # and [newY % len(lines), newX % len(lines)] not in barriers
                    and coord not in newPlots
                ):
                    newPlots.append(coord)
        if i > 50:
            print(
                i + 1,
                len(
                    list(
                        filter(
                            lambda coord: coord[1] >= 0
                            and coord[1] < sideLength
                            and coord[0] > -0
                            and coord[0] < sideLength,
                            newPlots,
                        )
                    )
                ),
            )
        plots.clear()
        plots.extend(newPlots)


def part1(input):
    answer = 0
    steps = 64
    steps = 150
    # steps to solve 26501365

    # print(26501365 // 131)
    # print(202300 * 131 + 65)

    adventure(steps)
    answer = len(plots)
    # plots.sort()
    # print(plots)

    print("answer part 1", answer)
    # assert answer in [0, 16, 3820], "total is wrong " + str(answer)
    pass


# the sample data isnt a good representation of the input data
# there is no rocks vertically and horizontally from the starting point in the input
# so we can predict how many boxes are filled in and how many partially
# day vs plots framed for 131x131 - it took 131 days before it gets fully filled in
"""129 7654
130 7668
131 7654
132 7668
133 7654
134 7668
135 7654
136 7668
137 7654
138 7668
139 7654
140 7668
141 7654
142 7668
143 7654
144 7668
145 7654
146 7668"""


def part2(input):
    answer = 0

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d21_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))
sideLength = len(lines)

input = init(lines)

print(len(barriers))
# print(plots)
# print(len(lines), len(lines[0]))

# part1(input)
# part2(input)
