"""Solution module for Day 6, 2022"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline
from advent_of_code.y2019.d8 import chunks


def compute(buffer, offset):
    for idx in range(len(buffer)):
        window = buffer[idx : idx + offset]
        if len(set(window)) == len(window):
            return idx + offset


def solution_1(input):
    return compute(input, 4)


def solution_2(input):
    return compute(input, 14)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)[0]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
