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


def part1():
    pass


def part2():
    pass

# def coordinateToString(  x,   y,   z):
#     return 

filename = "..\\data\\d17_input.txt"
ACTIVE = '#'
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

inputMap = [ ]

y = 0
z=0
for line in lines:
    for i in range (0, len(line.strip())):
        if (line[i] == ACTIVE):
            inputMap.append ("{0}_{1}_{2}".format(i, y, z))
    y += 1    


print(inputMap)

part1()
part2()
