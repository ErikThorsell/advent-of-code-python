"""Solution module for Day 11, 2023"""
import copy
from itertools import combinations
import time

from advent_of_code.utils.coordinates import get_grid_dimensions
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.manhattan import get_manhattan_distance


def parse(input):
    universe = {}
    for iy, row in enumerate(input.split("\n")):
        for ix, chr in enumerate(row):
            if chr == "#":
                universe[(ix, iy)] = chr
    return universe


def find_empty(universe):

    max_x, max_y = get_grid_dimensions(universe.keys())

    empty_rows = []
    for iy in range(max_y):
        if not any((x, iy) in universe for x in range(max_x)):
            empty_rows.append(iy)

    empty_columns = []
    for ix in range(max_x):
        if not any((ix, y) in universe for y in range(max_y)):
            empty_columns.append(ix)

    return empty_rows, empty_columns


def expand_universe(universe, empty_rows, empty_columns, expansion):

    max_x, max_y = get_grid_dimensions(universe.keys())

    y = 0
    expanded_universe = {}
    for iy in range(max_y):

        if iy in empty_rows:
            y += expansion

        x = 0
        for ix in range(max_x):

            if ix in empty_columns:
                x += expansion

            if (ix, iy) in universe:
                expanded_universe[(x, y)] = "#"
            
            x += 1
        y += 1
            
    return expanded_universe


def solution_1(input):
    universe = parse(input)

    empty_rows, empty_columns = find_empty(universe)
    expanded_universe = expand_universe(universe, empty_rows, empty_columns, 1)

    distances = []
    for pair in combinations(expanded_universe, 2):
        distances.append(get_manhattan_distance(pair[0], pair[1]))
    
    return sum(distances)


def solution_2(input):
    universe = parse(input)

    empty_rows, empty_columns = find_empty(universe)
    expanded_universe = expand_universe(universe, empty_rows, empty_columns, 999999)

    distances = []
    for pair in combinations(expanded_universe, 2):
        distances.append(get_manhattan_distance(pair[0], pair[1]))
    
    return sum(distances)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
