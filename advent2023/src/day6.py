# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math


def switchToTest():
    global filename, times, distances
    filename = "..\\data\\test.txt"
    times = [7, 15, 30]
    distances = [9, 40, 200]


def init(lines):
    retval = []
    for line in lines:
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1(input):
    global times
    tries = []
    for time in times:
        # its a bell curve thing
        tries.append(time + 1 - 2 * deduceFirstOccurence(time))
    total = math.prod(tries)
    print("final answer", total)
    assert total == 505494, "total is wrong " + str(total)
    pass


def part2(input):
    global distances, times

    times = [int("".join(list(map(str, times))))]
    distances = [int("".join(list(map(str, distances))))]

    time = times[0]
    total = time + 1 - 2 * deduceFirstOccurence(time)
    print("final answer", total)
    assert total == 23632299, "total is wrong " + str(total)
    pass


def deduceFirstOccurence(time):
    global distances, times
    distBenchmark = distances[times.index(time)]
    print("benchmark", distBenchmark)

    for i in range(1, time):
        if (i * (time - i)) > distBenchmark:
            return i


filename = "..\\data\\d6_input.txt"
times = [40, 82, 91, 66]
distances = [277, 1338, 1349, 1063]

# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)


# part1(input)
part2(input)


# test = [40, 82, 91, 66]


# print (test)
