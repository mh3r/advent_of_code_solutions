import functools
import util
import re
import json

NO_OTHER = "no other"
THE_ONE =  "shiny gold"


def extractValue(key, input):
    retval = None
    if key in input:
        retval = input.split(key + ":")[1].split(" ")[0]
    return retval


file = "C:\\aoc\\data.txt"
file = "C:\\aoc\\sample.txt"

lines = open(file, "r").readlines()


class Bag:
    def __init__(self, input):
        split = input.split(" contain ")
        self.name = split[0]
        tmpSecond = split[1]
        self.kids = None
        self.parents               = None
        if NO_OTHER != tmpSecond:
            self.kids = []
            kids = split[1].split(", ")
            print(kids)
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
    print(line)

def findLineage():
    shinyParents =  []
    parents = [THE_ONE]

    while len(parents) > 0:
        current = parents.pop(0)
        for bag in bags:
            if bag.kids != None:
                for kid in bag.kids:
                    if kid.name ==  current:
                        pass
        pass

def part1():
    pass


def part2():
    pass


part1()
part2()


print(json.dumps(bags, default=lambda x: x.__dict__, indent=2))
