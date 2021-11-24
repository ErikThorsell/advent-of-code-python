"""Solution module for Day 1, 2019 """
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def calc(mass: int) -> int:
    return mass // 3 - 2


def solution_1(input):
    return sum([calc(i) for i in input])


def solution_2(input):
    sum = 0
    for i in input:
        mass = calc(i)
        while mass > 0:
            sum += mass
            mass = calc(mass)
    return sum


def run(year: int, day: int):
    print(f"🌟 Fetching input for {year}/{day} 🌟")

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
