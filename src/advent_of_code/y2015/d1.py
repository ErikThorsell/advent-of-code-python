"""Solution module for Day 1, 2015"""
import copy
import time

from advent_of_code.utils.fetch import fetch


def solution_1(input):
    floor = 0
    for p in input:
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1
    return floor


def solution_2(input):
    floor = 0
    for idx, p in enumerate(input):
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1

        if floor == -1:
            return idx + 1


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
