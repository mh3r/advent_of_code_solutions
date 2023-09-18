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
    def __init__(self, isPartOne=True):
        self.mem = {}
        self.mem_part2 = {}
        self.total = 0
        self.masks = []
        self.maxIndex = 36
        self.isPartOne = isPartOne

    def updateMasks(self, mask):
        reverseMask = util.reverseString(mask)
        self.masks.clear()
        for index, char in enumerate(reverseMask):
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
                if mask[1] != "X":
                    binary_list[mask[0]] = mask[1]

            binary_str = util.reverseString("".join(binary_list))
            # print(key, binary_str)
            value = int(binary_str, 2)
            # print(key, value)
            self.mem[key] = value

    def calculate_v2(self, memSet):
        for key in memSet:
            keys = []
            binary_str = bin(int(key))[2:]
            binLength = len(binary_str)
            # append zeros
            if self.maxIndex > binLength:
                binary_str = (self.maxIndex - binLength + 1) * "0" + binary_str

            binary_list = list(util.reverseString(binary_str))
            for mask in self.masks:
                if mask[1] == "1":
                    binary_list[mask[0]] = "1"
                elif mask[1] == "X":
                    binary_list[mask[0]] = "X"

            binary_str = util.reverseString("".join(binary_list))
            print (binary_str)
            addresses = self.exploitFloating(binary_str)
            print(addresses)

            for address in addresses:
                self.mem_part2[str(int(address, 2))] = self.mem[key]

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

    print(sum(totals))

    # print(json.dumps(mask.__dict__, indent=2))


def part2(lines):
    mask = Mask()
    memSet = set()

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
            memSet.add(address)

    mask.calculate_v2(memSet)
    totals = [mask.mem_part2[key] for key in mask.mem_part2]

    print(sum(totals))


filename = "..\\data\\d14_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")


# part1(lines)

# string takes too long .. consider using bit operations 
part2(lines)
