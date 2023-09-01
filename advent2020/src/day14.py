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


class Mask:
    def __init__(self):
        self.mem = {}
        self.total = 0
        self.masks = []
        self.maxIndex = 36

    def updateMasks(self, mask):
        reverseMask = util.reverseString(mask)
        self.masks.clear()
        for index, char in enumerate(reverseMask):
            if char != "X":
                self.masks.append((index, char))

    def calculate(self, memSet):
        for key in memSet:
            binary_str = bin(self.mem[key])[2:]
            binLength = len(binary_str)
            # append zeros
            if self.maxIndex > binLength:
                binary_str = (self.maxIndex - binLength + 1) * "0" + binary_str

            binary_list = list(util.reverseString(binary_str))
            for mask in self.masks:
                binary_list[mask[0]] = mask[1]

            binary_str = util.reverseString("".join(binary_list))
            # print(key, binary_str)
            value = int(binary_str, 2)
            print(key, value)
            self.mem[key] = value

    def addAssignment(self, address, value):
        self.mem[address] = value


def part1(lines):
    mask = Mask()
    memSet = set()

    for line in lines:
        if "mask" in line:
            mask.calculate(memSet)
            memSet.clear()
            mask.updateMasks(line.split("=")[1].strip())
        else:
            splitted = line.split("=")
            address = splitted[0].strip().replace("mem[", "").replace("]", "")
            value = int(splitted[1])
            mask.addAssignment(address, value)
            memSet.add(address)

    mask.calculate(memSet)

    totals = [mask.mem[key] for key in mask.mem]

    print(sum(totals))

    # print(json.dumps(mask.__dict__, indent=2))


def part2():
    pass


filename = "..\\data\\d14_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")


part1(lines)
part2()


# tryit = "11011"
# print(int(tryit, 2))

# bin27 = bin(27)[2:]

# print(bin27)

# print(int(bin(27), 2))
