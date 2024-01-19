# from parse import *
from functools import reduce, cmp_to_key
import util
import re
import json
import os
import types
import math
from collections import defaultdict


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


def init(lines):
    retval = []
    for line in lines:
        hand, value = line.split()
        retval.append((hand, int(value)))
    return retval


def compare(itemA, itemB):
    handA, handB = itemA[0], itemB[0]
    for i in range(len(handA)):
        intrinsicValueA = cardValues.index(handA[i])
        intrinsicValueB = cardValues.index(handB[i])
        diff = intrinsicValueA - intrinsicValueB
        if diff != 0:
            return diff / abs(diff)
    return 0


def classify(hand, isJokerise):
    hand = jokerise(hand) if isJokerise else hand

    counters = []
    for x in hand:
        counters.append(str(hand.count(x)))
    counters.sort()

    return "".join(counters)


def jokerise(hand):
    retval = hand
    jokerCount = hand.count(JOKER)
    if jokerCount > 0 and jokerCount != 5:
        shortHand = hand.replace(JOKER, "")
        cardCounter = list(map(lambda x: shortHand.count(x), shortHand))
        retval = shortHand + jokerCount * shortHand[cardCounter.index(max(cardCounter))]

    return retval


def calculateValue(isJokerise=False):
    categorisedDeck = defaultdict(list)
    categorisations = "11111 11122 12222 11333 22333 14444 55555".split()

    total = 0
    counter = 1
    for line in input:
        key = classify(line[0], isJokerise)
        categorisedDeck[key].append(line)

    for key in categorisations:
        categorisedDeck[key] = sorted(categorisedDeck[key], key=cmp_to_key(compare))
        for line in categorisedDeck[key]:
            total += counter * line[1]
            counter += 1

    return total


def part1():
    total = calculateValue()
    print("answer", total)
    assert total in [248217452, 0, 6440], "total is wrong " + str(total)


def part2():
    global cardValues
    cardValues = "J23456789TQKA"
    total = calculateValue(True)

    print("answer part 2", total)
    assert total in [245576185, 0, 5905], "total is wrong " + str(total)


filename = "..\\data\\d7_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

input = init(lines)

JOKER = "J"
cardValues = "23456789TJQKA"

part1()
part2()
