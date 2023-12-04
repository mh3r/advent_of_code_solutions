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
        splitted = line.split("|")

        retval.append([splitted[0].strip().split(" "), splitted[1].strip().split(" ")])
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1(input):
    total = 0
    for game in input:
        power = -1
        for number in game[1]:
            if number != "" and number in game[0]:
                power += 1
        if power > -1:
            total += math.pow(2, power)
        print(game)
    print("answer", total)
    pass


def part2(input):
    pointsByGame = {}
    counter = 1
    for game in input:
        power = 0
        for number in game[1]:
            if number != "" and number in game[0]:
                power += 1
        pointsByGame[str(counter)] = power
        counter += 1

    print(pointsByGame)
    total = 0

    tallies = {}
    for i in range(1, len(pointsByGame) + 1):
        tallies[str(i)] = 1

    for key in pointsByGame:
        for i in range(int(key) + 1, int(key) + pointsByGame[key] + 1):
            tallies[str(i)] += tallies[key]

    print(tallies)
    for key in tallies:
        total += tallies[key]
    print("answer", total)
    pass


filename = "..\\data\\d4_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)

part1(input)
part2(input)
