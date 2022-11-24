"""Solution module for Day X, YEAR"""
import copy
from hashlib import md5
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def solution_1(input):
    for i in range(int(10e6)):
        rstr = f"{input}" + str(i)
        hash_str = md5(rstr.encode("utf-8")).hexdigest()
        if hash_str.startswith("00000"):
            return i


def solution_2(input):
    for i in range(int(10e6)):
        rstr = f"{input}" + str(i)
        hash_str = md5(rstr.encode("utf-8")).hexdigest()
        if hash_str.startswith("000000"):
            return i


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
