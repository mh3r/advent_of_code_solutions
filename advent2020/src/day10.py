# from parse import *
from functools import reduce
import util
import re
import json
import os


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def part1(lines):
    diff_1 = []
    diff_3 = []

    length = len(lines)
    previous = 0
    for index, jolt in enumerate(lines):
        # if index == length - 1:
        #     diff_3.append(jolt)
        #     break
        if index != 0:
            previous = lines[index - 1]
        if jolt - previous == 1:
            diff_1.append(jolt)
        elif jolt - previous == 3:
            diff_3.append(jolt)
    print("\n\n")
    print(len(diff_1))
    print(len(diff_3) + 1)

    pass


def aggregateCounter(index, lines, agg, head):
    head = head.copy()
    head.append(lines[index])
    length = len(lines)
    if index == length - 1:
        agg.append(head)
        return

    jolt = lines[index]
    for inc in range(1, 4):
        tmp = jolt + inc
        if tmp in lines:
            aggregateCounter(list.index(lines, tmp), lines, agg, head)


def part2_1(lines):
    agg = []
    print(lines)
    aggregateCounter(0, lines, agg, [])
    # print(*agg[:30], sep="\n")
    print(len(agg))
    return len(agg)


def part2(lines):
    multList = []
    lines.insert(0, 0)
    lines.append(max(lines))
    index = 0
    while index < len(lines):
        i = 0
        tmpList = [lines[index]]
        while True:
            current = lines[index]
            index += 1

            if index + 1 >= len(lines):
                break

            next = lines[index]
            tmpList.append(next)
            if next - current == 3:
                index = list.index(lines, next)
                break

        if len(tmpList) > 2:
            index = list.index(lines, tmpList[-1])
            multList.append(part2_1(tmpList))

    print(multList)
    print(reduce(lambda x, y: x * y, multList))


filename = "..\\data\\d10_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: int(x.strip()), lines))
lines.sort()

# print (*lines, sep= "\n")

# part1(lines)
part2(lines)
