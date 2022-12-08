"""Solution module for Day 8, 2022"""
import copy
from math import prod
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import get_rays_from_inside
from advent_of_code.utils.parse import parse_grid


def solution_1(input):
    visible = 0

    for rx, row in enumerate(input):
        for cx, col in enumerate(row):

            # All trees on the edge are visible
            if rx == 0 or cx == 0 or rx == len(input)-1 or cx == len(row)-1:
                visible += 1
                continue

            # Look at surrounding trees
            rays = get_rays_from_inside(input, rx, cx)
            for trees in rays:
                if all(t < col for t in trees):
                    visible += 1
                    break  # doesn't matter if the tree is visible from multiple angles
    
    return visible


def solution_2(input):
    max_scenic_score = 0

    for rx, row in enumerate(input):
        for cx, col in enumerate(row):

            rays = get_rays_from_inside(input, rx, cx)
            viewing_distances = list()

            for trees in rays:
                vd = 0
                for idx, t in enumerate(trees):
                    if t < col:
                        vd += 1
                    else:
                        vd += 1  # include the tree that caused us to stop
                        break
                viewing_distances.append(vd)
            
            max_scenic_score = max(max_scenic_score, prod(viewing_distances))
    
    return max_scenic_score


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_grid(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
