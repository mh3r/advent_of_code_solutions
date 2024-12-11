# from parse import *
from functools import reduce
from collections import defaultdict
import sys
import re
import json
import os
import types
import math
from functools import cache

sys.path.append(os.getcwd() + "\py-util")
import util


def switchToTest():
    global filename
    print("Testing ... ")
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    stones = input[0].strip()

    stoneList = list(map(int, stones.split(" ")))

    for stone in stoneList:
        answer += blinkRecur(stone, 25)

    # print(stoneList)
    # answer = len(stoneList)
    print("answer part 1:", answer)
    assert answer in [55312, 235850], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    stones = input[0].strip()

    stoneList = list(map(int, stones.split(" ")))
    for stone in stoneList:
        answer += blinkRecur(stone, 75)

    # print(stoneList)
    # answer = len(stoneList)
    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


@cache
def blinkRecur(stone, times):
    if times == 0:
        return 1

    nextTime = times - 1
    if stone == 0:
        return blinkRecur(1, nextTime)

    digits = int(math.log10(stone)) + 1
    if digits % 2 == 0:
        halfIndex = int(digits / 2)
        firstHalf = first_n_digits(stone, halfIndex)
        secondHalf = last_n_digits(stone, halfIndex)
        return blinkRecur(firstHalf, nextTime) + blinkRecur(secondHalf, nextTime)

    return blinkRecur(stone * 2024, nextTime)


def blink(stones):
    retval = []

    for stone in stones:
        stoneStr = str(stone)
        if stoneStr in blinkMap:
            retval.extend(blinkMap[stoneStr])
            continue

        if stone == 0:
            retval.append(1)
            continue

        digits = int(math.log10(stone)) + 1
        if digits % 2 == 0:
            halfIndex = int(digits / 2)
            firstHalf = first_n_digits(stone, halfIndex)
            secondHalf = last_n_digits(stone, halfIndex)
            retval.append(firstHalf)
            retval.append(secondHalf)
            blinkMap[stoneStr] = [firstHalf, secondHalf]
            continue

        value = 2024 * stone
        retval.append(value)
        blinkMap[stoneStr] = [value]

    return retval


def last_n_digits(num, n):
    return int(abs(num) % (10**n))


def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)


filename = "..\\data\\d11_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

blinkMap = {"0": [1]}

input = init(lines)

part1()
part2()
