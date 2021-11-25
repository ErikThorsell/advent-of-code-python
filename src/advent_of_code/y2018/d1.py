"""Solution module for Day X, YEAR"""
from itertools import cycle
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def solution_1(input):
    frequency = 0
    for i in input:
        frequency += i
    return frequency


def solution_2(input):
    freqs = {0: 1}
    frequency = 0
    for i in cycle(input):
        frequency += i
        if frequency in freqs:
            return frequency
        else:
            freqs[frequency] = 1


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
