# from parse import *
from functools import reduce
from collections import defaultdict
import sys
import re
import json
import os
import types
import math
import numpy as np


sys.path.append(os.getcwd() + "\py-util")
import util


def switchToTest():
    global filename
    print("Testing ... ")
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    tmpMachine = []
    for line in lines:
        if line:
            line = (
                line.replace("Button A: X+", "")
                .replace("Button B: X+", "")
                .replace("Y+", "")
                .replace("Prize: X=", "")
                .replace("Y=", "")
            )
            splitted = line.split(",")
            tmpMachine.append(int(splitted[0]))
            tmpMachine.append(int(splitted[1]))
        else:
            retval.append(tmpMachine)
            tmpMachine = []

    retval.append(tmpMachine)
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0

    for machine in input:
        answer += calculatePresses(machine)

    print("answer part 1:", answer)
    assert answer in [480, 38839], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    for machine in input:
        answer += calculatePresses2(machine)
    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def calculatePresses(machine):
    a, b, c, d, e, f = machine
    print(machine)

    x = (d * e - c * f) / (d * a - c * b)
    y = (e - a * x) / c

    if x in range(1, 101) and y in range(1, 101):
        print(x, y)
        return int(3 * x + y)

    return 0


def calculatePresses2(machine):
    a, b, c, d, e, f = machine
    e += 10000000000000
    f += 10000000000000
    print(machine)

    x = (d * e - c * f) / (d * a - c * b)
    y = (e - a * x) / c

    if x > 0 and y > 0 and x.is_integer() and y.is_integer():
        print(x, y)
        return int(3 * x + y)

    return 0


def calculateMin(machine):
    print(machine)
    ax, ay, bx, by, px, py = machine
    maxRange = 100
    manualA = 0
    manualB = 0
    dx = ax - ay
    dy = bx - by
    dp = px - py
    try:
        for b in range(maxRange, 0, -1):
            for a in range(1, maxRange + 1):
                if a * ax + b * bx == px and a * ay + b * by == py:
                    print(a, b, a * dx + b * dy)
                    manualA = a
                    manualB = b
                    raise StopIteration
    except StopIteration:
        pass

    A = np.matrix([[ax, bx], [ay, by]])
    B = np.matrix([[px], [py]])

    A_inverse = np.linalg.inv(A)
    X = A_inverse * B

    print(X)

    a = acceptIfIntegerish(X[0, 0])  # The first value (80)
    b = acceptIfIntegerish(X[1, 0])  # The second value (40)
    if a > 100 or b > 100 or a < 1 or b < 1:
        a = 0
        b = 0

    if manualA != a or manualB != b:
        print("whats going on here ")

    print(a, b)

    return a * 3 + b


def acceptIfIntegerish(input):
    retval = 0

    roundedInput = round(input)

    if input < roundedInput + 0.002 and input > roundedInput - 0.002:
        retval = roundedInput

    return retval


def calculateMin2(machine):
    ax, ay, bx, by, px, py = machine
    px += 10000000000000
    py += 10000000000000

    """ 
    a 94 + b 22 = 8400
    a 34 + b 67 = 5400 

    """

    A = np.matrix([[ax, bx], [ay, by]])
    B = np.matrix([[px], [py]])

    A_inverse = np.linalg.inv(A)
    X = A_inverse * B

    print(X)
    a = round(X[0, 0])  # The first value (80)
    b = round(X[1, 0])  # The second value (40)

    print(a, b)

    return a * 3 + b


filename = "..\\data\\d13_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

''' 
need clean up ... 

had segway into numpy matrices ... bad move 
'''


part1()
part2()
