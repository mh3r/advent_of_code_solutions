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
    mapRules = []

    seedLine, *blocks = lines.split("\n\n")
    seeds = seedLine.split(":")[1].split()

    for block in blocks:
        tmpArray = []
        _, *rules = block.split("\n")
        for rule in rules:
            tmpArray.append(list(map(int, rule.split())))
        mapRules.append(tmpArray)

    seeds = list(map(lambda x: int(x), seeds))
    return seeds, mapRules


def part1():
    locations = []
    for seed in seeds:
        locations.append(locationValue(seed))
    answer = min(locations)
    assert answer in [389056265, 35], f"answer is wrong {answer}"
    print("answer", answer)

# kind of cheated here 
# it comes from the realisation that the destination for each of 
# the mapping or the lower range of input seed will always make up 
# the smallest of destination 
# we collect the destinations from each of the map 
# we travel upwards to get seed number and check if thats within the valid range 
# then we proceed as usual 
def part2():
    locations = []
    for mapIndex, mapRule in enumerate(mapRules):
        for mapping in mapRule:
            potentialSeed = seedValue(mapping[0], mapIndex)

            isQualified = False
            for j in range(0, len(seeds), 2):
                if (
                    potentialSeed >= seeds[j]
                    and potentialSeed < seeds[j] + seeds[j + 1]
                ):
                    isQualified = True
                    break

            if isQualified:
                locations.append(locationValue(potentialSeed))

    answer = min(locations)
    assert answer in [137516820, 46], f"answer is wrong {answer}"

    print("answer", answer)
    pass


def locationValue(value):
    for i in range(len(mapRules)):
        mapRule = mapRules[i]

        for mapping in mapRule:
            dest, source, theRange = mapping
            if value >= source and value < source + theRange:
                value = value - source + dest
                break

    return value


def seedValue(value, index):
    for i in range(index, -1, -1):
        mapRule = mapRules[i]

        for mapping in mapRule:
            dest, source, theRange = mapping
            if value >= dest and value < dest + theRange:
                value = value - dest + source
                break

    return value


filename = "..\\data\\d5_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").read()
# lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

seeds, mapRules = init(lines)

part1()
part2()
