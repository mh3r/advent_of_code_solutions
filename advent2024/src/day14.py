# from parse import *
from functools import reduce
from collections import defaultdict
import sys
import re
import json
import os
import types
import math
from operator import mul

sys.path.append(os.getcwd() + "\py-util")
import util


def switchToTest():
    global filename
    print("Testing ... ")
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []

    for line in lines:
        line = line.replace("p=", "")
        firstSplit = line.split(" v=")
        robotPos = list(map(int, firstSplit[0].split(",")))
        robotSpeed = list(map(int, firstSplit[1].split(",")))
        retval.append([robotPos, robotSpeed])
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    robots = input[:]
    steps = 100
    
    width = 11
    height = 7

    width = 101
    height = 103

    occupiers = [0, 0, 0, 0]

    for instruction in robots:
        quadrant = move(instruction, steps, width, height)
        if quadrant > 0:
            occupiers[quadrant - 1] += 1

    print(occupiers)
    answer = reduce(mul, occupiers)
    print("answer part 1:", answer)
    assert answer in [12, 219150360], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    inputCopy = input[:]

    bots = []
    moves = []
    for tmp in inputCopy:

        bots.append(tmp[0])
        moves.append(tmp[1])

    stepCounter = 0
    width = 101
    height = 103

    while True:
        for i in range(len(bots)):
            x, y = bots[i]
            dx, dy = moves[i]

            bots[i] = [(x + dx) % width, (y + dy) % height]

        stepCounter += 1

        if isPotentialTree(bots, 3):
            drawBots(bots)

            debug = 1

        # takes a while to see the picture
        break
    print("answer part 2:", answer)
    # assert answer in [0, 8053], "answer is wrong " + str(answer)
    pass


def move(instruction, steps, width, height):
    [rx, ry], [dx, dy] = instruction

    for i in range(steps):
        rx = (rx + dx) % width
        ry = (ry + dy) % height

    midY = int(height / 2)
    midX = int(width / 2)

    quadrant = 0

    if ry < midY:
        if rx < midX:
            quadrant = 1
        elif rx > midX:
            quadrant = 2
    if ry > midY:
        if rx < midX:
            quadrant = 4
        elif rx > midX:
            quadrant = 3

    return quadrant


def drawBots(bots):
    print("-------------------------------------------------------")
    print("\n\n")

    board = [[" "] * 101 for i in range(103)]

    for bot in bots:
        x, y = bot

        board[y][x] = "o"

    for line in board:
        print("".join(line))

    pass


def isPotentialTree(bots, dimension):

    for bot in bots:
        x, y = bot
        spotToCheck = []
        for i in range(0, dimension):
            spotToCheck.append([x + i, y])
            for j in range(1, dimension):
                spotToCheck.append([x + i, y + j])
        huh = 1
        if all(spot in bots for spot in spotToCheck):
            return True
    return False


filename = "..\\data\\d14_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

part1()
# part2()
