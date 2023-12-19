# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

"/\|-"
RIGHT = [0, 1]
LEFT = [0, -1]
TOP = [-1, 0]
DOWN = [1, 0]

DOT = "."
MIRROR_F = "/"
MIRROR_B = "\\"
SPLITTER_VERT = "|"
SPLITTER_HORZ = "-"


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    leftMirrors = []
    rightMirrors = []
    vertSplitter = []
    horzSplitter = []
    land = []
    for y, line in enumerate(lines):
        for x, char in enumerate([*line]):
            if char == MIRROR_F:
                leftMirrors.append([y, x])
            if char == MIRROR_B:
                rightMirrors.append([y, x])
            if char == SPLITTER_VERT:
                vertSplitter.append([y, x])
            if char == SPLITTER_HORZ:
                horzSplitter.append([y, x])

        land.append([*line])

    return land, leftMirrors, rightMirrors, vertSplitter, horzSplitter

    # lots of improvements to be made ... 
def lightThrough(startingCoord):
    # this should hve just included the direction from so its just one array
    fromLeft = []
    fromRight = []
    fromTop = []
    fromBottom = []
    energized = []

    queue = [startingCoord]

    while len(queue) > 0:
        y, x, y1, x1 = queue.pop()

        direction = "top"
        if [y1, x1] == RIGHT:
            direction = "right"
        if [y1, x1] == LEFT:
            direction = "left"
        if [y1, x1] == DOWN:
            direction = "down"
        message = f"{y} {x} going {direction}"

        # if message == "8 7 going top":
        #     asjlfas = 0
        # print(message)

        # for yyy in range(len(land)):
        #     line = ""
        #     for xxx in range(len(land[0])):
        #         if [yyy, xxx] in energized:
        #             line += "#"
        #         else:
        #             line += "."
        #     print(line)

        if [y, x] not in energized:
            energized.append([y, x])
        newY = y + y1
        newX = x + x1
        while newY >= 0 and newY < len(land) and newX >= 0 and newX < len(land[0]):
            nextObstacle = land[newY][newX]

            # could have checked the original direction 
            # eg. right [0, 1] going through / [-1, 0]
            # similarly left  [0, -1] going through / [1, 0] ie. y, x ----> -y, x 

            # we could also cache the light arrays since they are constant 
            if [
                y1,
                x1,
            ] == RIGHT and nextObstacle in SPLITTER_VERT + MIRROR_B + MIRROR_F:
                if [newY, newX] not in fromLeft:
                    fromLeft.append([newY, newX])
                else:
                    break
                if nextObstacle == SPLITTER_VERT:
                    # print("GO UP AND DOWN FROM ", newY, newX)
                    queue.append([newY, newX, -1, 0])
                    queue.append([newY, newX, 1, 0])
                    break
                if nextObstacle == MIRROR_F:
                    # print("GO UP FROM ", newY, newX)
                    queue.append([newY, newX, -1, 0])
                    break
                if nextObstacle == MIRROR_B:
                    # print("GO DOWN FROM ", newY, newX)
                    queue.append([newY, newX, 1, 0])
                    break
            if [y1, x1] == LEFT and nextObstacle in SPLITTER_VERT + MIRROR_B + MIRROR_F:
                if [newY, newX] not in fromRight:
                    fromRight.append([newY, newX])
                else:
                    break
                if nextObstacle == SPLITTER_VERT:
                    # print("GO UP AND DOWN FROM ", newY, newX)
                    queue.append([newY, newX, -1, 0])
                    queue.append([newY, newX, 1, 0])
                    break
                if nextObstacle == MIRROR_F:
                    # print("GO DOWN FROM ", newY, newX)
                    queue.append([newY, newX, 1, 0])
                    break
                if nextObstacle == MIRROR_B:
                    # print("GO UP FROM ", newY, newX)
                    queue.append([newY, newX, -1, 0])
                    break
            if [y1, x1] == DOWN and nextObstacle in SPLITTER_HORZ + MIRROR_B + MIRROR_F:
                if [newY, newX] not in fromTop:
                    fromTop.append([newY, newX])
                else:
                    break
                if nextObstacle == SPLITTER_HORZ:
                    # print("GO LEFT AND RIGHT FROM ", newY, newX)
                    queue.append([newY, newX, 0, 1])
                    queue.append([newY, newX, 0, -1])
                    break
                if nextObstacle == MIRROR_F:
                    # print("GO LEFT FROM ", newY, newX)
                    queue.append([newY, newX, 0, -1])
                    break
                if nextObstacle == MIRROR_B:
                    # print("GO RIGHT FROM ", newY, newX)
                    queue.append([newY, newX, 0, 1])
                    break
            if [y1, x1] == TOP and nextObstacle in SPLITTER_HORZ + MIRROR_B + MIRROR_F:
                if [newY, newX] not in fromBottom:
                    fromBottom.append([newY, newX])
                else:
                    break
                if nextObstacle == SPLITTER_HORZ:
                    # print("GO LEFT AND RIGHT FROM ", newY, newX)
                    queue.append([newY, newX, 0, 1])
                    queue.append([newY, newX, 0, -1])
                    break
                if nextObstacle == MIRROR_F:
                    # print("GO  RIGHT FROM ", newY, newX)

                    queue.append([newY, newX, 0, 1])
                    break
                if nextObstacle == MIRROR_B:
                    # print("GO LEFT FROM ", newY, newX)

                    queue.append([newY, newX, 0, -1])
                    break

            if [newY, newX] not in energized:
                energized.append([newY, newX])
            newY += y1
            newX += x1

    return len(energized)


def part1():
    answer = 0

    # if using example ... do
    answer = lightThrough([0, 0, 0, 1])
    # answer = lightThrough([0, 0, 1, 0])
    print("answer part 1", answer)
    assert answer in [0, 7517, 46], "total is wrong " + str(answer)
    pass


def part2():
    answer = 0
    values = []
    for y in range(len(land)):
        for x in range(len(land[0])):
            if y == 0:
                # most top
                print(y, x)
                values.append(lightThrough([y, x, 1, 0]))

            if y == len(land) - 1:
                values.append(lightThrough([y, x, -1, 0]))
                print(y, x)

            if x == 0:
                # left
                values.append(lightThrough([y, x, 0, 1]))

                print(y, x)

            if x == len(land[0]) - 1:
                values.append(lightThrough([y, x, 0, -1]))

                # most right
                print(y, x)

    answer = max(values)
    print("answer part 2", answer)
    assert answer in [0, 51, 7741], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d16_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

land, leftMirrors, rightMirrors, vertSplitter, horzSplitter = init(lines)


# part1()
part2()
