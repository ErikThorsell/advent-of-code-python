"""Solution module for Day 20, 2024"""
from collections import deque
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def parse(input):
    grid = [list(line) for line in input.split('\n')]
    start = (-1, -1)
    end = (-1, -1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start=(r,c)
            if grid[r][c] == 'E':
                end=(r,c)
    
    return grid, start, end


def bfs(grid, start):
    height, width = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    dist = [[maxsize]*width for _ in range(height)]
    dist[start[0]][start[1]]=0

    queue = deque([start])
    while queue:

        r, c = queue.popleft()
        d = dist[r][c]+1

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr <= height and 0 <= nc <= width and grid[nr][nc]!='#' and dist[nr][nc]>d:
                dist[nr][nc]=d
                queue.append((nr,nc))

    return dist


def cheat(grid, s_dist, e_dist, o_dist, cheat_size):
    height, width = len(grid), len(grid[0])

    s_cells = []
    e_cells = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] != '#':
                if s_dist[r][c] < maxsize:
                    s_cells.append((r,c))
                if e_dist[r][c] < maxsize:
                    e_cells.append((r,c))

    cheat_savings = []
    for r1, c1 in s_cells:
        base_dist = s_dist[r1][c1]

        for r2, c2 in e_cells:
            m_dist = abs(r1-r2) + abs(c1-c2)

            if m_dist <= cheat_size:
                cost = base_dist + m_dist + e_dist[r2][c2]
                saved = o_dist - cost
                if saved > 0:
                    cheat_savings.append(saved)

    return cheat_savings


def solution_1(input):
    grid, start, end = parse(input)

    s_dist = bfs(grid, start)
    e_dist = bfs(grid, end)

    o_dist = s_dist[end[0]][end[1]]

    cheat_savings = cheat(grid, s_dist, e_dist, o_dist, 2)
    return(sum(1 for s in cheat_savings if s>=100))


def solution_2(input):
    grid, start, end = parse(input)

    s_dist = bfs(grid, start)
    e_dist = bfs(grid, end)

    o_dist = s_dist[end[0]][end[1]]

    cheat_savings = cheat(grid, s_dist, e_dist, o_dist, 20)
    return(sum(1 for s in cheat_savings if s>=100))



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
