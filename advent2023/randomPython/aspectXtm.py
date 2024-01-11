import xml.etree.ElementTree as ET


HASH = "#"
PUBLIC = "-public"


def findTopicIdByUrlPath(wantedPath, root, parentMap):
    topicId = None

    for node in root.iter("baseNameString"):
        if node.text == wantedPath:
            grandParent = parentMap[parentMap[node]]
            topicId = grandParent.attrib["id"]
            break
    return topicId


def findLicenseesByMember(topicId, root, parentMap):
    licensees = set()
    retval = []

    for node in root.iter("topicRef"):
        for key in node.attrib:
            if HASH + topicId == node.attrib[key]:
                associationNode = parentMap[parentMap[node]]
                scope = associationNode.find("scope")
                for licenseeNode in scope:
                    for key in licenseeNode.attrib:
                        licensees.add(licenseeNode.attrib[key].replace(HASH, ""))

    retval = list(licensees)
    retval.sort()
    return retval


def filterPublic(licensees):
    retval = []
    if licensees:
        licenseesWithPublic = list(filter(lambda x: PUBLIC in x, licensees))
        licenseesWithoutPublic = list(filter(lambda x: PUBLIC not in x, licensees))

        dedupPublic = list(
            filter(
                lambda x: x.split("-")[0] not in licenseesWithoutPublic,
                licenseesWithPublic,
            )
        )
        retval = licenseesWithoutPublic + dedupPublic
    return retval


# given url, it will try to find all available xtm-licensees (with -public removed)
def run(filePath, wantedPath):
    tree = ET.parse(filePath)
    root = tree.getroot()
    parentMap = {c: p for p in tree.iter() for c in p}

    topicId = findTopicIdByUrlPath(wantedPath, root, parentMap)
    licensees = findLicenseesByMember(topicId, root, parentMap)
    licensees = filterPublic(licensees)
    print(f'Licensees with path "{wantedPath}":')
    print(*licensees, sep="\n")


filePath = "C:\\stash\\aspectweb\\web\\src\\main\\resources\\xtm\\aspect.xtm"
wantedPath = "/af/company/ahresearch"


run(filePath, wantedPath)
