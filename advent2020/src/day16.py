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


def init(meta, tickets):
    for line in lines:
        line = line.strip()
        if (
            line
            and line.strip() != "your ticket:"
            and line.strip() != "nearby tickets:"
        ):
            if line.count(",") > 0:
                ticketsStr = line.split(",")
                tickets.append(list(map(lambda x: int(x), ticketsStr)))

            else:
                mainSplit = line.split(":")
                name = mainSplit[0]
                firstSplit = mainSplit[1].strip().split("or")
                limits = []
                tmpSplit = firstSplit[0].strip().split("-")
                limits += [int(tmpSplit[0]), int(tmpSplit[1])]
                tmpSplit = firstSplit[1].strip().split("-")
                limits += [int(tmpSplit[0]), int(tmpSplit[1])]
                meta[name] = limits


def isValid(number, meta):
    retval = False
    for key, value in meta.items():
        retval = (number >= value[0] and number <= value[1]) or (
            number >= value[2] and number <= value[3]
        )

        if retval:
            # print(key, number)
            break
    return retval


def part1(meta, tickets):
    init(meta, tickets)
    invalid = []

    for ticket in tickets:
        for number in ticket:
            if not isValid(number, meta):
                invalid.append(number)
                continue

    print("Total:", sum(invalid))

    # print(meta)
    # print(tickets)
    pass


def part2():
    pass


filename = "..\\data\\d16_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")
print()

meta = {}
tickets = []


part1(meta, tickets)
part2()
