"""Solution module for Day 1, 2021"""
import copy
import time

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def solution_1(input):
    prev_depth = 0
    num_inc = 0
    for v1 in input:
        if v1 > prev_depth:
            num_inc += 1
        prev_depth = v1
    return num_inc - 1


def solution_2(input):
    sliding_window = np.convolve(input, np.ones(3, dtype=int), "valid")
    prev_depth = 0
    num_inc = 0
    for v1 in sliding_window:
        if v1 > prev_depth:
            num_inc += 1
        prev_depth = v1
    return num_inc - 1


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
