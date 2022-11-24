"""Solution module for Day X, YEAR"""
import copy
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):
    area = 0
    for box in input:
        l, w, h = map(int, re.findall(r"\d+", box))
        area += 2 * l * w + 2 * w * h + 2 * h * l
        area += min([l * w, w * h, h * l])
    return area


def solution_2(input):
    ribbon = 0
    for box in input:
        l, w, h = map(int, re.findall(r"\d+", box))
        smallest_faces = sorted((l, w, h))[:2]
        perimeter = 2 * smallest_faces[0] + 2 * smallest_faces[1]
        ribbon += perimeter + l * w * h
    return ribbon


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
