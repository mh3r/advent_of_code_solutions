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
    global moves
    global startCoord
    retval = []
    for i in range(len(lines)):
        line = lines[i]
        if len(line) > 0:
            if "<" in line:
                moves.extend(list(line))
            else:
                board.append(list(line))
                if "@" in line:
                    x = line.index(START)
                    startCoord = (i, x)
                    # board[i][x] = EMPTY

        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    boardCopy = board[:]
    startCoordCopy = startCoord[:]
    pushItOut(startCoordCopy, boardCopy, moves)

    for y in range(len(boardCopy)):
        for x in range(len(boardCopy[0])):
            if boardCopy[y][x] == BOX:
                answer += 100 * y + x

    print("answer part 1:", answer)
    assert answer in [10092, 1471826], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def pushItOut(startCoord, boardCopy, moves):
    y, x = startCoord

    for move in moves:

        dy, dx = translateMove(move)
        newY = y + dy
        newX = x + dx

        if boardCopy[newY][newX] == WALL:
            continue
        if boardCopy[newY][newX] == EMPTY:
            boardCopy[newY][newX] = START
            boardCopy[y][x] = EMPTY

            y = newY
            x = newX
            continue
        if boardCopy[newY][newX] == BOX:

            if y == 1 and x == 4:
                debug = 1

            boxesAhead = canPushBox(y, x, dy, dx, boardCopy)

            if boxesAhead > 0:
                boardCopy[y][x] = EMPTY

                y = newY
                x = newX
                boardCopy[newY][newX] = START

                emptyY = dy * boxesAhead
                emptyX = dx * boxesAhead

                boardCopy[newY + emptyY][newX + emptyX] = BOX

            continue

    print("the bot -- ", y, x)


def canPushBox(y, x, dy, dx, boardCopy):
    retval = 0
    boxesAhead = 0
    index = x
    sandBox = boardCopy[y]

    if dx == -1:
        sandBox = boardCopy[y][::-1]
        index = len(sandBox) - x - 1

    if dy == 1:
        sandBox = list(zip(*boardCopy[::-1]))[x][::-1]
        index = y

    if dy == -1:
        sandBox = list(zip(*boardCopy[::-1]))[x]

        index = len(sandBox) - y - 1

    for i in range(1, len(sandBox) - index):
        if sandBox[i + index] == BOX:
            boxesAhead += 1
        else:
            break

    expectedEmpyIndex = index + boxesAhead + 1
    if expectedEmpyIndex < len(sandBox) - 1 and sandBox[expectedEmpyIndex] == EMPTY:
        retval = expectedEmpyIndex - 1 - index

    return retval


def translateMove(move):

    if move == "<":
        return [0, -1]

    if move == ">":
        return [0, 1]

    if move == "^":
        return [-1, 0]

    if move == "v":
        return [1, 0]


filename = "..\\data\\d15_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

START = "@"
BOX = "O"
WALL = "#"
EMPTY = "."

startCoord = None
board = []
moves = []
input = init(lines)

part1()
part2()
