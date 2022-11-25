"""Solution module for Day 9, 2015"""
from collections import defaultdict
import copy
from itertools import permutations
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def compute(input):
    places = set()
    graph = defaultdict(dict)

    for line in input:
        source, dest, dist = (line.split()[0], line.split()[2], int(line.split()[4]))
        places.add(source)
        places.add(dest)
        graph[source][dest] = int(dist)
        graph[dest][source] = int(dist)

    distances = list()
    for perm in permutations(places):
        distances.append(sum([graph[s][d] for s, d in zip(perm[:-1], perm[1:])]))

    return distances


def solution_1(input):
    return min(compute(input))


def solution_2(input):
    return max(compute(input))


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
