def parseInts(filename: str) -> [int]:
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [int(line) for line in lines]


def num_increases(depths):
    numIncreaases = 0

    for i in range(len(depths)):
        if i == 0:
            continue

        if depths[i] > depths[i - 1]:
            numIncreaases += 1
    return numIncreaases



def part1():
    depths = parseInts("inputs/input1.txt")
    print(f"part 1 - number of increases={num_increases(depths)}")

def part2():
    depths = parseInts("inputs/input1.txt")

    averaged_depths = []

    for i in range(len(depths)):
        if i < 2:
            continue
        averaged_depths.append(sum(depths[i-2:i+1]))

    print(f"part 2 - num increases = {num_increases(averaged_depths)}")

if __name__ == '__main__':
    part1()
    part2()