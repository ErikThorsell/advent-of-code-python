"""Solution module for Day X, YEAR"""
import copy
import time

from advent_of_code.utils.fetch import fetch


def reduce_polymer(polymer: str) -> str:
    buffer = list()
    for c in polymer:
        if buffer and react(c, buffer[-1]):
            buffer.pop()
        else:
            buffer.append(c)
    return buffer


def react(c1, c2: str) -> bool:
    return abs(ord(c1) - ord(c2)) == 32


def solution_1(input):
    reduced_polymer = reduce_polymer(input)
    return len(reduced_polymer)


def solution_2(input):
    potential_badies = list(set(input))
    shortest_polymer = 999999
    for pb in potential_badies:
        candidate_input = input.replace(pb.lower(), "")
        candidate_input = candidate_input.replace(pb.upper(), "")
        if (
            candidate_reduction := len(reduce_polymer(candidate_input))
        ) < shortest_polymer:
            shortest_polymer = candidate_reduction
    return shortest_polymer


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
