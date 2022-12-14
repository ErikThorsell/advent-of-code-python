"""Solution module for Day 14, 2022"""
import copy
from operator import itemgetter
import time

from advent_of_code.utils.comb_it import sliding_window
from advent_of_code.utils.coordinates import get_coordinates_between
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    def to_int(s_tuple):
        sx, sy = s_tuple.split(",")
        return (int(sx), int(sy))

    cave = dict()
    y_max = 0
    for path in input:
        points = path.split(" -> ")
        for p1, p2 in sliding_window(points, 2):
            c1 = to_int(p1)
            c2 = to_int(p2)
            for rock in get_coordinates_between(c1, c2):
                cave[rock] = "#"
                y_max = max(y_max, rock[1])
    return cave, y_max


def add_floor(cave):
    x_min = min(cave.keys(), key=itemgetter(0))[0]
    x_max = max(cave.keys(), key=itemgetter(0))[0]
    y_max = max(cave.keys(), key=itemgetter(1))[1]
    for x in range(x_min - x_min, x_max * 2):
        cave[(x, y_max + 2)] = "#"
    return cave


def add_one_sand(cave, abyss):
    pos = (500, 0)

    while True:

        if pos[1] > abyss:
            return cave

        # Check if it's possible to fall down
        if (pos[0], pos[1] + 1) not in cave:
            pos = (pos[0], pos[1] + 1)
            continue

        # if it's not possible to fall down; go down to the left instead
        elif (pos[0] - 1, pos[1] + 1) not in cave:
            pos = (pos[0] - 1, pos[1] + 1)
            continue

        # if it's not possible to go down to the left; try down to the right
        elif (pos[0] + 1, pos[1] + 1) not in cave:
            pos = (pos[0] + 1, pos[1] + 1)
            continue

        # we're done falling
        else:
            cave[pos] = "o"
            return cave


def solution_1(input):
    cave, abyss = parse(input)

    counter = 0
    prev_amount = 0

    while True:
        cave = add_one_sand(cave, abyss)
        if len(cave) == prev_amount:
            break
        counter += 1
        prev_amount = len(cave)

    return counter


def solution_2(input):
    cave, abyss = parse(input)
    cave = add_floor(cave)

    counter = 0

    while (500, 0) not in cave:
        cave = add_one_sand(cave, abyss + 2)
        counter += 1

    return counter


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
