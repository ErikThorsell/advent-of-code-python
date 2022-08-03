"""Solution module for Day 5, 2019"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.intcode import Intcode
from advent_of_code.utils.parse import split_number_by_separator


def solution(input):
    intcode = Intcode(input)
    intcode.run()


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_separator(input, ",")

    tic = time.perf_counter()
    s1 = solution(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem: {s1}, acquired in: {toc-tic:0.4f} seconds")
