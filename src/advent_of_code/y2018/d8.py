"""Solution module for Day X, YEAR"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_separator


def compute_tree(input):
    n_children, n_metadata = input[:2]
    input = input[2:]
    child_metadata = []
    sum_metadata = 0

    for _ in range(n_children):
        total, value, input = compute_tree(input)
        sum_metadata += total
        child_metadata.append(value)

    sum_metadata += sum(input[:n_metadata])

    if n_children == 0:
        return (sum_metadata, sum(input[:n_metadata]), input[n_metadata:])

    return (
        sum_metadata,
        sum(
            child_metadata[k - 1]
            for k in input[:n_metadata]
            if k > 0 and k <= len(child_metadata)
        ),
        input[n_metadata:],
    )


def solution_1(input):
    total, _, _ = compute_tree(input)
    return total


def solution_2(input):
    _, value, _ = compute_tree(input)
    return value


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_separator(input, " ")

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
