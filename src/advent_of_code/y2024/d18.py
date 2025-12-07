"""Solution module for Day 18, 2024"""
from collections import defaultdict
import copy
from heapq import heapify, heappop, heappush
import time
from sys import maxsize

from advent_of_code.utils.coordinates import draw_coordinates_dict
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import dijkstra_grid, get_adjacent


def test_1():
    input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    answer = 22
    assert(solution_1(input) == answer)
    

def test_2():
    input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
    answer = 6,1
    assert(solution_2(input) == answer)


def parse(input, dims, bytes):
    grid = {}
    for x in range(dims[0]+1):
        for y in range(dims[1]+1):
            grid[(x, y)] = "."

    for idx, row in enumerate(input.split("\n")):
        x, y = map(int, row.split(","))
        grid[(x, y)] = "#"
        if idx == bytes-1:
            break

    return grid


def get_neighbors(pos, grid):
    x, y = pos
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    neighbors = list()
    for dx, dy in directions:
        nx, ny = x+dx, y+dy

        if (nx, ny) in grid and grid[(nx, ny)] != "#":
            neighbors.append((nx, ny))
    
    return neighbors


def find_path(grid, start, end):
    pq = []
    heappush(pq, (0, start))

    dists = defaultdict(lambda: maxsize)
    predecessors = defaultdict(lambda: set())
    while pq:
        dist, pos = heappop(pq)

        if pos == end:
            return dist

        for nx, ny in get_neighbors(pos, grid):
            n_dist = dist + 1
            n_pos = (nx, ny)

            if n_dist < dists[n_pos]:
                dists[n_pos] = n_dist
                predecessors[n_pos] = {pos}
                heappush(pq, (n_dist, n_pos))
        

def solution_1(input):
    grid = parse(input, (70, 70), 1024)
    dist = find_path(grid, (0, 0), (70, 70))
    return dist


def solution_2(input):
    lower = 1024
    upper = 1024

    while True:
        grid = parse(input, (70, 70), upper)
        dist = find_path(grid, (0, 0), (70, 70))
        if dist is None:
            break
        else:
            lower = upper
            upper *= 2
    
    while lower < upper:
        mid = (lower + upper) // 2
        grid = parse(input, (70, 70), mid)
        dist = find_path(grid, (0, 0), (70, 70))

        if dist is None:
            upper = mid
        else:
            lower = mid+1
    
    return input.split("\n")[lower-1]
            


def run(year: int, day: int):
    print(f"🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
