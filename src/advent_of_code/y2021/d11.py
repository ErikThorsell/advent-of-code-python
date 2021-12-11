"""Solution module for Day X, YEAR"""
import copy
import time

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import get_adjacent
from advent_of_code.utils.parse import parse_grid


def step(grid):
    grid += 1
    step_flashes = np.argwhere(grid > 9)
    flashed = list()
    new_flash = True if len(step_flashes) > 0 else False
    while new_flash:
        for c in step_flashes:
            if (c[0], c[1]) in flashed:
                continue
            flashed.append((c[0], c[1]))
            for (nx, ny) in get_adjacent(c[0], c[1], 8):
                if ny < 0 or ny >= len(grid):
                    continue
                if nx < 0 or nx >= len(grid[0]):
                    continue
                grid[nx, ny] += 1
        sub_flashes = np.argwhere(grid > 9)
        if len(sub_flashes) > len(step_flashes):
            step_flashes = sub_flashes
        else:
            new_flash = False

    for (cx, cy) in np.argwhere(grid > 9):
        grid[cx, cy] = 0

    return grid, len(flashed)


def solution_1(input):
    flashes = 0
    for _ in range(100):
        input, step_flash = step(input)
        flashes += step_flash
    return flashes


def solution_2(input):
    steps = 0
    while True:
        input, step_flash = step(input)
        steps += 1
        if step_flash == input.size:
            return steps


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
