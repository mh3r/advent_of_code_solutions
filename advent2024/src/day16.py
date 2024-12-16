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
    global start
    global end
    retval = []
    for y in range(len(lines)):
        line = lines[y]
        board.append(list(line))
        if "S" in line:
            start = (y, line.index("S"))

        if "E" in line:
            end = (y, line.index("E"))

        pass
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0

    answer = aStarAttempt()






    print("answer part 1:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass



def aStarAttempt():
    openQueue = [start]



    aStarRoadMap = {}
    aStarRoadMap[start] = 0
    aStarRoadMap[start] = 10
    aStarRoadMap[end] = 3
    
    

    aStarRoadMap = dict(sorted(aStarRoadMap.items(), key=lambda item: item[1])) 

    return 0
    pass


def part2():
    answer = 0

    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


filename = "..\\data\\d16_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

board = []
start = None
end = None
input = init(lines)

part1()
part2()



'''
cbf for now - but a-star is the way here i think ... just need to add direction into the key 

'''