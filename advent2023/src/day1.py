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


def part1(lines):
    counts = []
    for line in lines:
        print(line)
        numbers = re.findall(r"\d", line)
        counts.append(int(numbers[0] + numbers[-1]))

    print(counts)
    ans = sum(counts)
    print("total ", ans)


def part2(lines):
    counts = []
    # better solution is ...
    # line = line.replace("one", "o1e")
    # line = line.replace("eight", "e8t")
    
    for line in lines:
        line = line.replace("oneight", "18")
        line = line.replace("twone", "21")
        line = line.replace("threeight", "38")
        line = line.replace("fiveight", "58")
        line = line.replace("sevenine", "79")
        line = line.replace("eighthree", "83")
        line = line.replace("eightwo", "82")
        line = line.replace("nineight", "98")

        line = line.replace("one", "1")
        line = line.replace("two", "2")
        line = line.replace("three", "3")
        line = line.replace("four", "4")
        line = line.replace("five", "5")
        line = line.replace("six", "6")
        line = line.replace("seven", "7")
        line = line.replace("eight", "8")
        line = line.replace("nine", "9")

        numbers = re.findall(r"\d", line)
        counts.append(int(numbers[0] + numbers[-1]))

    print(counts)
    print("total ", sum(counts))


filename = "..\\data\\d1_input.txt"#
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")

# part1(lines)
part2(lines)
