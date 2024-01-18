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
    global seeds
    global mapRules
    tmpArray = []
    mapName = None
    for counter, line in enumerate(lines):
        if "seeds" in line:
            seeds = line.split(":")[1].strip().split(" ")
            continue
        if "map:" in line:
            if tmpArray:
                tmpArray.sort()
                mapRules.append(tmpArray)
                tmpArray = []
            continue
        if line.strip():
            splitted = line.split(" ")
            tmpArray.append([int(splitted[0]), int(splitted[1]), int(splitted[2])])
        if counter == len(lines) - 1:
            tmpArray.sort()
            mapRules.append(tmpArray)

    seeds = list(map(lambda x: int(x), seeds))


def part1():
    dests = []
    for seed in seeds:
        dests.append(locationValue(seed, 0))
    answer = min(dests)
    assert answer in [389056265, 35], f"answer is wrong {answer}"
    print("answer", answer)


def part2():
    global seeds, mapRules

    answer = seedsCollection()

    # 882027676 is too high
    # 224525111
    assert answer in [137516820, 46], f"answer is wrong {answer}"

    
    print("answer", answer)
    pass


def locationValue(value, index):
    for i in range(index, len(mapRules)):
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


def seedsCollection():
    locations = []

    for i, mapRule in enumerate(mapRules):
        for mapping in mapRule:
            potentialSeed = seedValue(mapping[0], i)

            isQualified = False
            for j in range(0, len(seeds), 2):
                if (
                    potentialSeed >= seeds[j]
                    and potentialSeed < seeds[j] + seeds[j + 1]
                ):
                    isQualified = True
                    break

            if isQualified:
                locations.append(locationValue(potentialSeed, 0))

    answer = min(locations)

    return answer


filename = "..\\data\\d5_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

seeds = []
mapRules = []
init(lines)

# print(seeds)
# util.printJson(mapRules)

# part1()
part2()

# seedsCollection()
