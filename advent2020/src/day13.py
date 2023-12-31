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
even when changed to 
jumping on biggest element 
and verifying the numbers surrounding it 
"""


def part2(lines):
    busses = lines[1].split(",")
    start = 100000000000000
    end = 200000000000000
    departTime = 0

    start = 1000000
    end = 2000000

    # start = 1000000000
    # end = 2000000000

    busesInt = filter(lambda x: x != "x", busses)
    busesInt = list(map(lambda x: int(x), busesInt))
    maxBus = max(busesInt)

    start = start + maxBus - start % maxBus
    maxBusIndex = list.index(busses, str(maxBus))

    while start < end:
        for busIndex, busValue in enumerate(busses):
            busId = 0
            if busValue == "x":
                continue
            else:
                busId = int(busValue)

            if (start + busIndex - maxBusIndex) % busId != 0:
                break

            if busIndex == len(busses) - 1:
                departTime = start - maxBusIndex

        if departTime > 0:
            break

        start += maxBus

    print(departTime)
    pass


# https://www.youtube.com/watch?v=zIFehsBHB8o&ab_channel=MathswithJay
# https://www.youtube.com/watch?v=MdePzlQtnCc&ab_channel=CalculusbyChristee
# chinese remainder theorem (Sun Tzu)
def part2_crt(lines):
    rawBusses = lines[1].split(",")
    remainderList = []
    modulusList = []

    for index, bus in enumerate(rawBusses):
        if bus != "x":
            number = int(bus)
            modulusList.append(number)
            remainderList.append((number - index) % number)

    modProduct = reduce(lambda x, y: x * y, modulusList)
    miList = [modProduct // n for n in modulusList]
    xiList = [pow(mi, -1, modulusList[index]) for index, mi in enumerate(miList)]
    rimixiList = [
        remainderList[index] * mi * xiList[index] for index, mi in enumerate(miList)
    ]
    print(sum(rimixiList) % modProduct)


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
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")


# part1(lines)
part2_crt(lines)
