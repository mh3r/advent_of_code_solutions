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

    numberIndexesCopy = numberIndexes[:]
    dotIndexesCopy = dotIndexes[:]
    shiftIndexes(numberIndexesCopy, dotIndexesCopy)

    for i in numberIndexesCopy:
        answer += i[0] * i[1]

    # print(memory)

    print("answer part 1:", answer)
    # assert answer in [1928, 6607511583593], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0
    numberIndexesCopy = numberIndexes[:]
    shiftIndexesTwo(numberIndexesCopy)

    for i in numberIndexesCopy:
        answer += i[0] * i[1]

    print("answer part 2:", answer)
    # assert answer in [2858, 0], "answer is wrong " + str(answer)
    pass


def populateIndexes(numberIndexes, dotIndexes):

    counter = 0
    indexCounter = 0
    for i in range(len(list(input))):
        char = input[i]
        multiplier = int(char)
        # print(i, multiplier)

        for x in range(multiplier):
            if i % 2 == 0:
                numberIndexes.append([indexCounter, counter])
            else:
                dotIndexes.append(indexCounter)
            indexCounter += 1

        if i % 2 == 0:
            counter += 1


def shiftIndexes(numberIndexes, dotIndexes):

    while True:
        lastNumberIndex = numberIndexes[-1][0]
        lastNumberValue = numberIndexes[-1][1]
        firstDotIndex = dotIndexes[0]

        if firstDotIndex > lastNumberIndex:
            break

        dotIndexes.pop(0)
        numberIndexes.pop()
        numberIndexes.append([firstDotIndex, lastNumberValue])
        numberIndexes.sort()

    pass


def shiftIndexesTwo(numberIndexes):

    fileBlocks = analyzeFileBlock(numberIndexes)

    # 00992111777.44.333....5555.6666.....8888..
    while len(fileBlocks) > 0:

        fileBlock = fileBlocks.pop(0)
        indexGap = findIndexGap(fileBlock[0], fileBlock[2], numberIndexes)
        if indexGap > 0:
            filteredNumberIndexes = list(
                filter(lambda x: x[1] != fileBlock[1], numberIndexes)
            )

            numberIndexes.clear()
            numberIndexes.extend(filteredNumberIndexes)

            for i in range(fileBlock[0]):
                numberIndexes.append([indexGap + i, fileBlock[1]])

            numberIndexes.sort()


def findIndexGap(gap, firstIndex, numberIndexes):
    for i in range(len(numberIndexes) - 1):
        if numberIndexes[i][0] > firstIndex:
            return 0 
        if numberIndexes[i + 1][0] - numberIndexes[i][0] > gap:
            index = numberIndexes[i][0] + 1
            if index > firstIndex:
                return 0
            return index
    return 0


def analyzeFileBlock(numberIndexes):
    retval = []
    numberIndexesCopy = numberIndexes[:]

    while len(numberIndexesCopy) > 0:
        biggestNumber = numberIndexesCopy[-1][1]
        listOfBigNumber = list(
            filter(lambda x: x[1] == biggestNumber, numberIndexesCopy)
        )
        listOfBigNumber.sort()
        firstIndex = listOfBigNumber[0][0]
        counter = len(listOfBigNumber)
        numberIndexesCopy = list(
            filter(lambda x: x[1] != biggestNumber, numberIndexesCopy)
        )
        retval.append([counter, biggestNumber, firstIndex])

    return retval


def convertToMemory(input):
    retval = ""

    counter = 0
    for i in range(len(list(input))):
        char = input[i]
        multiplier = int(char)
        # print(i, multiplier)

        value = DOT
        if i % 2 == 0:
            value = str(counter)
            counter += 1
        retval += multiplier * value

    return retval


def moveMemories(memory):
    retval = memory
    while True:
        compactedMemory = retval.replace(".", "")
        strippedMemory = retval.replace(".", " ").strip()

        if len(compactedMemory) == len(strippedMemory):
            break

        lastDigit = findLastDigitIndex(retval)
        firstDot = retval.index(DOT)

        retvalList = list(retval)

        retvalList[firstDot] = retvalList[lastDigit]
        retvalList[lastDigit] = DOT

        retval = "".join(retvalList)

    return retval


def findLastDigitIndex(string):
    reversed = util.reverseString(string)
    reversedIndex = 0
    for i in range(len(list(reversed))):
        if reversed[i] != DOT:
            reversedIndex = i
            break

    return len(string) - 1 - reversedIndex


def calculateScore(string):
    retval = 0
    for i in range(len(list(string))):
        char = string[i]
        if char == DOT:
            break
        retval += i * int(char)
    return retval


filename = "..\\data\\d9_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

input = init(lines)

input = input[0]


numberIndexes = []
dotIndexes = []

populateIndexes(numberIndexes, dotIndexes)


# part1()
part2()
