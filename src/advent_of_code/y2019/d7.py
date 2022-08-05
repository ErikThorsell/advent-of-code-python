"""Solution module for Day X, YEAR"""
import copy
from itertools import permutations
from sys import maxsize
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.intcode import Intcode
from advent_of_code.utils.parse import split_number_by_separator


def solution_1(input):
    max_res = -maxsize
    res = []
    prev_in = 0

    input_copy = copy.deepcopy(input)
    for seq in list(permutations(range(5))):
        res = []
        prev_in = 0

        for i in seq:
            intcode = Intcode(input, [i, prev_in])
            intcode.run()
            out = intcode.output
            res.append(out)
            prev_in = res[-1]
            input = copy.deepcopy(input_copy)

        sub_res = res[-1]
        if sub_res > max_res:
            print(f"Sequence: {seq} yielded a better result: {sub_res}")
            max_res = sub_res

    return max_res


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
