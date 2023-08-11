filename = "D:\\aoc\\advent2020\\data\\d1_input.txt"
# filename = "D:\\aoc\\advent2020\\data\\test.txt"

# Using readlines()
file1 = open(filename, "r")
Lines = file1.readlines()
input = list(map(int, Lines))


def part1():
    expectedAddition = 2020

    start = 0
    end = len(input) - 1
    print(end)

    second = start + 1

    resultList = []

    while True:
        if start == end:
            break
        
        if input[start] + input[second] == expectedAddition:
            resultList = [input[start], input[second]]
            break
        else:
            second += 1

        if second > end:
            start += 1
            second = start + 2

    print(
        "{} * {} = {}".format(
            resultList[0], resultList[1], resultList[0] * resultList[1]
        )
    )


def part2():
    expectedAddition = 2020

    start = 0
    end = len(input) - 1
    print(end)

    second = start + 1
    third = start + 2

    resultList = []

    while True:
        if start == end:
            break
        if input[start] + input[second] + input[third] == expectedAddition:
            resultList = [input[start], input[second], input[third]]
            break
        else:
            third += 1

        if third > end:
            second += 1
            third = second + 1

        if second + 2 > end:
            start += 1
            second = start + 1
            third = start + 2

    print(
        "{} * {} * {} = {}".format(
            resultList[0],
            resultList[1],
            resultList[2],
            resultList[0] * resultList[1] * resultList[2],
        )
    )


# part1()
part2()
