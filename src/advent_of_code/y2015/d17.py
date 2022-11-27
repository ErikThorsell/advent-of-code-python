"""Solution module for Day X, YEAR"""
from itertools import combinations
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def solution_1(input):
    total = 0

    for b in range(len(input)):
        for combination in combinations(input, b):
            if sum(combination) == 150:
                total += 1

    return total


def solution_2(input):
    for b in range(len(input)):
        total = 0
        for combination in combinations(input, b):
            if sum(combination) == 150:
                total += 1

        if total > 0:
            return total


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
