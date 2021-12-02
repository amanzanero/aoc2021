def parsePosittions(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    col = []
    for line in lines:
        position, num = line.split()
        col.append((position, int(num)))
    return col


def part1():
    pos = parsePosittions("input.txt")
    x, y = 0, 0

    for p in pos:
        position, depth = p
        if position == "forward":
            x += depth
        elif position == "up":
            y -= depth
        elif position ==    "down":
            y += depth

    print(x * y)

def part2():
    pos = parsePosittions("02/input.txt")
    x, y, aim = 0, 0, 0

    for p in pos:
        position, depth = p
        if position == "forward":
            x += depth
            y += aim * depth
        elif position == "up":
            aim -= depth
        elif position == "down":
            aim += depth

    print(x * y)



if __name__ == '__main__':
    part1()
    part2()
