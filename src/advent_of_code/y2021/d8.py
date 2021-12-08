"""Solution module for Day X, YEAR"""
import copy
from collections import defaultdict
from itertools import permutations
import time
from sys import maxsize
from typing import Dict, List

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_seven_segment, split_number_by_newline


def determine_digit_by_length(signal: str) -> int:
    if len(signal) == 2:
        return 1
    if len(signal) == 3:
        return 7
    if len(signal) == 4:
        return 4
    if len(signal) == 7:
        return 8
    return -1


def solution_1(input):
    occ = defaultdict(lambda: 0)
    for _, output in input:
        for digit in output.split():
            occ[determine_digit_by_length(digit)] += 1
    return occ[1] + occ[4] + occ[7] + occ[8]


def solution_2(input):
    pass


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_seven_segment(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
