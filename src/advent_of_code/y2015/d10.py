"""Solution module for Day X, YEAR"""
import copy
from itertools import groupby
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def compute(phrase, iterations):
    for _ in range(iterations):
        phrases = [list(g) for k, g in groupby(phrase)]
        output = ""
        for p in phrases:
            output += str(len(p)) + p[0]

        phrase = output

    return len(phrase)


def solution_1(input):
    return compute(input, 40)


def solution_2(input):
    return compute(input, 50)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
