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


def part1(lines):
    start, busses = processInput(lines)
    end = start + busses[-1]
    print(busses)

    departTime = 0
    targetBus = 0
    isFound = False
    for i in range(start, end):
        for bus in busses:
            if i % bus == 0:
                departTime = i
                targetBus = bus
                isFound = True
                break

        if isFound:
            break

    print((departTime - start) * targetBus)
    pass

""" 
this is taking too long 
instead of jumping on first element 
jump on biggest element 
but then you have to verify the numbers by the differences in the indexes instead of starting from 0 
""" 
def part2(lines):
    busses = lines[1].split(",")
    start = 100000000000000
    end = 200000000000000
    departTime = 0
    
    firstModulusFound = False
    firstBusId = int(busses[0])
    while start < end:
        for busIndex, busValue in enumerate(busses):
            busId = 0
            if busValue == "x":
                continue
            else:
                busId = int(busValue)

            if (start + busIndex) % busId != 0:
                break

            if busIndex == len(busses) - 1:
                departTime = start

        if departTime > 0:
            break

        if not firstModulusFound:
            firstModulusFound = start % firstBusId == 0

        if not firstModulusFound:   
            start += 1
        else:
            start += firstBusId

    print(departTime)
    pass


def processInput(lines):
    start = int(lines[0])
    busses = []
    splitted = lines[1].split(",")
    for split in splitted:
        if split != "x":
            busses.append(int(split))

    busses.sort()

    return (start, busses)


filename = "..\\data\\d13_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")


# part1(lines)
part2(lines)
