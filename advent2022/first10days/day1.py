
# gold code sample 
# https://github.com/kajott/adventofcode/blob/master/2022/01/aoc2022_01_part1.py
print("gold code sample -------")

filename = "C:\\github\\aoc\\advent2022\\data\\d1_input.txt"
print (max(sum(map(int,E.split()))for E in open(filename).read().split("\n\n")))