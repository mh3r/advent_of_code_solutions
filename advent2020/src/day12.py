# from parse import *
from functools import reduce
import util
import re
import json
import os
import types
import math

consts = types.SimpleNamespace()
consts.EAST = "E"
consts.NORTH = "N"
consts.WEST = "W"
consts.SOUTH = "S"
consts.FORWARD = "F"
consts.LEFT = "L"
consts.RIGHT = "R"
consts.COMPASS = [consts.NORTH, consts.EAST, consts.SOUTH, consts.WEST]


def switchToTest():
    global filename
    filename = "..\\data\\test.txt"


class Ferry:
    def __init__(self):
        self.f_direction = consts.EAST
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.x = 0
        self.y = 0

    def instruction(self, line):
        direction = line[0]
        steps = int(line[1:])

        match direction:
            case consts.RIGHT | consts.LEFT:
                self.rotate(direction, steps)
            case _:
                absoluteDirection = direction
                if direction == consts.FORWARD:
                    absoluteDirection = self.f_direction
                self.move(absoluteDirection, steps)

    def move(self, direction, steps):
        match direction:
            case consts.NORTH:
                self.y += steps
            case consts.SOUTH:
                self.y -= steps
            case consts.WEST:
                self.x -= steps
            case consts.EAST:
                self.x += steps

    def rotate(self, direction, steps):
        if direction == consts.LEFT:
            steps = 360 - steps
        indexIncrement = int(steps / 90)

        tmpIndex = list.index(consts.COMPASS, self.f_direction)
        self.f_direction = consts.COMPASS[
            int(tmpIndex + indexIncrement) % len(consts.COMPASS)
        ]

    def printManhattan(self):
        print(abs(self.x) + abs(self.y))

    def instruction_p2(self, line):
        direction = line[0]
        steps = int(line[1:])

        match direction:
            case consts.FORWARD:
                self.move_p2(steps)
            case consts.RIGHT | consts.LEFT:
                self.rotate_p2(direction, steps)
            case _:
                self.changeWaypoint(direction, steps)

    def move_p2(self, magnitude):
        self.y += magnitude * self.waypoint_y
        self.x += magnitude * self.waypoint_x

    def changeWaypoint(self, direction, steps):
        match direction:
            case consts.NORTH:
                self.waypoint_y += steps
            case consts.SOUTH:
                self.waypoint_y -= steps
            case consts.WEST:
                self.waypoint_x -= steps
            case consts.EAST:
                self.waypoint_x += steps

    # taken from somewhere .. was initially going thorugh quadrant .. etc
    def rotate_p2(self, direction, steps):
        if direction == consts.RIGHT:
            steps = 360 - steps
        px, py = self.waypoint_x, self.waypoint_y
        angle = math.radians(steps)
        self.waypoint_x = round(math.cos(angle) * px - math.sin(angle) * py)
        self.waypoint_y = round(math.sin(angle) * px + math.cos(angle) * py)


def part1():
    ferry = Ferry()
    for line in lines:
        ferry.instruction(line)
    # print(ferry)
    print(json.dumps(ferry.__dict__))
    ferry.printManhattan()
    pass


def part2():
    ferry = Ferry()
    for line in lines:
        ferry.instruction_p2(line)
    # print(ferry)
    print(json.dumps(ferry.__dict__))
    ferry.printManhattan()
    pass


filename = "..\\data\\d12_input.txt"
switchToTest()

abs_file_path = os.path.join(os.path.dirname(__file__), filename)
lines = open(abs_file_path, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))

# print(*lines, sep="\n")

part1()
part2()
