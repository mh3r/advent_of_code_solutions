# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

# from fractions import gcd


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    global pattern
    retval = {}

    counter = 0
    for line in lines:
        if counter == 0:
            pattern = lines[0].strip()
        elif line:
            line = line.replace("(", "").replace(")", "").replace(" ", "")
            split1 = line.split("=")
            split2 = split1[1].split(",")
            retval[split1[0]] = [split2[0], split2[1]]
        counter += 1
    return retval


def arrivedAtTarget(direction, current, input):
    index = 0 if direction == "L" else 1
    return input[current][index]


def part1(input):
    global pattern
    total = 0

    current = "AAA"
    while True:
        if current == "ZZZ":
            break

        current = arrivedAtTarget(pattern[total % len(pattern)], current, input)
        total += 1

    print("answer part 1", total)
    assert 15989 == total, "total is wrong " + str(total)
    pass


def part2(input):
    global pattern

    combos = []
    startingPoints = list(filter(lambda x: x[2] == "A", input))
    print("starting points ", startingPoints)
    for current in startingPoints:
        total = 0
        while True:
            if current[2] == "Z":
                break

            current = arrivedAtTarget(pattern[total % len(pattern)], current, input)
            total += 1
        combos.append(total)

    print(combos)
    theGcd = find_gcd(combos)
    print("gcd", theGcd)
    answer = math.lcm(*combos)
    print("answer part 2", answer)

    assert 13830919117339 == answer, "total is wrong " + str(answer)
    pass

# this is not needed ... should learn about gcd and lcm 
def find_gcd(list):
    x = reduce(math.gcd, list)
    return x


def part2_notused(input):
    global pattern
    total = 0

    startingPoints = list(filter(lambda x: x[2] == "A", input))
    print("starting points ", startingPoints)
    endPoints = []
    # current = "AAA"
    while True:
        if len(startingPoints) == len(endPoints):
            break
        endPoints = startingPoints

        for count, value in enumerate(startingPoints):
            endPoints[count] = arrivedAtTarget(
                pattern[total % len(pattern)], value, input
            )
        # print (endPoints)
        endPoints = list(filter(lambda x: x[2] == "Z", startingPoints))

        total += 1

    print("answer part 2", total)
    # assert 15989 == total, "total is wrong " + str(total)
    pass


filename = "..\\data\\d8_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(lines)

print(*lines, sep="\n")
pattern = ""

input = init(lines)
print(input)
# part1(input)
# part2(input)


# startingPoints = list(filter(lambda x: x[2] == "A", input))
# print(input)
# print(startingPoints)
