"""Solution module for Day 14, 2022"""
import copy
from operator import itemgetter
import time
from typing import List, Tuple

from advent_of_code.utils.comb_it import sliding_window
from advent_of_code.utils.coordinates import get_coordinates_between
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def draw_cave(coordinates: List[Tuple[int, int]]) -> None:
    x_min = min(coordinates, key=itemgetter(0))[0]
    y_min = 0
    x_max = max(coordinates, key=itemgetter(0))[0]
    y_max = max(coordinates, key=itemgetter(1))[1]
    print()
    for y in range(y_min, y_max + 1):  # loop y first to get same output as AoC
        for x in range(x_min, x_max + 1):
            if (x, y) in coordinates:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def to_int(s_tuple):
    sx, sy = s_tuple.split(",")
    return (int(sx), int(sy))


def parse(input):
    rock_segments = list()
    for path in input:
        points = path.split(" -> ")
        for p1, p2 in sliding_window(points, 2):
            c1 = to_int(p1)
            c2 = to_int(p2)
            rock_segments.extend(get_coordinates_between(c1, c2))

    return rock_segments


# Guesses for Part 1
#  99 | Too large
def solution_1(input):
    segments = parse(input)
    draw_cave(segments)


# Guesses for Part 2
# 97 | Too small
def solution_2(input):
    pass


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
