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
    networkMap = {}
    pattern, rest = lines.split("\n\n")

    for line in rest.split("\n"):
        line = line.replace("(", "").replace(")", "").replace(" ", "")
        source, destination = line.split("=")
        networkMap[source] = destination.split(",")
    return networkMap, pattern


def arrivedAtTarget(direction, current, input):
    index = 0 if direction == "L" else 1
    return input[current][index]


def part1(networkMap):
    total = 0
    current = "AAA"
    while current != "ZZZ":
        current = arrivedAtTarget(pattern[total % len(pattern)], current, networkMap)
        total += 1

    print("answer part 1", total)
    assert 15989 == total, "total is wrong " + str(total)


def part2(input):
    global pattern

    combos = []
    startingPoints = list(filter(lambda x: x[2] == "A", input))
    print("starting points ", startingPoints)
    for current in startingPoints:
        total = 0
        while current[2] != "Z":
            current = arrivedAtTarget(pattern[total % len(pattern)], current, input)
            total += 1
        combos.append(total)

    print(combos)
    answer = math.lcm(*combos)
    print("answer part 2", answer)
    assert 13830919117339 == answer, "total is wrong " + str(answer)


filename = "..\\data\\d8_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").read()


# print(*lines, sep="\n")


networkMap, pattern = init(lines)
part1(networkMap)
part2(networkMap)
