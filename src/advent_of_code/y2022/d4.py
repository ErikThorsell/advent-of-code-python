"""Solution module for Day 4, 2022"""
import copy
import re
import time

from advent_of_code.utils.fetch import fetch


def solution_1(input):
    fully_contained = 0
    for (d1, d2), (d3, d4) in input:

        a1 = set(range(d1, d2 + 1))
        a2 = set(range(d3, d4 + 1))

        if a1.issubset(a2) or a2.issubset(a1):
            fully_contained += 1

    return fully_contained


def solution_2(input):
    overlap = 0
    for (d1, d2), (d3, d4) in input:

        a1 = set(range(d1, d2 + 1))
        a2 = set(range(d3, d4 + 1))

        if len(a1.intersection(a2)) > 0:
            overlap += 1

    return overlap


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = list()
    for row in input.split("\n"):
        d1, d2, d3, d4 = map(int, re.findall(r"\d+", row))
        parsed_input.append(((d1, d2), (d3, d4)))

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
