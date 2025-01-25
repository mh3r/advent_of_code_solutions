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
    answer = runner()
    print("answer part 1:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


filename = "..\\data\\d17_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

A, B, C = list("abc")
PROGRAM = "program"
OUTPUT = "output"
COUNTER = "counter"

REGISTERS = {
    A: int(lines[0].split(":")[1]),
    B: int(lines[1].split(":")[1]),
    C: int(lines[2].split(":")[1]),
    PROGRAM: list(map(int, lines[4].split(":")[1].strip().split(","))),
    OUTPUT: [],
    COUNTER: 0,
}


def translateOperand(operand):
    retval = None
    match operand:
        case 0 | 1 | 2 | 3:
            retval = operand
        case 4:
            retval = REGISTERS[A]
        case 5:
            retval = REGISTERS[B]
        case 6:
            retval = REGISTERS[C]

    return retval


def adv(operand):
    operandValue = translateOperand(operand)
    REGISTERS[A] = int(REGISTERS[A] / pow(2, operandValue))


def bxl(operand):
    REGISTERS[B] = xor(REGISTERS[B], operand)


def bst(operand):
    operandValue = translateOperand(operand)
    REGISTERS[B] = operandValue % 8


def jnz(operand):
    if REGISTERS[A] != 0:
        REGISTERS[COUNTER] = operand


def bxc(operand):
    REGISTERS[B] = xor(REGISTERS[B], REGISTERS[C])


def out(operand):
    operandValue = translateOperand(operand) % 8
    REGISTERS[OUTPUT].append(operandValue)


def bdv(operand):
    operandValue = translateOperand(operand)
    REGISTERS[B] = int(REGISTERS[A] / pow(2, operandValue))


def cdv(operand):
    operandValue = translateOperand(operand)
    REGISTERS[C] = int(REGISTERS[A] / pow(2, operandValue))


"""
The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register.
 (The numerator is still read from the A register.)
"""


def runner():
    while len(REGISTERS[PROGRAM]) - 1 > REGISTERS[COUNTER]:
        tmpCounter = REGISTERS[COUNTER]

        operand = REGISTERS[PROGRAM][tmpCounter + 1]

        instructions[tmpCounter](operand)

        # do the thing

        if tmpCounter == REGISTERS[COUNTER]:
            REGISTERS[COUNTER] += 2
    return ",".join(REGISTERS[OUTPUT])


def xor(a, b):
    return (a and not b) or (not a and b)


instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


part1()
part2()


