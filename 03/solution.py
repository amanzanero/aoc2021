from util import parseLines

def most_common_at(iterable, position):
    zero_count = 0
    one_count = 0
    for row in iterable:
        if row[position] == "0":
            zero_count += 1
        else:
            one_count += 1
    return (0, 1) if zero_count > one_count else (1, 0)

def part1():
    lines = parseLines("input.txt")
    gamma = ""
    epsilon = ""

    for i in range(len(lines[0])):
        most_common, least_common = most_common_at(lines, i)
        gamma += str(most_common)
        epsilon += str(least_common)

    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    lines = parseLines("input.txt")

    oxygen = lines
    co2 = lines
    for position in range(len(lines[0])):
        most_common, _ = most_common_at(oxygen, position)
        next_oxygen = list(filter(lambda x: x[position] == str(most_common) and len(lines) > 1, oxygen))
        if len(next_oxygen) == 0:
            oxygen = oxygen
        else:
            oxygen = next_oxygen


        _, least_common = most_common_at(co2, position)
        next_co2 = list(filter(lambda x: x[position] == str(least_common), co2))
        if len(next_co2) == 0:
            co2 = co2
        else:
            co2 = next_co2

    print(int(oxygen[0], 2) * int(co2[0], 2))


if __name__ == '__main__':
    part1()
    part2()
