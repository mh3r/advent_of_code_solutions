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
        if line:
            if line.count(",") > 0:
                ticketsStr = line.split(",")
                tickets.append(list(map(lambda x: int(x), ticketsStr)))

            else:
                mainSplit = line.split(":")
                name = mainSplit[0]
                
                pass

    pass


def part1():
    pass


def part2():
    pass


filename = "..\\data\\d16_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

meta = {}
tickets = []


part1()
part2()
