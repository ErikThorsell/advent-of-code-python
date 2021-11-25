"""Solution module for Day X, YEAR"""
from collections import defaultdict
from typing import Dict, List, Tuple
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_fabric_claims


def compute_rectangle(claim: Tuple[int, int, int, int]) -> List[Tuple[int, int]]:
    lm = claim[0]
    tm = claim[1]
    w = claim[2]
    h = claim[3]
    coverage = list()
    for x in range(lm, lm + w):
        for y in range(tm, tm + h):
            coverage.append((x, y))
    return coverage


def compute_coverage(
    claims: Dict[int, Tuple[int, int, int, int]]
) -> Dict[Tuple[int, int], List[int]]:

    coverage = defaultdict(list)
    for claim in claims:
        rectangle = compute_rectangle(claims[claim])
        for c in rectangle:
            coverage[c].append(claim)
    return coverage


def solution_1(input):
    coverage = compute_coverage(input)
    return len([o for o in coverage if len(coverage[o]) > 1])


def solution_2(input):
    coverage = compute_coverage(input)
    candidates = list(input.keys())
    for c in coverage:
        if len(coverage[c]) > 1:
            for id in coverage[c]:
                if id in candidates:
                    candidates.remove(id)
    return candidates[0]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_fabric_claims(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
