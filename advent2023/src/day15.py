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


def init(lines):
    retval = []
    for line in lines:
        retval = line.split(",")
    retval = lines if len(retval) == 0 else retval
    return retval


def hashItUp(word):
    total = 0
    for char in word:
        total += ord(char)
        total *= 17
        total = total % 256
    return total


def part1(input):
    answer = 0

    """ Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256."""
    values = []
    for word in input:
        values.append(hashItUp(word))
    print(values)
    answer = sum(values)
    print("answer part 1", answer)
    assert answer in [1320, 507291], "total is wrong " + str(total)
    pass


def cachedHash(label, address):
    if label not in address:
        address[label] = hashItUp(label)
    return address[label]


def part2(input):
    answer = 0
    boxes = {}
    address = {}

    for word in input:
        if "=" in word:
            label, value = word.split("=")
            boxNumber = str(cachedHash(label, address))

            if boxNumber not in boxes:
                boxes[boxNumber] = []
            lenses = boxes[boxNumber]
            found = None
            for i, lense in enumerate(lenses):
                if label + " " in lense:
                    found = i
                    break
            if found is None:
                lenses.append(word.replace("=", " "))
            else:
                lenses[found] = word.replace("=", " ")
        else:
            label = word[:-1]
            boxNumber = str(cachedHash(label, address))
            if boxNumber in boxes:
                lenses = boxes[boxNumber]
                found = None
                for lense in lenses:
                    if label + " " in lense:
                        found = lense
                        break
                if found:
                    lenses.remove(found)

            pass

    util.printJson(boxes)

    for key in boxes:
        # rn: 1 (box 0) * 1 (first slot) * 1 (focal length) = 1
        for i, value in enumerate(boxes[key]):
            answer += (int(key) + 1) * (i + 1) * int(value.split(" ")[1])

    print("answer part 2", answer)
    assert answer in [145, 296921], "total is wrong " + str(answer)
    pass


filename = "..\\data\\d15_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")


input = init(lines)

print(input)

# part1(input)
part2(input)
 
