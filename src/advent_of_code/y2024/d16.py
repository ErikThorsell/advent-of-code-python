"""Solution module for Day 16, 2024"""
from collections import defaultdict
import copy
import heapq
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    answer = 7036
    assert(solution_1(input) == answer)
    

def test_2():
    input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    answer = 45
    assert(solution_2(input) == answer)


def parse(input):
    return [list(row) for row in input.splitlines()]


def find_start_and_end(grid):
    start = end = None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return start, end


def get_neighbors(pos, direction, grid):
    x, y = pos
    directions = ["E", "S", "W", "N"]
    dir_idx = directions.index(direction)
    
    dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][dir_idx]
    nx, ny = (x + dx, y + dy)

    neighbors = []
    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[nx][ny] != '#':
        neighbors.append(((nx, ny), direction, 1))

    for rotation in [-1, 1]:
        n_dir = directions[(dir_idx + rotation) % 4]
        neighbors.append((pos, n_dir, 1000))

    return neighbors


def find_path(grid, start, end, part=1):
    pq = []
    heapq.heappush(pq, (0, (start, "E")))

    dists = defaultdict(lambda: maxsize)
    predecessors = defaultdict(lambda: set())
    while pq:
        dist, (pos, dir) = heapq.heappop(pq)

        if pos == end and part == 1:
            return dist

        for n_pos, n_dir, cost in get_neighbors(pos, dir, grid):
            n_dist = dist + cost
            state = (n_pos, n_dir)

            if n_dist < dists[state]:
                dists[state] = n_dist
                predecessors[state] = {(pos, dir)}
                heapq.heappush(pq, (n_dist, state))
            elif n_dist == dists[state]:
                predecessors[state].add((pos, dir))
    
    return predecessors, (end, dir)
    

def solution_1(input):
    grid = parse(input)
    start, end = find_start_and_end(grid)
    return find_path(grid, start, end)


def solution_2(input):
    grid = parse(input)
    start, end = find_start_and_end(grid)
    predecessors, last = find_path(grid, start, end, part=2)

    stack = [last]
    tiles = set(stack)
    while stack:
        tile = stack.pop(-1)

        for n_tile in predecessors[tile]:
            if n_tile not in tiles:
                tiles.add(n_tile)
                stack.append(n_tile)

    tiles = set(t[0] for t in tiles)

    return len(tiles)



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
