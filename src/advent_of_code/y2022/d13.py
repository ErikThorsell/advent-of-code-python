"""Solution module for Day 13, 2022"""
import copy
from functools import cmp_to_key
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_separator


# First I implemented a solution with True/False for Part 1, but had to rewrite to use -1/1 in order to utilize
# the cmp_to_key functionality.
def ordered(left, right):

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left < right:
            return -1
        else:
            return 1

    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    for sub_left, sub_right in zip(left, right):
        sub_result = ordered(sub_left, sub_right)
        if sub_result != 0:
            return sub_result

    if len(left) < len(right):
        return -1

    if len(left) > len(right):
        return 1

    return 0


# Guesses for Part 1
# 4842
def solution_1(in_list):

    sum_of_indices = 0

    for pair in range(len(in_list)):
        p1, p2 = map(eval, in_list[pair].split("\n"))
        if ordered(p1, p2) == -1:
            sum_of_indices += pair + 1

    return sum_of_indices


# Guesses for Part 2
# 140  <- ran with test input....
def solution_2(in_list):
    packets = [[[2]], [[6]]]

    for pair in range(len(in_list)):
        p1, p2 = map(eval, in_list[pair].split("\n"))
        packets += [p1, p2]

    sorted_packets = sorted(packets, key=cmp_to_key(ordered))
    return (1 + sorted_packets.index([[2]])) * (1 + sorted_packets.index([[6]]))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_separator(input, "\n\n")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
