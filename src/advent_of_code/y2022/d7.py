"""Solution module for Day X, YEAR"""
from collections import defaultdict
import copy
from itertools import accumulate
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    dirs = defaultdict(int)

    for line in input:
        match line.split():
            case "$", "cd", "/":
                current_directory = [""]
            case "$", "cd", "..":
                current_directory.pop()
            case "$", "cd", directory:
                current_directory.append(directory)
            case "$", "ls":
                pass
            case "dir", size:
                pass
            case size, file:
                for p_sum in accumulate(current_directory):
                    dirs[p_sum] += int(size)

    return dirs


def solution_1(input):
    dirs = parse(input)

    sum = 0
    for s in dirs.values():
        if s <= 100000:
            sum += s

    return sum


def solution_2(input):
    dirs = parse(input)

    min_dir = maxsize
    for s in dirs.values():
        if s >= dirs[""] - 40000000:
            min_dir = min(min_dir, s)

    return min_dir


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
