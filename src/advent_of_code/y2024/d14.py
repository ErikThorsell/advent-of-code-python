"""Solution module for Day 14, 2024"""

import copy
from functools import reduce
from operator import mul
import time

from advent_of_code.utils.fetch import fetch


def parse(input):
    data = []
    for row in input.strip().split("\n"):
        pos, vel = row.split()
        p = tuple(map(int, pos[2:].split(",")))
        v = tuple(map(int, vel[2:].split(",")))
        data.append((p, v))
    return data


def simulate(guards, time, width, height):
    positions = []
    for pos, vel in guards:
        nx = (pos[0] + vel[0] * time) % width
        ny = (pos[1] + vel[1] * time) % height
        positions.append((nx, ny))
    return positions


def safety_factor(positions, width, height):
    quadrants = [0] * 4

    for x, y in positions:
        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[2] += 1
        elif x > width // 2 and y > height // 2:
            quadrants[3] += 1
        else:
            continue

    return reduce(mul, quadrants)


def solution_1(input):
    grid = parse(input)

    width, height = 101, 103
    positions = simulate(grid, 100, width, height)
    return safety_factor(positions, width, height)


def visualise(positions):
    xs, ys = zip(*positions)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    grid = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for x, y in positions:
        grid[y - min_y][x - min_x] = "#"

    print("\n".join("".join(row) for row in grid))


def are_unique(positions):
    seen = set()
    for pos in positions:
        if pos in seen:
            return False
        seen.add(pos)
    return True


def solution_2(input_data):
    grid = parse(input_data)

    time = 0
    width, height = 101, 103
    while True:
        positions = simulate(grid, time, width, height)
        if are_unique(positions):
            # visualise(positions)
            return time

        time += 1


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
