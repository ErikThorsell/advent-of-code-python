"""Solution module for Day X, YEAR"""
from collections import defaultdict
import copy
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):
    grid = defaultdict(int)

    for instr in input:
        action = re.search(r"^[^\d]*", instr).group(0).strip()

        start, end = re.findall(r"\d+,\d+", instr)
        start = (int(start.split(",")[0]), int(start.split(",")[1]))
        end = (int(end.split(",")[0]), int(end.split(",")[1]))

        for y in range(start[0], end[0] + 1):
            for x in range(start[1], end[1] + 1):

                if action == "turn off":
                    grid[(y, x)] = 0
                elif action == "turn on":
                    grid[(y, x)] = 1
                elif action == "toggle":
                    grid[(y, x)] = 1 - grid[(y, x)]

    return sum(grid.values())


def solution_2(input):
    grid = defaultdict(int)

    for instr in input:
        action = re.search(r"^[^\d]*", instr).group(0).strip()

        start, end = re.findall(r"\d+,\d+", instr)
        start = (int(start.split(",")[0]), int(start.split(",")[1]))
        end = (int(end.split(",")[0]), int(end.split(",")[1]))

        for y in range(start[0], end[0] + 1):
            for x in range(start[1], end[1] + 1):

                if action == "turn off":
                    grid[(y, x)] = max(0, grid[(y, x)] - 1)
                elif action == "turn on":
                    grid[(y, x)] += 1
                elif action == "toggle":
                    grid[(y, x)] += 2

    return sum(grid.values())


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
