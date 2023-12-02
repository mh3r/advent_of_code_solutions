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
    games = {}
    for line in lines:
        split_1 = line.split(":")
        contents = [0, 0, 0]
        games[(split_1[0][5:])] = contents
        for game in split_1[1].split(";"):
            for item in game.split(","):
                number = int(item.strip().split(" ")[0])
                if "red" in item:
                    if contents[0] < number:
                        contents[0] = number
                if "green" in item:
                    if contents[1] < number:
                        contents[1] = number
                if "blue" in item:
                    if contents[2] < number:
                        contents[2] = number
    print(games)
    return games


def part1(games, restriction):
    total = 0
    for game in games:
        if (
            games[game][0] <= restriction[0]
            and games[game][1] <= restriction[1]
            and games[game][2] <= restriction[2]
        ):
            total += int(game)

    print(total)


def part2(games):
    total = 0
    for game in games:
        total += int(games[game][0]) * int(games[game][1]) * int(games[game][2])

    print(total)
    pass


filename = "..\\data\\d2_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

games = init(lines)
restriction = [12, 13, 14]

part1(games, restriction)
part2(games)
