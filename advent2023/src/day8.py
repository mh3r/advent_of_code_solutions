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
    steps, rest = lines.split("\n\n")

    for line in rest.split("\n"):
        line = line.replace("(", "").replace(")", "").replace(" ", "")
        source, destination = line.split("=")
        networkMap[source] = destination.split(",")
    return networkMap, steps


def arrivedAtTarget(direction, current, input):
    index = 0 if direction == "L" else 1
    return input[current][index]


def part1(networkMap, steps):
    total = 0
    current = "AAA"
    while current != "ZZZ":
        current = arrivedAtTarget(steps[total % len(steps)], current, networkMap)
        total += 1

    print("answer part 1", total)
    assert 15989 == total, "total is wrong " + str(total)


def part2(input, steps):
    combos = []
    startingPoints = list(filter(lambda x: x.endswith("A"), input))
    print("starting points ", startingPoints)
    for current in startingPoints:
        total = 0
        while not current.endswith("Z"):
            current = arrivedAtTarget(steps[total % len(steps)], current, input)
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


networkMap, steps = init(lines)
part1(networkMap, steps)
part2(networkMap, steps)
