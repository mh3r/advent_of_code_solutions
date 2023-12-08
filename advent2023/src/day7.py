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


def init(lines):
    global categories, powers

    for power in powers:
        categories[power] = []

    retval = {}
    for line in lines:
        card, value = line.split(" ")
        retval[card] = int(value)
    retval = lines if len(retval) == 0 else retval

    return retval


# a better way is do do a count for each card in hand, sort them
# and they will always be in this format
# [5,5,5,5,5] five of a kind
# [2,2,3,3,3] full house
# [1,1,3,3,3] three of a kind
def categorise(hand, isPart2=False):
    jokersCount = hand.count(JOKER)

    if jokersCount > 0:
        hand = hand.replace(JOKER, "")
        if len(hand) > 0:
            cardCounter = list(map(lambda x: hand.count(x), hand))
            hand = hand + jokersCount * hand[cardCounter.index(max(cardCounter))]
        else:
            hand = jokersCount * JOKER

    cardList = [*hand]
    cardSet = set(cardList)
    a, b, c, d, e = cardList

    # print(cardSet)
    if hand.count(a) == 5:
        return 0

    if hand.count(a) == 4 or hand.count(b) == 4:
        return 1

    # full house logic ...
    if len(cardSet) == 2:
        return 2

    if len(cardSet) == 3:
        # three of a kind
        for char in cardSet:
            if hand.count(char) == 3:
                return 3

        # two pairs
        pairCounter = 0
        for char in cardSet:
            if hand.count(char) == 2:
                pairCounter += 1
        if pairCounter == 2:
            return 4

    if len(cardSet) == 4:
        return 5

    if len(cardSet) == 5:
        return 6


def sortingUtil(input, isPart2=False):
    total = 0
    power = 5
    # "23456789TJQKA" and find index to get the value maybe a better solution 
    for card in input:
        value = 0
        match card:
            case "A":
                value = 14
            case "K":
                value = 13
            case "Q":
                value = 12
            case "J":
                value = 11 if not isPart2 else 1
            case "T":
                value = 10
            case other:
                value = int(card)

        power -= 1
        total += value * 100**power
    return total


def part1(input):
    global categories, powers
    total = 0
    counter = 0
    for hand in input:
        category = categorise(hand)
        categories[powers[category]].append(hand)

    util.printJson(categories)

    for power in categories:
        categories[power] = sorted(categories[power], key=sortingUtil)

    powers.reverse()
    for power in powers:
        for hand in categories[power]:
            counter += 1
            total += counter * input[hand]
            # print (counter, input[hand])
            huh = 1

    print("answer", total)
    assert 248217452 == total, "total is wrong " + str(total)
    pass


def part2(input):
    global categories, powers
    total = 0
    counter = 0
    for hand in input:
        category = categorise(hand, True)
        categories[powers[category]].append(hand)

    util.printJson(categories)

    for power in categories:
        categories[power] = sorted(
            categories[power], key=lambda x: sortingUtil(x, True)
        )

    powers.reverse()
    for power in powers:
        for hand in categories[power]:
            counter += 1
            total += counter * input[hand]
            # print (counter, input[hand])
            huh = 1

    print("answer part 2", total)
    assert 245576185 == total, "total is wrong " + str(total)
    pass


filename = "..\\data\\d7_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")
categories = {}
powers = ["five", "four", "fullhouse", "three", "two", "one", "high"]
JOKER = "J"


input = init(lines)
# print(input)


# part1(input)
part2(input)
