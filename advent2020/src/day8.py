from functools import reduce
import util
import re
import json
import os


def runner(input):
    accumulator = 0
    cursor = 0
    visited = []
    while True:
        if cursor in visited:
            print("Part 1:", accumulator)
            accumulator = 0
            break
        if cursor >= len(input):
            print("Part 2:", accumulator)
            break
        visited.append(cursor)
        split = input[cursor].split(" ")
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


def swap(input, index):
    split = input[index].split(" ")
    op = split[0]
    volume = split[1]
    match op:
        case "nop":
            op = "jmp"
        case "jmp":
            op = "nop"
        case _:
            pass
    input[index] = op + " " + volume


def part1():
    runner(lines)


def part2():
    nonaccs = []
    for index, val in enumerate(lines):
        split = val.split(" ")
        op = split[0]
        if op != "acc":
            nonaccs.append(index)

    for nonaccs in nonaccs:
        linesCopy = lines.copy()
        swap(linesCopy, nonaccs)
        total = runner(linesCopy)
        if total != 0:
            break

    # print(nonaccs)
    # print(linesCopy)
    # print(lines)

    pass


filename = "..\\data\\d8_input.txt"
# filename = "..\\data\\test.txt"
abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# part1()
part2()


# print(lines, sep="\n")
