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
    global end

    filename = "..\\data\\test.txt"
    end = 2020


def part1(input):
    last = None
    memoryMap = {}
    for i in range(start, end):
        if len(input) > 0:
            last = input.pop(0)
            memoryMap[last] = [i]
            last = int(last)
        else:
            current = str(last)
            if current in memoryMap and len(memoryMap[current]) > 1:
                value = memoryMap[current][-1] - memoryMap[current][-2]
                memoryMap[current].pop(0)
                strValue = str(value)
                if strValue in memoryMap:
                    memoryMap[strValue].append(i)
                else :
                    memoryMap[strValue] = [i]

                last = value
            else:
                last = 0
                current = str(last)
                if current in memoryMap:
                    memoryMap[current].append(i)
                else:
                    memoryMap["0"] = [i]
        # print(i, last)

    # print(memoryMap)
    print(last)


def part2(input):
    global end
    end = 30000000 + 1
    part1(input)
    pass


filename = "..\\data\\d15_input.txt"
start = 1
end = 2020
switchToTest()

end += 1

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")


part1(lines[0].split(","))
part2(lines[0].split(","))
