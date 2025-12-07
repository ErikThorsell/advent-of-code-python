"""Solution module for Day 4, 2025"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    answer = 13
    assert(solution_1(input) == answer)

def test_2():
    input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    answer = 43
    assert(solution_2(input) == answer)


def parse(input):

    grid = []

    for lidx, line in enumerate(input.split("\n")):
        grid.append([])
        for idx, item in enumerate(line):
            grid[lidx].append(item)

    return grid


def neighbours(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),         ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    for dr, dc in offsets:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield grid[nr][nc]


def solution_1(input):

    grid = parse(input)

    reachable = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                if list(neighbours(grid, i, j)).count("@") < 4:
                    reachable += 1

    return reachable


def remove(grid):

    to_remove = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                if list(neighbours(grid, i, j)).count("@") < 4:
                    to_remove.append((i, j))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in to_remove:
                grid[i][j] = '.'

    return grid, len(to_remove)


def solution_2(input):

    grid = parse(input)
    total_removed = 0
    removed = 1

    while removed > 0:
        grid, removed = remove(grid)
        total_removed += removed

    return total_removed


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    test_2()
    print("Test 2 was successful!")
    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
