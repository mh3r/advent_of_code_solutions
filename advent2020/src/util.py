import parse


def parseToList(template, input):
    return list(parse.parse(template, input))
