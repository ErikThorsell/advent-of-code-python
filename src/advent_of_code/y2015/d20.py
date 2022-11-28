"""Solution module for Day X, YEAR"""
from collections import defaultdict
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def compute(goal, num_pkgs=10, limit=None):
    houses = defaultdict(int)

    for elf in range(1, goal // 10):
        for house in range(elf, goal // 10, elf):
            if limit and house >= elf * limit:
                break
            houses[house] += elf * num_pkgs

    min_house = maxsize
    for h in houses:
        if houses[h] >= goal and h < min_house:
            min_house = h

    return min_house


def solution_1(input):
    return compute(input[0])


def solution_2(input):
    return compute(input[0], 11, 50)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
