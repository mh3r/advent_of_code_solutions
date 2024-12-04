# from parse import *
from functools import reduce
from collections import defaultdict
import sys
import re
import json
import os
import types
import math

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

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            character = grid[y][x]
            if character == "X":
                answer += checkXmas(y, x)
            

#   2401 ???
 
    print("answer part 1", answer)
    assert answer in [18, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print("answer part 2", answer)
    assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def checkXmas(y, x):
    retval = 0
    # print ("---------------" ,y , x)
    for dx, dy in util.ADJ_DIRS_2:

        if y + len(MAS) * dy not in range(len(grid)) or x + len(MAS) * dx not in range(
            len(grid[0])
        ):
            continue

        tmpY = y
        tmpX = x
        for letter in MAS:
            tmpY += dy
            tmpX += dx
            if grid[tmpY][tmpX] != letter:
                break
            
            if letter == MAS[-1]:
                # print ("THE LAST COORD", tmpY, tmpX)
                retval += 1
    return retval                


filename = "..\\data\\d4_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

input = init(lines)

grid = []
for line in lines:
    grid.append(list(line))

MAS = list("MAS")

# print(grid)

part1()
part2()
