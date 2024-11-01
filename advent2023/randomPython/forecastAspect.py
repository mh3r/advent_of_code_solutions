import json
import re

HASH = "#"
PUBLIC = "-public"
MODEL = "model/"
ASTERISK = "*"


def printJson(object):
    print(json.dumps(object, indent=2))


def guesstimateFormat(label):
    retval = "N0"

    if "per" in label and "oper" not in label:
        retval = "N2"
    return retval


def fileToLines(filePath):
    lines = open(filePath, "r").readlines()
    lines = list(map(lambda x: x.strip(), lines))
    return lines


def run(mainFile, arcExportFile, arcforecastCsFile):
    mainLines = fileToLines(mainFile)
    mainLines = list(filter(lambda x: x, mainLines))

    arcExportLines = fileToLines(arcExportFile)
    arcExportLines = list(filter(lambda x: ASTERISK in x, arcExportLines))

    arcForecastLines = fileToLines(arcforecastCsFile)

    labelPathMapping = {}

    for line in arcExportLines:
        # print (line)
        splitted = line.split(" * ")
        label = splitted[0].strip()
        path = MODEL + splitted[1].strip().split(".")[1]

        labelPathMapping[label] = path

    for line in arcForecastLines:
        splitted = line.split(" * ")
        label = splitted[1].strip()
        path = MODEL + splitted[0].strip()

        labelPathMapping[label] = path

    for line in mainLines:
        # print (line)

        if line.startswith("="):
            print("</group>")
            print(f"<group name='{line[1:] }'>")
        else:
            path = MODEL + "_blank"
            if line in labelPathMapping:
                path = labelPathMapping[line]
            print(f"<value path='{path}' label='{line}' />")


def run2(mainFile):
    stringTemplate = """                                <div class="R text generalS">
                                    <div class="block" style="width: 25px;">
                                        <input type="checkbox" id="" name="{1}" group="ratio" /></div>
                                    <div class="block" style="width: 147px;">
                                        {2}</div>
                                </div>
                                """

    stringTemplate = '            colMapper.Add("{1}", "{2}");'

    mainLines = fileToLines(mainFile)
    mainLines = list(filter(lambda x: x, mainLines))

    for line in mainLines:
        # print (line)
        splitted = line.split(" * ")
        label = splitted[0].strip()
        path = splitted[1].strip()

      
        print(stringTemplate.replace("{2}", label).replace("{1}", path))

def run3(mainFile):   
    mainLines = fileToLines(mainFile)
    # mainLines = list(filter(lambda x: x, mainLines))

    
    for i, line in enumerate(mainLines):
        #print (i, line)
        if ("label" in line): 
            label_value = re.search(r'label="([^"]+)"', line).group(1)
            if (len(label_value) >= 27):
                print (i + 1, label_value)

    


mainFile = "C:\\stash\\aspectweb\\web\\src\\main\\resources\\xml\\arcxml\\stock\\forecasts.xml"
arcExportFile = "C:\\dled\\arc_export_labelDBMapping.txt"
arcforecastCsFile = "C:\\dled\\arc_forecast_cs.txt"


# run(mainFile, arcExportFile, arcforecastCsFile)

#run2(mainFile)

run3(mainFile)


