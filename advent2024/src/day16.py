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
    global start
    global end
    retval = []
    for y in range(len(lines)):
        line = lines[y]
        board.append(list(line))
        if "S" in line:
            start = (y, line.index("S"), EAST)

        if "E" in line:
            end = (y, line.index("E"))

        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0

    answer = aStarAttempt()

    print("answer part 1:", answer)
    assert answer in [7036, 11048, 72400], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    answer = aStarAttempt(True)

    print("answer part 2:", answer)
    assert answer in [45, 64, 435], "answer is wrong " + str(answer)
    pass


def aStarAttempt(isPart2=False):
    aStarRoadMap = {}
    traversed = {}
    aStarRoadMap[start] = (0, [start])
    traversed[start] = (0, [start])
    # board1 = copy.deepcopy(board)
    finalScore = None

    while len(aStarRoadMap) > 0:

        aStarRoadMap = dict(sorted(aStarRoadMap.items(), key=lambda item: item[1]))
        traversed = dict(sorted(traversed.items(), key=lambda item: item[1]))
        key = next(iter(aStarRoadMap))
        cy, cx, d = key
        # board1[cy][cx] = EMPTY
        cScore, paths = aStarRoadMap.pop(key)

        journeys = JOURNEYS[d]

        for i in range(len(journeys)):
            journey = journeys[i]
            newY = cy + journey[0]
            newX = cx + journey[1]

            if board[newY][newX] in [EMPTY, "E"]:
                newD = journey[2]
                nextKey = (newY, newX, newD)
                newScore = cScore + FEES[i] + 1

                if (newY, newX) == end and finalScore is None:
                    if not isPart2:
                        return newScore
                    finalScore = newScore

                if (
                    nextKey not in traversed
                    or traversed[nextKey][0] > newScore
                    or (finalScore is not None and finalScore > newScore)
                ):
                    # board1[newY][newX] = newD
                    aStarRoadMap[nextKey] = (newScore, paths + [nextKey])
                    traversed[nextKey] = (newScore, paths + [nextKey])
                elif traversed[nextKey][0] == newScore or (
                    finalScore is not None and finalScore == newScore
                ):
                    aStarRoadMap[nextKey][1].extend(paths + [nextKey])
                    traversed[nextKey][1].extend(paths + [nextKey])


    if isPart2:
        shortestpaths = findLastCoordinates(traversed, finalScore)

        seats = set()

        for shortestPath in shortestpaths:
            for coord in traversed[shortestPath][1]:
                
                seats.add((coord[0], coord[1]))

        print(seats)
        finalScore = len(seats)

    return finalScore
    pass



def findLastCoordinates(traversed, finalScore):
    retval = []
    keys = list({k: v for (k, v) in traversed.items() if v[0] == finalScore}.keys())

    for key in keys:
        if key[0] == end[0] and key[1] == end[1]:
            retval.append(key)

    return retval



filename = "..\\data\\d16_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")
NORTH, EAST, SOUTH, WEST = list("nesw")
FEES = [0, 1000, 1000]
EMPTY = "."

board = []
start = None
end = None
init(lines)

JOURNEYS = {
    NORTH: [(-1, 0, NORTH), (0, -1, WEST), (0, 1, EAST)],
    EAST: [(0, 1, EAST), (-1, 0, NORTH), (1, 0, SOUTH)],
    SOUTH: [(1, 0, SOUTH), (0, 1, EAST), (0, -1, WEST)],
    WEST: [(0, -1, WEST), (1, 0, SOUTH), (-1, 0, NORTH)],
}

part1()
part2()

'''
TODO 
FEES variable may not be needed 
JOURNEYS variable may be simplified

part 2 took so long - need to figure out a better way - maybe use set instead of list to record paths
or use a completely diff dictionary to keep track unique coords 
'''