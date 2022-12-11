"""Solution module for Day X, YEAR"""
import copy
import time
from typing import Dict, List, Tuple
from advent_of_code.utils.coordinates import get_coordinates_between

from advent_of_code.utils.coordinates import line_is_diagonal
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_line_segments


def compute_coverage(
    line_segments: List[Tuple[int, int]]
) -> Dict[Tuple[int, int], int]:
    coverage = dict()
    for line in line_segments:
        for c in get_coordinates_between(line[0], line[1]):
            if c not in coverage:
                coverage[c] = 1
            else:
                coverage[c] += 1
    return coverage


def get_no_overlapping_coordinates(coverage: Dict[Tuple[int, int], int]):
    overlaps = 0
    for c in coverage:
        if coverage[c] > 1:
            overlaps += 1
    return overlaps


def solution_1(input):
    line_segments = [(c1, c2) for (c1, c2) in input if not line_is_diagonal(c1, c2)]
    coverage = compute_coverage(line_segments)
    return get_no_overlapping_coordinates(coverage)


def solution_2(input):
    coverage = compute_coverage(input)
    return get_no_overlapping_coordinates(coverage)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_line_segments(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
