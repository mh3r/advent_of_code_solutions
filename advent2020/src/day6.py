import functools
import util
import re
import json
import os 

filename = "..\\data\\d6_input.txt"
# filename = "..\\data\\test.txt"
abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()


def extractValue(key, input):
    retval = None
    if key in input:
        retval = input.split(key + ":")[1].split(" ")[0]
    return retval



uniqueAnswers = []
tmpSet = set()
groupAnswers = []
tmpList = []
uniqueAnswers.append(tmpSet)
groupAnswers.append(tmpList)


# somehow this doesnt work
def groupCounter(a, b):
    print(a)
    print(type(a))

    # print(b)
    return len(a) + len(b)


for line in lines:
    line = line.strip()
    if line == "":
        tmpSet = set()
        uniqueAnswers.append(tmpSet)
        tmpList = []
        groupAnswers.append(tmpList)
    else:
        tmpSet.update(list(line))
        tmpList.append(line)


def part1():
    count = 0
    # total = functools.reduce(groupCounter, uniqueAnswers)
    print(sum(len(elem) for elem in uniqueAnswers))


def part2():
    count = 0
    for index, groupAnswer in enumerate(groupAnswers):
        for uniqueAnswer in list(uniqueAnswers[index]):
            if all(uniqueAnswer in x for x in groupAnswer):
                count += 1
    print(count)


print("uniqueAnswers", uniqueAnswers)
print("groupAnswers", groupAnswers)


part1()
part2()
