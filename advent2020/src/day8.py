from functools import reduce
import util
import re
import json
import os


def runner():
    accumulator = 0
    cursor = 0
    visited = []
    while True:
        if cursor in visited:
            print("Part 1:", accumulator)
            accumulator = 0
            break
        if cursor >= len(lines):
            break
        visited.append(cursor)
        split = lines[cursor].split(" ")
        op = split[0]
        volume = int(split[1])
        match op:
            case "acc":
                cursor += 1
                accumulator += volume
            case "jmp":
                cursor += volume
            case _:
                cursor += 1
    return accumulator


def part1():
    runner()


def part2():
    nonacc = []
    for index, val in enumerate(lines):
        split = val.split(" ")
        op = split[0]
        if op != "acc":
            nonacc.append(index)

    print(nonacc)

    pass


filename = "..\\data\\d8_input.txt"
filename = "..\\data\\test.txt"
abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

part1()
part2()


# print(lines, sep="\n")
