# from parse import *
from functools import reduce
import util
import re
import json
import os


def switchToTest():
    global filename
    global preambleNumber
    global part2Target
    filename = "..\\data\\test.txt"
    preambleNumber = 5
    part2Target = 127


def isValidSummation(target, contenders):
    retval = False
    for i in range(len(contenders) - 1):
        if i + 1 > len(contenders):
            break
        if target == 127:
            print()

        for j in range(i + 1, len(contenders)):
            if contenders[i] + contenders[j] == target:
                retval = True
                break
        else:
            continue
        break

    return retval


def part1():
    for i in range(preambleNumber, len(lines)):
        current = lines[i]
        if isValidSummation(current, preamble):
            preamble.append(current)
            preamble.pop(0)
        else:
            print(current)
            break

    pass


def part2():
    potentialCandidates = []
    for i in range(len(lines)):
        potentialCandidates = [lines[i]]
        for j in range(i + 1, len(lines)):
            if j >= len(lines):
                break
            potentialCandidates.append(lines[j])
            total = sum(potentialCandidates)
            if total == part2Target:
                print(potentialCandidates)
                potentialCandidates.sort()
                print(
                    potentialCandidates[0]
                    + potentialCandidates[len(potentialCandidates) - 1]
                )
                return potentialCandidates
            elif total < part2Target:
                continue
            else:
                break


filename = "..\\data\\d9_input.txt"
part2Target = 177777905
preambleNumber = 25

switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: int(x), lines))

preamble = lines[:preambleNumber]

part1()
part2()
