# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

TOP = "TOP"
BOTTOM = "BOTTOM"
RIGHT = "RIGHT"
LEFT = "LEFT"

GOING_TOP = {"|": (-2, 0, TOP), "7": (-1, -1, LEFT), "F": (-1, 1, RIGHT)}
GOING_BOTTOM = {"|": (2, 0, BOTTOM), "J": (1, -1, LEFT), "L": (1, 1, RIGHT)}
GOING_RIGHT = {"-": (0, 2, RIGHT), "7": (1, 1, BOTTOM), "J": (-1, 1, TOP)}
GOING_LEFT = {"-": (0, -2, LEFT), "L": (-1, -1, TOP), "F": (1, -1, BOTTOM)}

COMPASS = {
    TOP: GOING_TOP,
    BOTTOM: GOING_BOTTOM,
    LEFT: GOING_LEFT,
    RIGHT: GOING_RIGHT,
}


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    sCoord = None
    for count, line in enumerate(lines):
        retval.append([*line])
        if "S" in line:
            sCoord = (count, line.index("S"))
        pass
    retval = lines if len(retval) == 0 else retval
    return (retval, sCoord)


def deduceFirstMove(sCoord, theMap):
    y, x = sCoord
    moves = [
        (0, 1, RIGHT, "-J7"),
        (0, -1, LEFT, "-FL"),
        (1, 0, BOTTOM, "|JL"),
        (-1, 0, TOP, "|7F"),
    ]

    possibleCoordinates = []
    for move in moves:
        dy, dx, direction, charset = move
        if theMap[y + dy][x + dx] in charset:
            possibleCoordinates.append((y + dy, x + dx, direction))

    directions = [possibleCoordinates[0][2], possibleCoordinates[1][2]]
    StartReplacements = {
        "TOPLEFT": "J",
        "TOPRIGHT": "L",
        "TOPBOTTOM": "|",
        "RIGHTLEFT": "-",
        "RIGHTBOTTOM": "F",
        "BOTTOMLEFT": "7",
    }

    startHiddenCharacter = ""
    for key, value in StartReplacements.items():
        if all(direction in key for direction in directions):
            startHiddenCharacter = value
            break

    print(f"Replacing start character with: '{startHiddenCharacter}'")
    theMap[y][x] = startHiddenCharacter
    return possibleCoordinates[0]


def traversePipe(sCoord, theMap):
    path = []
    current = sCoord
    y1, x1, direction = deduceFirstMove(sCoord, theMap)
    next = (y1, x1)
    while current != sCoord or len(path) == 0:
        path.append((current))
        dy, dx, direction = COMPASS[direction][theMap[next[0]][next[1]]]
        next2 = (current[0] + dy, current[1] + dx)
        current = next
        next = next2
    return path


def part1(sCoord, theMap):
    path = traversePipe(sCoord, theMap)

    answer = int(len(path) / 2)
    print("answer part 1:", answer)
    assert answer in [6649, 8, 0], "total is wrong " + str(answer)
    pass


def part2(sCoord, theMap):
    path = traversePipe(sCoord, theMap)
    
    for y in range(len(theMap)):
        for x, character in enumerate(theMap[y]):
            print(y, x, character)
            break

            pass

    answer = 0
    print("answer part 2:", answer)
    assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d10_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# symbols = ["|", "-", "L", "J", "7", "F", "."]
# newSymbols = ["┃", "━", "┗", "┛", "┓", "┏", "x"]

# newInput = []
# for line in lines:
#     for count, symbol in enumerate(symbols):
#         line = line.replace(symbols[count], newSymbols[count])
#     newInput.append(line)


# print(*newInput, sep="\n")

input, sCoord = init(lines)

# part1(sCoord, input)
part2(sCoord, input)
