# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math


flipflops = {}
conjunctions = {}
paths = {}
lowSent = 0
highSent = 0


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        line = line.replace(" ", "")
        left, right = line.split("->")
        if "%" in left:
            left = left[1:]
            flipflops[left] = False

        elif "&" in left:
            left = left[1:]
            conjunctions[left] = []

        paths[left] = right.split(",")

    for key in conjunctions:
        for path in paths:
            if key in paths[path]:
                conjunctions[key].append([path, False])

    retval = lines if len(retval) == 0 else retval
    return retval


def process(input, cycle):
    global lowSent, highSent
    queue = [input]

    while queue:
        sender, key, pulse = queue.pop(0)

        # print(f'{sender}    {"high" if pulse else "low" } => {key}')
        if pulse:
            highSent += 1
        else:
            lowSent += 1

        if key in flipflops:
            if not pulse:
                if not flipflops[key]:
                    pulse = not pulse
                flipflops[key] = not flipflops[key]
            else:
                pulse = None
        elif key in conjunctions:
            if key == "tg" and pulse:
                print(f"{sender}  at {cycle}")

            for connector in conjunctions[key]:
                if connector[0] == sender:
                    connector[1] = pulse
                    break
            newPulse = True
            for connector in conjunctions[key]:
                newPulse = newPulse and connector[1]
            pulse = not newPulse

        if pulse is not None:
            if key in paths:
                for path in paths[key]:
                    queue.append([key, path, pulse])


def marksEndOfCycle():
    for flip in flipflops:
        if flipflops[flip]:
            return False

    for conj in conjunctions:
        for connector in conjunctions[conj]:
            if connector[1]:
                return False
    return True


def part1(input):
    global highSent, lowSent
    answer = 0
    startingPoint = ["button", "broadcaster", False]

    cycles = 10000
    cycleBreak = 0
    for i in range(1, cycles + 1):
        process(startingPoint, i)

        for conj in conjunctions["tg"]:
            if conj[1]:
                print(f"found {conj} at {i}  ")

        if marksEndOfCycle():
            cycleBreak = i
            print("it breaks at ", cycleBreak)
            break

    oneRotationHigh = highSent
    oneRotationLow = lowSent
    answer = oneRotationHigh * oneRotationLow
    if cycleBreak > 0:
        rotations = cycles // cycleBreak
        rest = cycles % cycleBreak

        highSent = 0
        lowSent = 0

        for i in range(rest):
            process(startingPoint)

        answer = (
            rotations
            * (oneRotationHigh + highSent)
            * rotations
            * (oneRotationLow + lowSent)
        )
    print("answer part 1", answer)
    assert answer in [0, 819397964], "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0

    # tf  at 3923
    # db  at 3929
    # vq  at 4007
    # ln  at 4091
    # tf  at 7846
    # db  at 7858
    # vq  at 8014
    # ln  at 8182

    answer = math.lcm(3923, 3929, 4007, 4091)

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d20_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)


part1(input)
part2(input)
