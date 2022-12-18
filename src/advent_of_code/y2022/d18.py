"""Solution module for Day 18, 2022"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    cubes = set()
    for cube in input:
        cubes.add(tuple(map(int, [c.strip() for c in cube.split(",")])))
    return cubes


def adj_cubes(cube):
    x, y, z = cube
    return (
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    )


def solution_1(input):
    cubes = parse(input)

    area = 0
    for cube in cubes:
        for adj_c in adj_cubes(cube):
            if adj_c not in cubes:
                area += 1

    return area


def solution_2(input):
    cubes = parse(input)

    min_x, min_y, min_z = min(c[0] for c in cubes), min(c[1] for c in cubes), min(c[2] for c in cubes)
    max_x, max_y, max_z = max(c[0] for c in cubes), max(c[1] for c in cubes), max(c[2] for c in cubes)
    x_range = range(min_x, max_x + 1)
    y_range = range(min_y, max_y + 1)
    z_range = range(min_z, max_z + 1)

    surface = set()

    def is_surface(cube):
        visited = set()
        stack = [cube]

        while stack:
            cube = stack.pop()

            if cube in visited:
                continue

            visited.add(cube)

            if cube in surface or not (cube[0] in x_range and cube[1] in y_range and cube[2] in z_range):
                surface.update(visited.difference(cubes))
                return True

            if cube not in cubes:
                stack.extend(adj_cubes(cube))

        return False

    area = 0
    for cube in cubes:
        for adj_c in adj_cubes(cube):
            if is_surface(adj_c):
                area += 1

    return area


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
