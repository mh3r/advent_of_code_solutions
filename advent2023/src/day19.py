# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math


xmas = ["x", "m", "a", "s"]

specialKeys = {"A": [], "R": []}


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    rules = {}
    instructions = []

    isRuleSection = True
    for line in lines:
        if line == "":
            isRuleSection = False
            continue

        if isRuleSection:
            line = line.replace("}", "")
            key, conditions = line.split("{")
            rules[key] = conditions.split(",")
        else:
            line = line[1:-1]

            collections = []
            for char in xmas:
                collections.append(int(re.search(char + "=(\d*)", line).group(1)))
            instructions.append(collections)

    retval = lines if len(retval) == 0 else retval
    return rules, instructions


def passTrough(instruction, conditions, index):
    x, m, a, s = instruction
    condition = conditions[index]

    if ":" in condition:
        left, right = condition.split(":")
        if eval(left):
            passTrough(instruction, [right], 0)
        else:
            passTrough(instruction, conditions, index + 1)
    elif condition in specialKeys:
        specialKeys[condition].append(instruction)
    else:
        passTrough(instruction, rules[condition], 0)


def part1():
    answer = 0
    for instruction in instructions:
        passTrough(instruction, rules["in"], 0)

    print(specialKeys)
    for values in specialKeys["A"]:
        answer += sum(values)

    print("answer part 1", answer)

    assert answer in [0, 19114, 432788], "total is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d19_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

rules, instructions = init(lines)

print(rules)
print(instructions)


part1()
part2()
