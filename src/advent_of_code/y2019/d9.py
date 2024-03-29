"""Solution module for Day X, YEAR"""
import copy
import time

from advent_of_code.utils.intcode import Intcode
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_separator


def solution_1(input):

    intcode = Intcode(input)
    intcode.run()
    return intcode.memory.values()


def solution_2(input):
    pass


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
