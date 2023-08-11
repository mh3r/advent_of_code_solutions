from parse import *


def parser(line):
    line = line.rstrip()
    retval = parse("{:d}-{:d} {}: {}", line)
    return list(retval)


def part1():
    count = 0
    for passie in input:
        occurrence = passie[3].count(passie[2])
        if occurrence >= passie[0] and occurrence <= passie[1]:
            count += 1
    print(count)


def part2():
    count = 0
    for passie in input:
        counter = 0
        if passie[2] == passie[3][passie[0] - 1]:
            counter += 1
        if passie[2] == passie[3][passie[1] - 1]:
            counter += 1
        if counter == 1:
            count += 1
    print(count)


filename = "D:\\aoc\\advent2020\\data\\d2_input.txt"
# filename = "D:\\aoc\\advent2020\\data\\test.txt"


# Using readlines()
file1 = open(filename, "r")
Lines = file1.readlines()
input = list(map(parser, Lines))

# print(input)


# part1()
part2()
