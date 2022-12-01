"""Solution module for Day 1, 2022"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_separator


def solution_1(input):
    max_cal = 0
    for e in input:
        max_cal = max((sum(map(int, e.split()))), max_cal)
    return max_cal


def solution_2(input):
    elfs = list()
    for e in input:
        elfs.append(sum(map(int, e.split())))
    return sum(sorted(elfs, reverse=True)[:3])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_separator(input, "\n\n")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
