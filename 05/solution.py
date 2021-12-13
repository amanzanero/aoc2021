import math

from util import parseLines
from pprint import pprint


def parse_lines():
    lines = parseLines("input.txt")
    segments = []
    for line in lines:
        left, right = line.split(" -> ")
        x1, y1 = left.split(",")
        x2, y2 = right.split(",")
        segments.append((
            (int(x1), int(y1)),
            (int(x2), int(y2))
        ))
    return segments


def part1():
    segments = parse_lines()
    points = {}

    for segment in segments:
        (x1, y1), (x2, y2) = segment
        if x1 == x2:
            if y1 < y2:
                r = range(y1, y2 + 1)
            else:
                r = range(y2, y1 + 1)

            for i in r:
                if (x1, i) not in points:
                    points[(x1, i)] = 0
                points[(x1, i)] += 1

        if y1 == y2:
            if x1 < x2:
                r = range(x1, x2 + 1)
            else:
                r = range(x2, x1 + 1)

            for i in r:
                if (i, y1) not in points:
                    points[(i, y1)] = 0
                points[(i, y1)] += 1

    print(sum(x >= 2 for x in points.values()))


def part2():
    segments = parse_lines()
    points = {}

    for segment in segments:
        (x1, y1), (x2, y2) = segment

        delta_y = 1
        delta_x = 1

        if y1 > y2:
            delta_y *= -1

        if x1 > x2:
            delta_x *= -1

        x, y = x1, y1
        while True:
            if (x, y) not in points:
                points[(x, y)] = 0
            points[(x, y)] += 1

            if y != y2:
                y += delta_y

            if x != x2:
                x += delta_x

            if (x, y) == (x2, y2):
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
                break

    print(sum(x >= 2 for x in points.values()))


if __name__ == '__main__':
    part1()
    part2()
