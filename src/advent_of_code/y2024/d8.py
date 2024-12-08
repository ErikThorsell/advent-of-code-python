"""Solution module for Day 8, 2024"""
from collections import defaultdict
import copy
from math import gcd
import time
from sys import maxsize

from advent_of_code.utils.coordinates import draw_coordinates_dict, get_grid_dimensions_dict
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def test_1():
    input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    answer = 14
    assert(solution_1(input) == answer)
    

def test_2():
    input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    answer = 34
    assert(solution_2(input) == answer)


def parse(input):
    rows = split_str_by_newline(input)

    grid = {}
    antennas = defaultdict(list)

    for rx, row in enumerate(rows):
        for cx, col in enumerate(row):
            grid[(cx, rx)] = col
            if col != ".":
                antennas[col].append((cx, rx))

    return grid, antennas


def solution_1(input):
    grid, antennas = parse(input)
    dims = get_grid_dimensions_dict(grid)

    antinodes = set()
    for _, pos in antennas.items():
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                dx = x2 - x1
                dy = y2 - y1

                anti_x = x1 - dx
                anti_y = y1 - dy
                if 0 <= anti_x < dims[1] and 0 <= anti_y < dims[0]:
                    antinodes.add((anti_x, anti_y))

                banti_x = x2 + dx
                banti_y = y2 + dy
                if 0 <= banti_x < dims[1] and 0 <= banti_y < dims[0]:
                    antinodes.add((banti_x, banti_y))

    return len(antinodes)


def solution_2(input):
    grid, antennas = parse(input)
    dims = get_grid_dimensions_dict(grid)

    antinodes = set()
    for _, pos in antennas.items():

        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                x1, y1 = pos[i]
                x2, y2 = pos[j]

                # Line between pos[i] and pos[j]
                dx = x2 - x1
                dy = y2 - y1

                # Find GCD to normalise the vector.
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # Any point on the line can now be described as:
                # (x, y) = (x1 + k*dx, y1 + k*dy) 
                # We limit our search to the grid.
                limit = sum(dims)
                for k in range(-limit, limit+1):
                    nx = x1 + k*dx
                    ny = y1 + k*dy
                    if 0 <= nx < dims[1] and 0 <= ny < dims[0]:
                        antinodes.add((nx, ny))

    return len(antinodes)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
