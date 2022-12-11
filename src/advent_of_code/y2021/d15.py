"""Solution module for Day X, YEAR"""
import copy
import time

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import dijkstra_grid
from advent_of_code.utils.parse import parse_grid


def solution_1(input):
    return dijkstra_grid(input, (0, 0), (len(input) - 1, len(input[0]) - 1))


def solution_2(input):
    exn = 5
    height = input.shape[0]
    width = input.shape[1]
    expanded_grid = np.zeros((height * exn, width * exn))

    for rx, row in enumerate(expanded_grid):
        for cx, _ in enumerate(row):
            dist = rx // height + cx // width
            expanded_value = input[rx % height, cx % width]
            for _ in range(dist):
                expanded_value += 1
                if expanded_value == 10:
                    expanded_value = 1
            expanded_grid[rx, cx] = expanded_value

    return dijkstra_grid(
        expanded_grid, (0, 0), (len(expanded_grid) - 1, len(expanded_grid[0]) - 1)
    )


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_grid(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
