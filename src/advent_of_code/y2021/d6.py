"""Solution module for Day 6, 2021"""
from collections import defaultdict
import copy
import time
from typing import Counter, List


from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_separator


def run_fishyplier(input: List[int], iterations: int) -> int:
    fishes = defaultdict(lambda: 0)
    for fish in input:
        fishes[fish] += 1

    for _ in range(iterations):
        temp_fishes = defaultdict(lambda: 0)
        for fish, count in fishes.items():
            upd_fish = fish - 1
            if upd_fish < 0:
                temp_fishes[8] += count
                upd_fish = 6

            temp_fishes[upd_fish] += count
            fishes = temp_fishes

    return sum(fishes.values())


def solution_1(input):
    return run_fishyplier(input, 80)


def solution_2(input):
    return run_fishyplier(input, 256)


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
