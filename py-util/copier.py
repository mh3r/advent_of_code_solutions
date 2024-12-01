import os
import requests
import creds

YEAR = 2024
srcPath = "advent{}/src/".format(YEAR)
dataPath = "advent{}/data/".format(YEAR)
dayXFileName = "dayx.py"
DX_INPUT = "dx_input"
cwd = os.getcwd()

dayNumber, newSrcName, newDataName, aocUrl = [None, None, None, None]

abs_file_path = os.path.join(os.path.dirname(__file__), dayXFileName)

def init():
    global dayNumber, newSrcName, newDataName, aocUrl
    if not os.path.exists(srcPath):
        os.makedirs(srcPath)

    if not os.path.exists(dataPath):
        os.makedirs(dataPath)
        open(dataPath + "test.txt", 'a').close()

    dayNumber = len(list(filter(lambda x: "day" in x, os.listdir(srcPath)))) + 1
    newSrcName = srcPath + "day{}.py".format(dayNumber)
    newDataName = dataPath + "d{}_input.txt".format(dayNumber)
    aocUrl = "https://adventofcode.com/{}/day/{}/input".format(YEAR, dayNumber)


def copySrc():
    abs_file_path = os.path.join(os.path.dirname(__file__), dayXFileName)
    lines = open(abs_file_path, "r").readlines()

    contents = []
    for line in lines:
        if DX_INPUT in line:
            line = line.replace(DX_INPUT, "d{}_input".format(dayNumber))
        contents.append(line)

    with open(newSrcName, "w") as the_file:
        for line in contents:
            the_file.write(line)
    print("Created: " + newSrcName)


def downloadInputFile():
    request = requests.get(
        aocUrl, allow_redirects=True, headers={"cookie": creds.COOKIE}
    )

    with open(newDataName, "wb") as file:
        file.write(request.content[:-1])
    print("Created: " + newDataName)


init()
copySrc()
downloadInputFile()

#  python -m pip install requests
