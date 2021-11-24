"""Solution module for Day X, YEAR"""
import copy
from itertools import groupby
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import (
    split_number_by_separator,
)


def solution_1(low, high: int) -> int:

    matches = 0
    for num in range(low, high + 1):

        s_num = str(num)

        if s_num != "".join(sorted(s_num)):
            continue

        groups = ["".join(g) for _, g in groupby(s_num)]
        if any([g for g in groups if len(g) >= 2]):
            matches += 1

    return matches


def solution_2(low, high):

    matches = 0
    for num in range(low, high + 1):

        s_num = str(num)

        if s_num != "".join(sorted(s_num)):
            continue

        groups = ["".join(g) for _, g in groupby(s_num)]
        if any([g for g in groups if len(g) == 2]):
            matches += 1

    return matches


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_separator(input, "-")

    tic = time.perf_counter()
    s1 = solution_1(parsed_input[0], parsed_input[1])
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input[0], parsed_input[1])
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
