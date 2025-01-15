# from parse import *
import copy
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
                    x = line.index(CURSOR)
                    startCoord = (i, x)
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    boardCopy = copy.deepcopy(board)
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

    newBoard = []
    startCoordCopy = (startCoord[0], 2 * startCoord[1])

    for line in board:
        newLine = []
        for character in line:
            newLine.extend(
                list(
                    character.replace(WALL, "##")
                    .replace(EMPTY, "..")
                    .replace(BOX, "[]")
                    .replace(CURSOR, "@.")
                )
            )
        newBoard.append(newLine)

    pushBulk(startCoordCopy, newBoard, moves)

    for y in range(len(newBoard)):
        for x in range(len(newBoard[0])):
            if newBoard[y][x] == BOXES[0]:
                answer += 100 * y + x

    print("answer part 2:", answer)
    assert answer in [9021, 1457703], "answer is wrong " + str(answer)
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
            boardCopy[newY][newX] = CURSOR
            boardCopy[y][x] = EMPTY

            y = newY
            x = newX
            continue

        if boardCopy[newY][newX] == BOX:
            boxesAhead = canPushBox(y, x, dy, dx, boardCopy)
            if boxesAhead > 0:
                boardCopy[y][x] = EMPTY

                y = newY
                x = newX
                boardCopy[newY][newX] = CURSOR

                emptyY = dy * boxesAhead
                emptyX = dx * boxesAhead

                boardCopy[newY + emptyY][newX + emptyX] = BOX
            continue


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


def pushBulk(startCoord, boardCopy, moves):
    y, x = startCoord
    for move in moves:
        # util.printBoard(boardCopy)
        # print("Move: ", move)
        dy, dx = translateMove(move)
        newY = y + dy
        newX = x + dx

        if boardCopy[newY][newX] == WALL:
            continue
        if boardCopy[newY][newX] == EMPTY:
            boardCopy[newY][newX] = CURSOR
            boardCopy[y][x] = EMPTY

            y = newY
            x = newX
            continue
        if boardCopy[newY][newX] in BOXES:

            if tryPushBoxes(y, x, dy, dx, boardCopy):
                boardCopy[y][x] = EMPTY

                y = newY
                x = newX
                boardCopy[newY][newX] = CURSOR

            continue

    # util.printBoard(boardCopy)


def tryPushBoxes(y, x, dy, dx, boardCopy):
    if dy == 0:
        return tryPushHorizontalBoxes(y, x, dx, boardCopy)
    else:
        return tryPushVerticalBoxes(y, x, dy, boardCopy)


def tryPushHorizontalBoxes(y, x, dx, boardCopy):
    retval = False

    affectedBoxes = []
    if boardCopy[y][x + dx] == BOXES[0]:
        affectedBoxes.append((y, x + dx))
    else:
        affectedBoxes.append((y, x + dx - 1))

    boxesToInvestigate = affectedBoxes[:]
    xs = [affectedBoxes[0][1]]

    while len(boxesToInvestigate) > 0:
        currentBox = boxesToInvestigate.pop()
        cx = currentBox[1]

        newX = cx + 2 * dx

        if newX in range(len(boardCopy[0])) and boardCopy[y][newX] == BOXES[0]:
            xs.append(newX)
            boxesToInvestigate.append((y, newX))
            affectedBoxes.append((y, newX))

    if dx > 0:
        xComparison = max(xs)
        if boardCopy[y][xComparison + 2 * dx] == EMPTY:
            retval = True

    else:
        xComparison = min(xs)
        if boardCopy[y][xComparison + dx] == EMPTY:
            retval = True

    if retval:
        for box in affectedBoxes:
            bx = box[1]
            boardCopy[y][bx + dx] = BOXES[0]
            boardCopy[y][bx + dx + 1] = BOXES[1]

    return retval


def tryPushVerticalBoxes(y, x, dy, boardCopy):
    retval = True
    affectedBoxes = []
    BOXES_AND_EMTPY = BOXES + [EMPTY]

    if boardCopy[y + dy][x] == BOXES[0]:
        affectedBoxes.append((y + dy, x))
    else:
        affectedBoxes.append((y + dy, x - 1))

    boxesToInvestigate = affectedBoxes[:]

    while len(boxesToInvestigate) > 0:
        currentBox = boxesToInvestigate.pop()
        cy, cx = currentBox

        newY = cy + dy

        if boardCopy[newY][cx] == WALL or boardCopy[newY][cx + 1] == WALL:
            continue

        if boardCopy[newY][cx] == BOXES[0]:
            affectedBoxes.append((newY, cx))
            boxesToInvestigate.append((newY, cx))
            continue

        if boardCopy[newY][cx] == BOXES[1]:
            affectedBoxes.append((newY, cx - 1))
            boxesToInvestigate.append((newY, cx - 1))

        if boardCopy[newY][cx + 1] == BOXES[0]:
            affectedBoxes.append((newY, cx + 1))
            boxesToInvestigate.append((newY, cx + 1))

    for box in affectedBoxes:
        cy, cx = box
        newY = cy + dy
        if (
            boardCopy[newY][cx] not in BOXES_AND_EMTPY
            or boardCopy[newY][cx + 1] not in BOXES_AND_EMTPY
        ):
            retval = False
            break

    if retval:
        affectedBoxes.sort(reverse=dy > 0)

        for box in affectedBoxes:
            cy, cx = box
            boardCopy[cy][cx] = EMPTY
            boardCopy[cy][cx + 1] = EMPTY
            newY = cy + dy
            boardCopy[newY][cx] = BOXES[0]
            boardCopy[newY][cx + 1] = BOXES[1]

    return retval


def translateMove(move):
    MOVESET = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    MOVES = list("<>^v")
    return MOVESET[MOVES.index(move)]


filename = "..\\data\\d15_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

CURSOR = "@"
BOX = "O"
WALL = "#"
EMPTY = "."
BOXES = list("[]")

startCoord = None
board = []
moves = []
input = init(lines)

part1()
part2()
