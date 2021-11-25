"""Solution module for Day X, YEAR"""
from collections import Counter
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline
from advent_of_code.utils.strings import hamming_distance


def solution_1(input):
    has_two = 0
    has_three = 0
    for i in input:
        counted = Counter(i)
        if 2 in counted.values():
            has_two += 1
        if 3 in counted.values():
            has_three += 1
    return has_two * has_three


def solution_2(input):
    for i1, s1 in enumerate(input):
        for i2, s2 in enumerate(input):
            if i1 == i2:
                continue
            if hamming_distance(s1, s2) == 1:
                return "".join([c for i, c in enumerate(s1) if c == s2[i]])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
