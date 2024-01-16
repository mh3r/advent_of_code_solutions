# from parse import *
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
    retval = []
    for line in lines:
        line = line.split(":")[1].strip()
        winners, owned = line.split("|")
        retval.append([winners.split(), owned.split()])
    retval = lines if len(retval) == 0 else retval
    return retval


def part1(input):
    total = 0
    for game in input:
        winners, owned = game
        thePowa = len([number for number in owned if number in winners])
        if thePowa:
            total += math.pow(2, thePowa - 1)
        # print(game)

    total = int(total)
    assert total == 21568, f"total is wrong {total}"
    print("answer", total)
    pass


def part2(input):
    total = 0
    pointsByGame = {}
    tallies = {}
    for counter, game in enumerate(input):
        winners, owned = game
        power = len([number for number in owned if number in winners])
        daCounter = str(counter + 1)
        pointsByGame[daCounter] = power
        tallies[daCounter] = 1

    print("pointsByGame", pointsByGame)

    for key in pointsByGame:
        for i in range(int(key) + 1, int(key) + pointsByGame[key] + 1):
            tallies[str(i)] += tallies[key]
        total += tallies[key]

    assert total == 11827296, f"total is wrong {total}"
    print("answer", total)


filename = "..\\data\\d4_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

part1(input)
part2(input)
