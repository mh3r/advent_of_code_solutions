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

    for hand in retval:
        keyList = [*hand]
        keySet = set(keyList)
        a, b, c, d, e = keyList

        print(keySet)
        if hand.count(a) == 5:
            categories[powers[0]].append(hand)
            continue

        if hand.count(a) == 4 or hand.count(b) == 4:
            categories[powers[1]].append(hand)
            continue

        # full house logic ...
        if len(keySet) == 2:
            categories[powers[2]].append(hand)
            continue

        if len(keySet) == 3:
            # three of a kind
            for char in keySet:
                if hand.count(char) == 3:
                    categories[powers[3]].append(hand)
                    continue
            # two pairs
            pairCounter = 0
            for char in keySet:
                if hand.count(char) == 2:
                    pairCounter += 1
            if pairCounter == 2:
                categories[powers[4]].append(hand)
                continue

        if len(keySet) == 4:
            categories[powers[5]].append(hand)
            continue

        if len(keySet) == 5:
            categories[powers[6]].append(hand)
            continue

    for power in categories:
        categories[power] = sorted(categories[power], key=sortingUtil )

    return retval


def sortingUtil(input):
    total = 0
    power = 5
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
                value = 11
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
    powers.reverse()
    for power in powers:
        for hand in categories[power]:
            counter += 1
            total += counter * input[hand]
            # print (counter, input[hand])
            huh = 1 


    print ("answer", total)
    # is wrong ?? 252779966  248220652 
    pass


def part2(input):
    pass


filename = "..\\data\\d7_input.txt"
# switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

print(*lines, sep="\n")
categories = {}
powers = ["five", "four", "fullhouse", "three", "two", "one", "high"]

input = init(lines)
print(input)
util.printJson(categories)


part1(input)
part2(input)


  

# print ("2975A", sortingUtil("2975A"))
# print ("2T45J", sortingUtil("2T45J"))
# print ("29A84", sortingUtil("29A84"))
