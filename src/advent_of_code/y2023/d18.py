"""Solution module for Day 18, 2023"""
import copy
import time

from advent_of_code.utils.grid import get_grid_area
from advent_of_code.utils.fetch import fetch


def test_1():
    input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
    answer = 62
    assert(solution_1(input) == answer)
    

def test_2():
    input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
    answer = 952408144115
    assert(solution_2(input) == answer)


def parse(input, part=1):
    move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

    x, y = 0, 0
    borders = []
    for row in input.split("\n"):

        if part == 1:
            dir_, dist, _ = row.split()
        if part == 2:
            _, _, colour = row.split()
            colour = colour[1:-1]
            dir_ = dirs[colour[-1]]
            dist = int(colour[1:-1], 16) 

        dx, dy = move[dir_]

        for _ in range(int(dist)):
            x, y = x + dx, y + dy
            borders.append((x, y))

    return borders


def solution_1(input):
    borders = parse(input)
    return get_grid_area(borders)

def solution_2(input):
    borders = parse(input, part=2)
    return get_grid_area(borders)


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
