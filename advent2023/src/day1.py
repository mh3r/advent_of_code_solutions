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
    answer = 0
    for line in lines:
        # can also use list comphrehension
        # numbers = [c for c in line if c.isdigit()]
        # same result when using regex
        numbers = re.findall(r"\d", line)
        answer += int(numbers[0] + numbers[-1])

    assert answer == 54990, f"answer is wrong {answer}"
    print("total ", answer)


def part2(lines):
    answer = 0

    for line in lines:
        line = (
            line.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )
        numbers = re.findall(r"\d", line)
        answer += int(numbers[0] + numbers[-1])

    assert answer == 54473, f"answer is wrong {answer}"
    print("total ", answer)


filename = "..\\data\\d1_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

part1(lines)
part2(lines)
