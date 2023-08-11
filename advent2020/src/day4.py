import util
import re
import json


def part1():
    count = 0
    print(*passports, sep="\n")

    for passport in passports:
        # passportObjects.append(Passport(passport))
        fieldLength = len(passport.split(" "))

        if (fieldLength > 6 and "cid:" not in passport) or fieldLength == 8:
            count += 1

    print(count)


def extractValue(key, input):
    retval = None
    if key in input:
        retval = input.split(key + ":")[1].split(" ")[0]
    return retval


class Passport:
    def __init__(self, passport):
        self.passport = passport

        byr = extractValue("byr", passport)
        iyr = extractValue("iyr", passport)
        eyr = extractValue("eyr", passport)

        self.byr = int(byr) if byr is not None else None
        self.iyr = int(iyr) if iyr is not None else None
        self.eyr = int(eyr) if eyr is not None else None
        self.hgt = extractValue("hgt", passport)
        self.hcl = extractValue("hcl", passport)
        self.ecl = extractValue("ecl", passport)
        self.pid = extractValue("pid", passport)
        self.valid = self.validate()

    def validate(self):
        fieldLength = len(self.passport.split(" "))
        part1Validation = (
            fieldLength == 7 and "cid:" not in self.passport
        ) or fieldLength == 8
        if not part1Validation:
            return False
        if self.byr < 1920 or self.byr > 2002:
            return False
        if self.iyr < 2010 or self.iyr > 2020:
            return False
        if self.eyr < 2020 or self.eyr > 2030:
            return False
        # height
        height = int(self.hgt[: len(self.hgt) - len("cm")])
        if "cm" in self.hgt:
            if height < 150 or height > 193:
                return False
        elif "in" in self.hgt:
            if height < 59 or height > 76:
                return False
        else:
            return False

        colourPattern = "^#[a-f0-9]{6}$"
        if not bool(re.search(colourPattern, self.hcl)):
            return False

        eyeColourPattern = "^[amb|blu|brn|gry|grn|hzl|oth]{1}"
        if not bool(re.search(eyeColourPattern, self.ecl)):
            return False

        passportIdPattern = "^[0-9]{9}$"
        if not bool(re.search(passportIdPattern, self.pid)):
            return False

        return True

    def __str__(self):
        return f"byr:{self.byr} iyr:{self.iyr} eyr:{self.eyr} hgt:{self.hgt} hcl:{self.hcl} ecl:{self.ecl} pid:{self.pid} "


def part2():
    count = 0
    validPassport = []
    for passport in passports:
        passportObj = Passport(passport)
        if passportObj.valid:
            validPassport.append(passportObj)
            # print(passportObj)
            count += 1
    print(count)

    # this was done to figure out whats wrong
    # as it turned out .. the regex isnt strict ... 
    # limiting pid to 9 actually allows for numbers above that 

    validPassport.sort(key=lambda x: x.hgt)
    print(*validPassport, sep="\n")


filename = "D:\\aoc\\advent2020\\data\\d4_input.txt"
# filename = "D:\\aoc\\advent2020\\data\\test.txt"
passports = []

# Using readlines()
file1 = open(filename, "r")
Lines = file1.readlines()

tmpLine = " "
for index, line in enumerate(Lines):
    if not line.isspace():
        tmpLine += line.strip() + " "
    else:
        passports.append(tmpLine.strip())
        tmpLine = ""
    if index == len(Lines) - 1:
        passports.append(tmpLine.strip())


# part1()
part2()

