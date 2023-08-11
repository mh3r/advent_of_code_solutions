from parse import *
from functools import reduce


TREE = "#"


def parser(line):
    line = line.rstrip()
    return list(line)


def part1(inputP1):
    count = 0
    index = 0
    inputP1.pop(0)
    width = len(inputP1[0].rstrip())
    print(inputP1[0].rstrip())
    i = 1
    print(" width ", width)
    for line in inputP1:
        i += 1
        index += 3
        if index >= width:
            index = index % width

        if line[index] == TREE:
            print(
                i,
                index,
            )
            count += 1

    print(" -----> ", count)


def part2(inputP2, xOffset, yOffset):
    count = 0
    x = 0
    inputP2.pop(0)
    width = len(inputP2[0].rstrip())
    print(inputP2[0].rstrip())
    y = 0
    print(" width ", width)
    for line in inputP2:
        y += 1

        if y % yOffset != 0:
            continue

        x += xOffset

        if x >= width:
            x = x % width

        if line[x] == TREE:
            # print(
            #     i,
            #     index,
            # )
            count += 1

    # print(" -----> ", count)
    return count


filename = "D:\\aoc\\advent2020\\data\\d3_input.txt"
# filename = "D:\\aoc\\advent2020\\data\\test.txt"


# Using readlines()
file1 = open(filename, "r")
Lines = file1.readlines()
input = Lines


# part1(input.copy())

numbers = []
numbers.append(part2(input.copy(), 1, 1))
numbers.append(part2(input.copy(), 3, 1))
numbers.append(part2(input.copy(), 5, 1))
numbers.append(part2(input.copy(), 7, 1))
numbers.append(part2(input.copy(), 1, 2))

print(numbers)
# [58, 209, 58, 64, 58]

total = reduce(lambda a, b: a * b, numbers)
print(total)
