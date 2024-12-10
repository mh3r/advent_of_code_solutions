# from email.errors import FirstHeaderLineIsContinuationDefect
# import parse


# def parseToList(template, input):
#     return list(parse.parse(template, input))
import json


ADJ_DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

ADJ_DIRS_2 = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]


def reverseString(input):
    retval = input[::-1] if not None else input
    return retval

# dont use this .. just use tuple 
def stringifyCoord(input):
    return f"{input[0]}_{input[1]}"


def decryptCoord(input):
    y, x = input.split("_")
    return [int(y), int(x)]


def printJson(object):
    print(json.dumps(object, indent=2))


def printObject(object):
    print(json.dumps(object, default=lambda x: x.__dict__, indent=2))


def manhattanDistance(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)
