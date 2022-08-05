"""Solution module for Day 5, 2019"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.intcode import Intcode
from advent_of_code.utils.parse import split_number_by_separator


def solution_1(input):
    """
    Day 5 part 1 uses the load() operation several times before ultimately terminating on opcode 99.
    Day 7 requires that one loops several times and return on both opcode 99 and opcode 4 (load).
    Since I ultimately want _all_ days to work, I went back and modified Day 5 s.t. I could use the same Intcode class
    for both days.

    Day 5 part 2 does not have the same problem.
    """
    op = 0
    intcode = Intcode(input, 1)
    while op != 99:
        (_, op) = intcode.run()
    return intcode.output


def solution_2(input):
    intcode = Intcode(input, 5)
    (res, _) = intcode.run()
    return res


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
