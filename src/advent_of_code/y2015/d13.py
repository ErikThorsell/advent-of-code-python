"""Solution module for Day 13, 2015"""
import copy
from collections import deque, defaultdict
from itertools import permutations
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(preferences):
    prefs = defaultdict(dict)

    for line in preferences:
        p1 = line.split()[0]
        d = line.split()[2]
        a = int(line.split()[3]) if d == "gain" else int(line.split()[3]) * -1
        p2 = line.split()[-1][:-1]
        prefs[p1][p2] = a

    return prefs


def compute(prefs, seating):
    happiness = 0
    for idx, p in enumerate(seating):
        hl = prefs[p][seating[(idx - 1) % len(seating)]]
        hr = prefs[p][seating[(idx + 1) % len(seating)]]
        happiness += hl + hr
    return happiness


def solution_1(input):
    prefs = parse(input)

    persons = prefs.keys()
    perms = permutations(persons)

    happiest = 0
    for p in perms:
        happiest = max(happiest, compute(prefs, p))

    return happiest


def solution_2(input):
    prefs = parse(input)

    # have to wrap in list to get a list and not a reference to the dict keys
    for p in list(prefs.keys()):
        prefs["Erik"][p] = 0
        prefs[p]["Erik"] = 0

    perms = permutations(prefs.keys())

    happiest = 0
    for p in perms:
        happiest = max(happiest, compute(prefs, p))

    return happiest


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
