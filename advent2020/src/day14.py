# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

X = "X"
ONE = "1"


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


class Mask:
    def __init__(self, isPartOne=True):
        self.mem = {}
        self.mem_part2 = {}
        self.total = 0
        self.masks = []
        # self.ones = []
        self.exes = []
        self.rawMask = 0
        self.maxIndex = 36
        self.isPartOne = isPartOne

    def updateMasks(self, mask):
        reverseMask = util.reverseString(mask)
        mask = mask.replace(X, "0")
        self.rawMask = int(mask, 2)
        self.masks.clear()
        # self.ones.clear()
        self.exes.clear()
        for index, char in enumerate(reverseMask):
            self.masks.append((index, char))
            if char == X:
                self.exes.append(index)
            # if char == ONE:
            #     self.ones.append(index)

    def calculate(self, memSet):
        for key in memSet:
            binary_str = bin(self.mem[key])[2:]
            binLength = len(binary_str)
            # append zeros
            if self.maxIndex > binLength:
                binary_str = (self.maxIndex - binLength + 1) * "0" + binary_str

            binary_list = list(util.reverseString(binary_str))
            for mask in self.masks:
                if mask[1] != "X":
                    binary_list[mask[0]] = mask[1]

            binary_str = util.reverseString("".join(binary_list))
            # print(key, binary_str)
            value = int(binary_str, 2)
            # print(key, value)
            self.mem[key] = value

    def calculate_v2(self, memSet):
        for key in memSet:
            print(self.exes)
            print(key, self.mem[key])
            print(self.rawMask)

            appliedMask = self.rawMask | int(key)
            addresses = self.populateMasks(appliedMask)

            for address in addresses:
                self.mem_part2[str(address)] = self.mem[key]

    def populateMasks(self, appliedMask):
        for x in self.exes:
            if appliedMask & 2**x == 2**x:
                appliedMask = appliedMask - 2**x

        keys = set()
        keys.add(appliedMask)
        for x in self.exes:
            additionalKeys = []
            for key in keys:
                additionalKeys.append(key)
                additionalKeys.append(key | 2**x)

            keys.update(additionalKeys)
        return keys

    def exploitFloating(self, input):
        keys = set()
        inputs = [input]
        while len(inputs) > 0:
            binary = inputs.pop()
            if "X" in binary:
                for index, char in enumerate(binary):
                    if char == "X":
                        inputs.append(binary[:index] + "0" + binary[index + 1 :])
                        inputs.append(binary[:index] + "1" + binary[index + 1 :])
            else:
                keys.add(binary)

        return list(keys)


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
            mask.mem[address] = value
            memSet.add(address)

    mask.calculate(memSet)

    totals = [mask.mem[key] for key in mask.mem]

    print("total:", sum(totals))

    # print(json.dumps(mask.__dict__, indent=2))


def part2(lines):
    mask = Mask()
    memSet = []

    for line in lines:
        if "mask" in line:
            mask.calculate_v2(memSet)
            memSet.clear()
            mask.updateMasks(line.split("=")[1].strip())
        else:
            splitted = line.split("=")
            address = splitted[0].strip().replace("mem[", "").replace("]", "")
            value = int(splitted[1])
            mask.mem[address] = value
            memSet.append(address)

    mask.calculate_v2(memSet)
    totals = [mask.mem_part2[key] for key in mask.mem_part2]
    # print (*mask.mem_part2, sep= "\n")
    print(json.dumps(mask.mem_part2, indent=2))

    print("total:", sum(totals))


filename = "..\\data\\d14_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")


# part1(lines)

# string takes too long .. consider using bit operations
part2(lines)
# 4720233919670 too low
