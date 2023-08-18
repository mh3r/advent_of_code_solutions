# from parse import *
from functools import reduce
import util
import re
import json
import os


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def part1():
    pass


def part2():
    pass


filename = "..\\data\\d6_input.txt"
switchToTest()
abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()

part1()
part2()
