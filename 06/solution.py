import math

from util import parseLines
from pprint import pprint


def parse_lines():
    lines = parseLines("input.txt")
    return [int(num) for num in lines[0].split(",")]


def part1():
    fish = parse_lines()
    for i in range(80):
        next_fish = [f for f in fish]
        for j in range(len(fish)):
            if fish[j] == 0:
                next_fish[j] = 6
                next_fish.append(8)
            else:
                next_fish[j] -= 1
        fish = next_fish
    print(len(fish))


def part2():
    fish = parse_lines()
    count_of_days = [fish.count(i) for i in range(9)]
    for day in range(256):
        count_of_days[(day + 7) % 9] += count_of_days[day % 9]
    print(sum(count_of_days))

if __name__ == '__main__':
    part1()
    part2()
