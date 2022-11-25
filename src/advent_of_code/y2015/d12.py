"""Solution module for Day 12, 2015"""
import copy
import json
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def solution_1(input):
    return sum([int(d) for d in re.findall(r"-?\d+", input)])


def dive(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([dive(i) for i in j])
    if type(j) != dict:
        return 0
    if "red" in j.values():
        return 0

    return dive(list(j.values()))


def solution_2(input):
    content = json.loads(input)
    return dive(content)


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
