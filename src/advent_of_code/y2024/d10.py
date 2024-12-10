"""Solution module for Day 10, 2024"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.coordinates import draw_coordinates_dict
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_grid, split_str_by_newline


def test_1():
    input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    answer = 36
    assert(solution_1(input) == answer)
    

def test_2():
    input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    answer = 81
    assert(solution_2(input) == answer)


def is_valid(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= x < rows and 0 <= y < cols


def dfs(grid, x, y, visited, reachable_nines=None):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if grid[x][y] == 9:
        if reachable_nines is None:
            return 1
        else:
            reachable_nines.add((x, y))

    path_count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(grid, nx, ny) and (nx, ny) not in visited:
            if grid[nx][ny] == grid[x][y] + 1:
                visited.add((nx, ny))
                if reachable_nines is None:
                    path_count += dfs(grid, nx, ny, visited)
                else:
                    dfs(grid, nx, ny, visited, reachable_nines)
                visited.remove((nx, ny))
    
    if reachable_nines is None:
        return path_count


def solution_1(input):
    grid = [list(map(int, line)) for line in input.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    trailhead_scores = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                reachable_nines = set()
                visited = {(i, j)}
                dfs(grid, i, j, visited, reachable_nines)
                trailhead_scores.append(len(reachable_nines))

    return sum(trailhead_scores)


def solution_2(input):
    grid = [list(map(int, line)) for line in input.splitlines()]
    rows = len(grid)
    cols = len(grid)

    trailhead_ratings = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                visited = {(i, j)}
                rating = dfs(grid, i, j, visited)
                trailhead_ratings.append(rating)

    return sum(trailhead_ratings)


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
