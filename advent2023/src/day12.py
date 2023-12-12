# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

BROKEN = "#"
QUESTION = "?"
WORKING = "."


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def patternMatchesCode(input, code):
    retval = []

    code = list(map(lambda x: int(x), code.split(","))) if "," in code else code

    input = input.replace(WORKING, " ")
    brokens = list(filter(lambda x: x.strip(), input.split(" ")))
    # print(brokens)
    for broken in brokens:
        retval.append(len(broken))

    return 1 if retval == code else 0


def populatePossiblePatterns(input):
    retval = []

    pool = []
    if QUESTION in input:
        pool = [input]
    else:
        retval = [input]

    while pool:
        current = pool.pop()
        brokenIndex = current.index(QUESTION)

        word1 = current[:brokenIndex] + BROKEN + current[brokenIndex + 1 :]
        word2 = current[:brokenIndex] + WORKING + current[brokenIndex + 1 :]

        if QUESTION in word1:
            pool.append(word1)
            pool.append(word2)
        else:
            retval.append(word1)
            retval.append(word2)

    return retval


def populatePossiblePatternsAgain(pattern, code):
    code = list(map(lambda x: int(x), code.split(",")))

    retval = []

    combos = []
    # chunk them up based on the size
    for i, value in enumerate(code):
        preceedingList = code[:i]
        postList = code[i + 1 :]

        onlyPossiblePattern = pattern[
            sum(preceedingList)
            + len(preceedingList) : len(pattern)
            - sum(postList)
            - len(postList)
        ]
        actualList = list(
            filter(
                lambda x: x.count(BROKEN) == value,
                populatePossiblePatterns(onlyPossiblePattern),
            )
        )
        combos.append(actualList)

    print(combos)

    head = []
    tmp = []
    while combos:
        next = combos.pop(0)
        if not head:
            head = next
            continue
        for headValue in head:
            for nextValue in next:
                tmp.append(headValue + nextValue)
        head = tmp
        tmp = []

    retval = head

    return retval


def singleDotPlease(input):
    while True:
        if 2 * WORKING in input:
            input = input.replace(2 * WORKING, WORKING)
        else:
            break

        if input and input[0] == WORKING:
            input = input[1:]

        if input and input[-1] == WORKING:
            input = input[:-1]

    return input


def expandLine(line):
    retval = ""
    pattern, code = line.split(" ")
    patterns = ""
    codes = ""

    for i in range(5):
        patterns += pattern + QUESTION
        codes += code + ","

    retval = patterns[:-1] + " " + codes[:-1]
    return retval


def part1(input):
    answer = 0
    partAnswer = []

    for line in input:
        score = 0
        pattern, code = line.split(" ")
        for newPattern in populatePossiblePatterns(pattern):
            score += patternMatchesCode(newPattern, code)

        partAnswer.append(score)

    print(partAnswer)
    answer = sum(partAnswer)
    print("answer part 1", answer)
    assert 7195 == answer, "total is wrong " + str(answer)
    pass


def part2(input):
    answer = 0
    partAnswer = []

    for line in input:
        score = 0
        line = expandLine(line)
        pattern, code = line.split(" ")
        pattern = singleDotPlease(pattern)
        # print(pattern, code)

        for newPattern in populatePossiblePatterns(pattern):
            score += patternMatchesCode(newPattern, code)

        partAnswer.append(score)

    print(partAnswer)
    answer = sum(partAnswer)
    print("answer part 2", answer)
    # assert 0 == answer, "total is wrong " + str(answer)
    pass


filename = "..\\data\\d12_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

# part1(input)
# part2(input)


# print(end)


# print(populatePossiblePatterns("?#?#"))
# score = 0
# actualList = list(filter(lambda x :patternMatchesCode(x, [3]),   populatePossiblePatterns("?#?#")))

# print(actualList)


# #  print patternMatchesCode(x, [value]),
# possibles = populatePossiblePatterns("##.#####.")
# print(possibles)

# print(patternMatchesCode(possibles[0], [5], True))
