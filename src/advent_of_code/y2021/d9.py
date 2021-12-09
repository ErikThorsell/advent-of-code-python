"""Solution module for Day 9, 2021"""
from collections import deque
import copy
from math import prod
import time
from sys import maxsize
from types import prepare_class
from typing import List

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import (
    parse_each_digit,
)


def risk_level(low_points: List[int]) -> int:
    return sum(low_points) + len(low_points)


def get_adjacent(x, y):
    return [
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
    ]


def get_cell(grid, ix, iy):
    if iy < 0 or iy >= len(grid):
        return maxsize
    if ix < 0 or ix >= len(grid[0]):
        return maxsize
    return grid[iy][ix]


def find_low_points(grid):
    low_points = {}
    for iy, _ in enumerate(grid):
        for ix, c in enumerate(grid[iy]):
            neighbors = [get_cell(grid, x, y) for (x, y) in get_adjacent(ix, iy)]
            if all(c < n for n in neighbors):
                low_points[(ix, iy)] = c
    return low_points


def get_basin_size(grid, root):
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        (ix, iy) = queue.popleft()
        for n in get_adjacent(ix, iy):
            if n not in visited and get_cell(grid, n[0], n[1]) < 9:
                visited.add(n)
                queue.append(n)

    return len(visited)


def solution_1(input):
    low_points = find_low_points(input)
    return risk_level(low_points.values())


def solution_2(input):
    basin_size = {}
    low_points = find_low_points(input)
    for lp in low_points:
        basin_size[lp] = get_basin_size(input, lp)
    return prod(sorted(basin_size.values(), reverse=True)[:3])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_each_digit(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
