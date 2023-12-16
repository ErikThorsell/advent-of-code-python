"""Solution module for Day 16, 2023"""
from collections import deque
import copy
import time

from advent_of_code.utils.coordinates import get_grid_dimensions
from advent_of_code.utils.fetch import fetch


def test_1():
    input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
    answer = 46
    assert(solution_1(input) == answer)
    

def test_2():
    input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
    answer = 51
    assert(solution_2(input) == answer)


def parse(input):
    cave = {}
    for iy, row in enumerate(input.split("\n")):
        for ix, chr in enumerate(row):
            cave[(ix, iy)] = chr
    return cave


def next_step(cave, x, y, dir):

    next_steps = []

    if dir == "N": x, y = x, y-1
    if dir == "W": x, y = x-1, y
    if dir == "S": x, y = x, y+1
    if dir == "E": x, y = x+1, y
    
    if (x, y) in cave:
        elem = cave[(x, y)]

        if elem == ".": next_steps.append(((x, y), dir))
        elif elem == "/" and dir == "N": next_steps.append(((x, y), "E"))
        elif elem == "/" and dir == "E": next_steps.append(((x, y), "N"))
        elif elem == "/" and dir == "S": next_steps.append(((x, y), "W"))
        elif elem == "/" and dir == "W": next_steps.append(((x, y), "S"))
        elif elem == "\\" and dir == "N": next_steps.append(((x, y), "W"))
        elif elem == "\\" and dir == "E": next_steps.append(((x, y), "S"))
        elif elem == "\\" and dir == "S": next_steps.append(((x, y), "E"))
        elif elem == "\\" and dir == "W": next_steps.append(((x, y), "N"))
        elif elem == "|" and dir in ["N", "S"]: next_steps.append(((x, y), dir))
        elif elem == "|" and dir in ["E", "W"]: next_steps.extend([((x, y), "N"), ((x, y), "S")])
        elif elem == "-" and dir in ["N", "S"]: next_steps.extend([((x, y), "E"), ((x, y), "W")])
        elif elem == "-" and dir in ["E", "W"]: next_steps.append(((x, y), dir))

    return next_steps


def beam(cave, start, dir):

    queue = deque()
    visited = set()
    energized = set()

    queue.append((start, dir))

    while len(queue) > 0:

        current = queue.popleft()
        visited.add(current)

        ((x, y), dir) = current
        energized.add((x, y))

        for ns in next_step(cave, x, y, dir):
            if ns not in visited:
                queue.append(ns)

    return energized


def solution_1(input):
    cave = parse(input)
    energized_cave = beam(cave, (-1, 0), "E")
    return len(energized_cave)-1


def solution_2(input):
    cave = parse(input)
    max_x, max_y = get_grid_dimensions(cave)

    best = 0
    for y in range(max_y):
        best = max(best, len(beam(cave, (-1, y), "E"))-1)
        best = max(best, len(beam(cave, (max_x, y), "W"))-1)
    for x in range(max_x):
        best = max(best, len(beam(cave, (x, -1), "S"))-1)
        best = max(best, len(beam(cave, (x, max_y), "N"))-1)

    return best


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
