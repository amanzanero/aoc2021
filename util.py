def parseInts(filename: str) -> [int]:
    lines = parseLines(filename)
    return [int(line) for line in lines]

def parseLines(filename: str) -> [str]:
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]