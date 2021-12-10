"""Solution module for Day 10, 2021"""
from collections import deque
import copy
import math
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):
    c_map = {"{": "}", "[": "]", "(": ")", "<": ">"}
    s_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

    incomplete = []
    score = 0

    for row in input:
        broken = False
        stack = deque()
        for c in row:
            if c in c_map:
                stack.append(c)
            else:
                m = stack.pop()
                if c != c_map[m]:
                    score += s_map[c]
                    broken = True
                    break
        if not broken:
            incomplete.append(row)

    return score, incomplete


def solution_2(input):
    c_map = {"{": "}", "[": "]", "(": ")", "<": ">"}
    s_map = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []

    for row in input:
        stack = deque()
        for c in row:
            if c in c_map:
                stack.append(c)
            else:
                m = stack.pop()

        score = 0
        while stack:
            cs = s_map[c_map[stack.pop()]]
            score = score * 5 + cs
        scores.append(score)

    scores.sort()
    return scores[int(len(scores) / 2)]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1, p2 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(p2)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
