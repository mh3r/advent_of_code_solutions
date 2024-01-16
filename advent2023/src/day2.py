# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

COLOURS = "red green blue".split()


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    games = {}
    for line in lines:
        gameId, gamePlay = line.split(":")
        gameId = gameId[5:]
        contents = [0, 0, 0]
        games[gameId] = contents
        for game in gamePlay.split(";"):
            for item in game.split(","):
                number, colour = item.split()
                number = int(number)
                index = COLOURS.index(colour)
                contents[index] = max(contents[index], number)

    return games


def part1(games):
    restriction = [12, 13, 14]
    total = 0
    for game in games:
        if (
            games[game][0] <= restriction[0]
            and games[game][1] <= restriction[1]
            and games[game][2] <= restriction[2]
        ):
            total += int(game)

    assert total == 2632, f"answer is wrong {total}"
    print(total)


def part2(games):
    total = 0
    for game in games:
        total += int(games[game][0]) * int(games[game][1]) * int(games[game][2])

    assert total == 69629, f"answer is wrong {total}"
    print(total)
    pass


filename = "..\\data\\d2_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

games = init(lines)

part1(games)
part2(games)
