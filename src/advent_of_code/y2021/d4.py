"""Solution module for Day X, YEAR"""
import copy
from typing import List
import time

import numpy as np

from advent_of_code.utils.bingo import play_one_number, has_bingo, sum_unmatched
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_bingo


def solution_1(order: List[int], boards) -> int:
    matches = [np.zeros((5, 5)) for _ in range(len(boards))]
    for number in order:
        matches = play_one_number(boards, matches, number)
        for mx, match in enumerate(matches):
            if has_bingo(match):
                sum_u = sum_unmatched(boards[mx], match)
                return sum_u * number


def solution_2(order, boards):
    matches = [np.zeros((5, 5)) for _ in range(len(boards))]
    bingos = [False for _ in range(len(boards))]
    for number in order:
        matches = play_one_number(boards, matches, number)
        for mx, match in enumerate(matches):
            if has_bingo(match):
                bingos[mx] = True
                if all(bingos):
                    sum_u = sum_unmatched(boards[mx], match)
                    return sum_u * number


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    order, boards = parse_bingo(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(order), copy.deepcopy(boards))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(order), copy.deepcopy(boards))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
