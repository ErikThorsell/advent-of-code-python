"""Solution module for Day X, YEAR"""
import time
from typing import Tuple

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def compute_power_level_for_fuel_cell(x, y, grid_serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level = power_level * rack_id
    power_level = int(str(power_level)[-3]) if power_level > 99 else 0
    return power_level - 5


def compute_total_power(x, y, grid_serial_number: int, rectangle_dimensions: Tuple[int, int]) -> int:
    total_power = 0
    for ix in range(x, x + rectangle_dimensions[0]):
        for iy in range(y, y + rectangle_dimensions[1]):
            total_power += compute_power_level_for_fuel_cell(ix, iy, grid_serial_number)
    return total_power


def solution_1(grid_serial_number: int) -> Tuple[int, int]:
    highest_power = 0
    best_coordinate = (-1, -1)
    for x in range(1, 301):
        for y in range(1, 301):
            if (power := compute_total_power(x, y, grid_serial_number, (3, 3))) > highest_power:
                highest_power = power
                best_coordinate = (x, y)
    return best_coordinate


# https://www.reddit.com/r/adventofcode/comments/a53r6i/comment/ebjoijs/
def solution_2(grid_serial_number: int) -> Tuple[int, int]:
    grid = [[0 for _ in range(301)] for _ in range(301)]
    for x in range(1, 301):
        for y in range(1, 301):
            grid[x][y] = compute_power_level_for_fuel_cell(x, y, grid_serial_number)

    # Partial sums
    for x in range(1, 301):
        for y in range(1, 301):
            grid[x][y] = grid[x][y] + grid[x - 1][y] + grid[x][y - 1] - grid[x - 1][y - 1]

    ans = (0, (0, 0, 0))
    for blk in range(1, 300):
        for x in range(1, 300 - blk + 1):
            for y in range(1, 300 - blk + 1):
                tot = grid[x + blk][y + blk] - grid[x][y + blk] - grid[x + blk][y] + grid[x][y]

                ans = max(ans, (tot, (x + 1, y + 1, blk)))

    return ans[1]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(int(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(int(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
