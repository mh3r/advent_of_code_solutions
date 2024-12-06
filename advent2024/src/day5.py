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
        if "|" in line:
            pages.append(line)
        if "," in line:
            books.append(line.split(","))
    retval = lines if len(retval) == 0 else retval
    return retval


def part1():
    answer = 0
    for book in books:

        bookCorrect = isBookCorrect(book)
        if bookCorrect == 0:
            incorrectBooks.append(book)
        answer += isBookCorrect(book)

        # break
    print("answer part 1:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def part2():
    answer = 0

    print(incorrectBooks)

    for book in incorrectBooks:
        answer += correctBook(book)

    print("answer part 2:", answer)
    # assert answer in [0, 0], "answer is wrong " + str(answer)
    pass


def isBookCorrect(book):

    relatedPages = []

    for page in book:
        relatedPages.extend(list(filter(lambda x: page in x, pages)))

    # print(relatedPages)

    for i in range(len(book) - 1):
        currentPage = book[i]
        for j in range(i, len(book)):
            nextPage = book[j]
            if nextPage + "|" + currentPage in relatedPages:
                return 0

        relatedPages = list(filter(lambda x: currentPage not in x, relatedPages))

    print(book)

    return int(book[int((len(book) - 1) / 2)])


def correctBook(book):
    correctBookOrder = []
    relatedPages = []

    for page in book:
        relatedPages.extend(list(filter(lambda x: page in x, pages)))

    # 97,75,47,61,53
    for page in book:

        correctBookOrder.append(page)

        tmpRelatedPages = list(filter(lambda x: page + "|" in x, relatedPages))
        laterPages = []
        for tmpRelatedPage in tmpRelatedPages:
            laterPages.append(tmpRelatedPage.split("|")[1])

        currentPageIndex = correctBookOrder.index(page)
        for laterPage in laterPages:

            if (
                laterPage in correctBookOrder
                and correctBookOrder.index(laterPage) < currentPageIndex
            ):
                correctBookOrder.remove(page)
                correctBookOrder.insert(correctBookOrder.index(laterPage), page)
                currentPageIndex = correctBookOrder.index(page)

    print(correctBookOrder)

    return int(correctBookOrder[int((len(correctBookOrder) - 1) / 2)])


filename = "..\\data\\d5_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

pages = []
books = []
incorrectBooks = []

input = init(lines)

part1()
part2()
