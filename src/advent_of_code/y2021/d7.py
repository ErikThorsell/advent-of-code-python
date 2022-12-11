"""Solution module for Day 7, 2021"""
import copy
import time
from typing import List
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_separator


def compute_min_pos_cost(crabs: List[int], natural_method: bool = False):
    def cost(crab, pos: int, natural_method: bool) -> int:
        return (
            abs(crab - pos) * abs((crab - pos) + 1) // 2
            if natural_method
            else abs(crab - pos)
        )

    return min(
        sum(cost(crab, pos, natural_method) for crab in crabs)
        for pos in range(min(crabs), max(crabs) + 1)
    )


def solution_1(input):
    return compute_min_pos_cost(input)


def solution_2(input):
    return compute_min_pos_cost(input, natural_method=True)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_separator(input, ",")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
