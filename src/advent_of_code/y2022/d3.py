"""Solution module for Day 3, 2022"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.strings import chunks
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def compute_score(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96


def solution_1(input):
    score = 0
    for r in input:
        c1, c2 = r[0 : len(r) // 2], r[len(r) // 2 : len(r)]
        common = list(set(c1) & set(c2))
        score += compute_score(common[0])
    return score


def solution_2(input):
    score = 0
    for g1, g2, g3 in chunks(input, 3):
        common = list(set(g1) & set(g2) & set(g3))
        score += compute_score(common[0])
    return score


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
