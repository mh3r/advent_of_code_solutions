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
    counter = 1
    for line in lines:
        if "seeds" in line:
            seeds = line.split(":")[1].strip().split(" ")
            counter += 1
            continue
        if "map:" in line:
            if mapName is not None:
                mapRules[mapName] = tmpArray
                tmpArray = []

            mapName = line.split(" ")[0]
            counter += 1
            continue
        if line.strip():
            splitted = line.split(" ")
            tmpArray.append([int(splitted[0]), int(splitted[1]), int(splitted[2])])
        if counter == len(lines):
            mapRules[mapName] = tmpArray
        counter += 1
    seeds = list(map(lambda x: int(x), seeds))


def part1():
    global seeds, mapRules

    source = "seed"
    dests = []
    for index in seeds:
        destination = nextDestination(source)
        while destination is not None:
            if destination == "fertilizer-to-water":
                i = 4
            index = findNewLocation(index, mapRules[destination])
            destination = nextDestination(destination)
            print(index)
        dests.append(index)

    answer = min(dests)

    assert answer in [389056265, 35], f"answer is wrong {answer}"
    print("answer", answer)

    # newLocation = findNewLocation(81, mapRules["soil-to-fertilizer"])
    # print(newLocation)


def part2():
    global seeds, mapRules
    # was thinking of listing it out ...
    # seeds has 10 pairs
    # the code wouldnt finish
    # gonna try to do a bottom up approach and get the smallest range against the input
    moarSeeds = []

    for i in range(0, len(seeds), 2):
        print(i)
        for j in range(seeds[i], seeds[i] + seeds[i + 1]):
            moarSeeds.append(j)

    print(moarSeeds)
    source = "seed"
    dests = []
    for index in moarSeeds:
        destination = nextDestination(source)
        while destination is not None:
            if destination == "fertilizer-to-water":
                i = 4
            index = findNewLocation(index, mapRules[destination])
            destination = nextDestination(destination)
            # print(index)
        dests.append(index)

    print("answer", min(dests))
    pass


def findNewLocation(index, mapList):
    retval = index
    for mapping in mapList:
        dest, source, theRange = mapping
        if index >= source and index < source + theRange:
            dest, source, theRange = mapping
            return index - source + dest

    return retval


def nextDestination(previousMap):
    global mapRules
    if "-" not in previousMap:
        return "seed-to-soil"
    source = previousMap.split("-")[2]
    for key in mapRules:
        if source + "-" in key:
            return key
    return None


filename = "..\\data\\d5_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

seeds = []
mapRules = {}
init(lines)

# print(seeds)
# util.printJson(mapRules)

# part1()
part2()

# print(mapRules)


# print ("======================")
# for key in mapRules:
#     isAllOk = True
#     # print(key)
#     sortedList = sorted(mapRules[key], key=lambda x: x[1])
#     # print(sortedList)

#     for i in range(len(sortedList) - 1):
#         _, s, r = sortedList[i]
#         _1, s1, r1 = sortedList[i + 1]
#         if s + r != s1:
#             isAllOk = False
#             break

#     if not isAllOk:
#         print(f"{key} is corrupted!!!!")
#         isAllOk = True
