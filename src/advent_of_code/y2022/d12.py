"""Solution module for Day 12, 2022"""
from collections import deque
import copy
from heapq import heapify, heappop, heappush
import time
from sys import maxsize

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import get_adjacent
from advent_of_code.utils.parse import split_str_by_newline


def parse(rows):
    grid = np.zeros((len(rows), len(rows[0])))

    for rx, row in enumerate(rows):
        for cx, col in enumerate(row):

            if col == "S":
                n_col = ord("a") - 96
            elif col == "E":
                n_col = ord("z") - 96
            else:
                n_col = ord(col) - 96

            grid[rx, cx] = n_col

    return grid


def find(grid, chr):
    rows, cols = len(grid), len(grid[0])
    return [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == chr]


def inbound(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def path_dijkstra(grid, sr, sc, er, ec):

    distances = {}
    distances[(sr, sc)] = 0
    for rx in range(len(grid)):
        for cx in range(len(grid[rx])):
            if (rx, cx) != (sr, sc):
                distances[(rx, cx)] = maxsize

    heap = [(0, (sr, sc))]
    heapify(heap)

    while heap:
        dist, (r, c) = heappop(heap)

        if (r, c) == (er, ec):
            return dist

        for (nr, nc) in get_adjacent(r, c, 4):
            if inbound(grid, nr, nc) and grid[nr][nc] - grid[r][c] <= 1:
                n_dist = dist + 1
                if distances[(nr, nc)] <= n_dist:
                    continue
                distances[(nr, nc)] = n_dist
                heappush(heap, (n_dist, (nr, nc)))

    return maxsize


def path(grid, sr, sc, er, ec):
    rows, cols = len(grid), len(grid[0])
    steps = [[maxsize] * cols for _ in range(rows)]
    steps[sr][sc] = 0

    Q = deque([(sr, sc)])

    while Q:
        r, c = Q.popleft()
        for nr, nc in get_adjacent(r, c, 4):
            if inbound(grid, nr, nc) and steps[nr][nc] == maxsize and grid[nr][nc] - grid[r][c] <= 1:
                steps[nr][nc] = steps[r][c] + 1
                Q.append((nr, nc))

    return steps[er][ec]


# Guesses for Part 1
def solution_1(input):
    sr, sc = find(input, "S")[0]
    er, ec = find(input, "E")[0]
    grid = parse(input)
    return path(grid, sr, sc, er, ec)


# Guesses for Part 2
def solution_2(input):
    er, ec = find(input, "E")[0]
    grid = parse(input)
    min_dist = maxsize
    for (sr, sc) in find(input, "a"):
        min_dist = min(min_dist, path(grid, sr, sc, er, ec))
    return min_dist


# Guesses for Part 3
def solution_3(input):
    sr, sc = find(input, "S")[0]
    er, ec = find(input, "E")[0]
    grid = parse(input)
    return path_dijkstra(grid, sr, sc, er, ec)


# Guesses for Part 4
def solution_4(input):
    er, ec = find(input, "E")[0]
    grid = parse(input)
    min_dist = maxsize
    for (sr, sc) in find(input, "a"):
        min_dist = min(min_dist, path_dijkstra(grid, sr, sc, er, ec))
    return min_dist


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

    tic = time.perf_counter()
    s3 = solution_3(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1 with Dijkstra: {s3}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s4 = solution_4(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2 with Dijkstra: {s4}, acquired in: {toc-tic:0.4f} seconds")
