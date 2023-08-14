import functools
import util
import re
import json
import os

NO_OTHER = "no other"
THE_ONE = "shiny gold"


def extractValue(key, input):
    retval = None
    if key in input:
        retval = input.split(key + ":")[1].split(" ")[0]
    return retval


file = "C:\\aoc\\data.txt"
file = "C:\\aoc\\sample.txt"


filename = "..\\data\\d7_input.txt"
filename = "..\\data\\test.txt"
abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()


class Bag:
    def __init__(self, input):
        split = input.split(" contain ")
        self.name = split[0]
        tmpSecond = split[1]
        self.kids = []
        if NO_OTHER != tmpSecond:
            kids = split[1].split(", ")
            for kid in kids:
                splitKid = kid.split(" ", 1)
                tmpJson = {"name": splitKid[1], "number": int(splitKid[0])}
                self.kids.append(tmpJson)


bags = []
for line in lines:
    line = line.strip()
    line = (
        line.replace(" bags.", "")
        .replace(" bag.", "")
        .replace(" bags", "")
        .replace(" bag", "")
    )

    bags.append(Bag(line))


def findLineage():
    shinyParents = []
    parents = [THE_ONE]

    while len(parents) > 0:
        current = parents.pop(0)
        for bag in bags:
            for kid in bag.kids:
                if kid["name"] == current and bag.name not in shinyParents:
                    shinyParents.append(bag.name)
                    parents.append(bag.name)
    print("the parents ... ", len(shinyParents), shinyParents)


def findDescendants(name, additions):
    retval = 0
    print(name)
    for bag in bags:
        if bag.name == name:
            if len(bag.kids) == 0:
                return 1
            else:
                for kid in bag.kids:
                    kidNumber = int(kid["number"])
                    descendant = findDescendants(kid["name"], additions)
                    if descendant != 1:
                        additions.append(kidNumber)
                    print(kidNumber, " * ", descendant)
                    retval += kidNumber * descendant

                print(retval)
                return retval


def part1():
    findLineage()


def part2():
    additions = []
    total = findDescendants(THE_ONE, additions)
    print (additions)
    total += sum(additions)
    print(total)
    pass


# part1()
part2()


# print(json.dumps(bags, default=lambda x: x.__dict__, indent=2))
