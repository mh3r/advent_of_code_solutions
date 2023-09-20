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


def init(meta, tickets):
    for line in lines:
        line = line.strip()
        if (
            line
            and line.strip() != "your ticket:"
            and line.strip() != "nearby tickets:"
        ):
            if line.count(",") > 0:
                ticketsStr = line.split(",")
                tickets.append(list(map(lambda x: int(x), ticketsStr)))

            else:
                mainSplit = line.split(":")
                name = mainSplit[0]
                firstSplit = mainSplit[1].strip().split("or")
                limits = []
                tmpSplit = firstSplit[0].strip().split("-")
                limits += [int(tmpSplit[0]), int(tmpSplit[1])]
                tmpSplit = firstSplit[1].strip().split("-")
                limits += [int(tmpSplit[0]), int(tmpSplit[1])]
                meta[name] = limits


def isValid(number, meta):
    retval = False
    for key, value in meta.items():
        retval = (number >= value[0] and number <= value[1]) or (
            number >= value[2] and number <= value[3]
        )

        if retval:
            # print(key, number)
            break
    return retval


def pinPointFields(metaMapping):
    registered = []
    while not isAllDefined(metaMapping):
        for key, value in metaMapping.items():
            if len(value) == 1 and value[0] not in registered:
                registered.append(value[0])
                for key2, value2 in metaMapping.items():
                    if len(value2) > 1:
                        try:
                            value2.remove(value[0])
                        except ValueError:
                            pass  # do nothing!
    return metaMapping


def isAllDefined(metaMapping):
    filtered = dict(filter(lambda x: len(x[1]) == 1, metaMapping.items()))
    return len(filtered) == len(metaMapping)


def part1(meta, tickets):
    invalid = []

    for ticket in tickets:
        for number in ticket:
            if not isValid(number, meta):
                invalid.append(number)
                continue

    print("Total:", sum(invalid))


def part2(meta, tickets):
    validTickets = []
    noOfFields = len(tickets[0])

    for ticket in tickets:
        validCounter = 0
        for number in ticket:
            if not isValid(number, meta):
                break
            else:
                validCounter += 1

        if validCounter == noOfFields:
            validTickets.append(ticket)

    print("Valid Tickets:", validTickets)

    noOfTickets = len(validTickets)
    metaMapping = {}
    for key, value in meta.items():
        metaMapping[key] = []

        for i in range(noOfFields):
            validCounter = 0
            for tickets in validTickets:
                if isValid(tickets[i], {key: value}):
                    validCounter += 1
            if validCounter == noOfTickets:
                metaMapping[key] += [i]

    metaMapping = pinPointFields(metaMapping)

    # print(meta)
    print(*metaMapping.items(), sep="\n")

    answerList = [1]
    for key, value in metaMapping.items():
        if "departure" in key:
            answerList.append(validTickets[0][value[0]])

    print("Total:", reduce(lambda x, y: x * y, answerList))


filename = "..\\data\\d16_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")
print()

meta = {}
tickets = []
init(meta, tickets)


part1(meta, tickets)
part2(meta, tickets)
