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
        if "map:" in line or counter == len(lines):
            if mapName is not None:
                mapRules[mapName] = tmpArray
                tmpArray = []

            mapName = line.split(" ")[0]
            counter += 1
            continue
        if line.strip():
            splitted = line.split(" ")
            tmpArray.append([int(splitted[0]), int(splitted[1]), int(splitted[2])])
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

    print("answer", min(dests))

    # newLocation = findNewLocation(81, mapRules["soil-to-fertilizer"])
    # print(newLocation)


def part2():
    global seeds, mapRules
    # was thinking of listing it out ... 
    # seeds has 10 pairs 
    # the code wouldnt finish 
    # gonna try to do a bottom up approach and get the smallest range against the input 
    moarSeeds = []
    for i in range (seeds[0], seeds [0]  + seeds[1]):
        moarSeeds.append(i)
    for i in range (seeds[2], seeds [2]  + seeds[3]):
        moarSeeds.append(i)
    print (moarSeeds)
    source = "seed"
    dests = []
    for index in seeds:
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


def findNewLocation(index, locationList):
    retval = index
    locationFound = None
    for location in locationList:
        start, end, theRange = location
        if index >= end and index < end + theRange:
            locationFound = location
            break
    if locationFound is not None:
        start, end, theRange = locationFound
        retval = index - end + start

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
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

seeds = []
mapRules = {}
init(lines)

# print(seeds)
# util.printJson(mapRules)

part1()
#part2()

print (len(seeds))