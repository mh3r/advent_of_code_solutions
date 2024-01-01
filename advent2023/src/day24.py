# from parse import *
from functools import reduce
from collections import defaultdict
from numpy import *
import util
import re
import json
import os
import types
import math
import matplotlib.pyplot as plt


def switchToTest():
    global filename, boundaries
    filename = "..\\data\\test.txt"
    boundaries = [7, 27]


def init(lines):
    retval = []
    for line in lines:
        splitted = line.split("@")
        x, y, z = list(map(lambda x: int(x), splitted[0].split(",")))
        px, py, pz = list(map(lambda x: int(x), splitted[1].split(",")))
        retval.append([x, y, z, px, py, pz])
    retval = lines if len(retval) == 0 else retval
    return retval


# taken from https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
def perp(a):
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1, a2, b1, b2):
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = dot(dap, db)
    num = dot(dap, dp)
    return (num / denom.astype(float)) * db + b1


def part1(input):
    answer = 0

    for i in range(len(input) - 1):
        for j in range(i + 1, len(input)):
            x1, y1, z1, px1, py1, pz1 = input[i]
            x2, y2, z2, px2, py2, pz2 = input[j]
            p1 = array([x1, y1])
            p2 = array([x1 + px1, y1 + py1])

            p3 = array([x2, y2])
            p4 = array([x2 + px2, y2 + py2])

            interX, interY = seg_intersect(p1, p2, p3, p4)

            if (
                interX > boundaries[0]
                and interY > boundaries[0]
                and interX < boundaries[1]
                and interY < boundaries[1]
                and ((interX > x1 and px1 > 0) or (interX < x1 and px1 < 0))
                and ((interX > x2 and px2 > 0) or (interX < x2 and px2 < 0))
                and ((interY > y1 and py1 > 0) or (interY < y1 and py1 < 0))
                and ((interY > y2 and py2 > 0) or (interY < y2 and py2 < 0))
            ):
                answer += 1

    print("answer part 1", answer)
    assert answer in [0, 2, 19976], "total is wrong " + str(answer)
    pass


def tester(input, sequences):
    
    for sequence in sequences:
        t, i = sequence
        

    


    return True


def part2(input):
    answer = 0

    length = len(input)
    tracker = {}
    for i in range(1, length + 3):
        tracker[i] = []
        for ufo in input:
            x, y, z, px, py, pz = ufo
            tracker[i].append(x + i * px)
    print(tracker)

    timeVsHailIndex = [[1, 4], [3, 1], [4, 2], [5, 0], [6, 3]]

    print("answer part 2", answer)
    assert answer in [0], "total is wrong " + str(answer)
    pass


boundaries = [200000000000000, 400000000000000]
filename = "..\\data\\d24_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))


input = init(lines)

# part1(input)
part2(input)


# #Example data
# x = [19,17]
# y = [13,14]
# x = np.array(x)
# y = np.array(y)

# #Fit line
# slope, intercept = np.polyfit(x, y, 1)

# #Plot
# plt.figure()
# plt.scatter(x, y)
# plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color = 'k')
# plt.show()

# print(slope)
