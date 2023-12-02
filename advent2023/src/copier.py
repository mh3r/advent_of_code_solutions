import os
import requests
import creds

srcPath = "advent2023/src/"
dataPath = "advent2023/data/"
dayXFileName = "dayx.py"
DX_INPUT = "dx_input"
dayNumber = len(list(filter(lambda x: "day" in x, os.listdir(srcPath))))
newSrcName = srcPath + "day{}.py".format(dayNumber)
newDataName = dataPath + "d{}_input.txt".format(dayNumber)
aocUrl = "https://adventofcode.com/2023/day/" + str(dayNumber) + "/input"


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


copySrc()
downloadInputFile()

#  python -m pip install requests
