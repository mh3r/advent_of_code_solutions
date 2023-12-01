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


def part1():
    pass


def part2():
    pass


def init(lines):
    global rules
    global phrases

    hasPhraseStarted = False
    for line in lines:
        if line == "":
            hasPhraseStarted = True
            continue
        line = line.replace('"', "")
        if hasPhraseStarted:
            phrases.append(line)
        else:
            splitted1 = line.split(":")
            key = splitted1[0]
            ruleList = []
            for sequence in splitted1[1].split("|"):
                ruleList.append(sequence.strip().split(" "))
            rules[key] = ruleList


def analysePossibleLengths(key):
    global rulesLengths
    lengths = set()
    if key in rulesLengths:
        return rulesLengths[key]

    if key not in rules:
        rulesLengths[key] = [1]

    for sequence in rules[key]:
        
        set.add()


    

    return lengths


filename = "..\\data\\d19_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

rules = {}
phrases = []
rulesLengths = {}

init(lines)

print(rules)


# print(analysePossibleLengths)

part1()
part2()
