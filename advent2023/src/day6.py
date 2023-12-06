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
        tries.append(len(checkPossibleTimes(time)))

    print("final answer", math.prod(tries))
    pass


def part2(input):
    global distances, times
    times = [40829166]
    distances = [277133813491063]

    # times = [71530]
    # distances = [940200]
    tries = []
    for time in times:
        tries.append(checkPossibleTimes(time, True))

    print("final answer", times[0] + 1 - 2 * tries[0][0])
    pass


def checkPossibleTimes(time, isPart2 = False):
    global distances, times
    retval = []
    distBenchmark = distances[times.index(time)]
    print("benchmark", distBenchmark)

    for i in range(1, time):
        if (i * (time - i)) > distBenchmark:
            print("first one ", i)
            retval.append(i)
            if (isPart2):
                break

    print(retval)
    print("ans", len(retval))
    return retval


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
