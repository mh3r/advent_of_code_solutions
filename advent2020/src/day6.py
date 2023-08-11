from parse import *
from functools import reduce
import util
import re
import json


def decode(rowInput, upperChar):
    tryout = ""
    for char in rowInput:
        tryout += "1" if upperChar == char else "0"
    return int(tryout, 2)


def part1():
    print(idList[0])


def part2():
    for id in idList:
        if id + 1 not in idList and id + 2 in idList:
            print(id + 1)
            return


filename = "D:\\aoc\\advent2020\\data\\d5_input.txt"
# filename = "D:\\aoc\\advent2020\\data\\test.txt"

# Using readlines()
input = open(filename, "r").readlines()

idList = []
for row in input:
    idList.append(decode(row[:7], "B") * 8 + decode(row[7:10], "R"))
idList.sort(reverse=True)

part1()
# part2()
