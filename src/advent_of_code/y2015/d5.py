"""Solution module for Day X, YEAR"""
from collections import deque
import copy
from itertools import islice, zip_longest
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def solution_1(input):
    nice = []
    good = True
    for s in input:

        # ab, cd, pq, xy are not part of the string
        illegal = ["ab", "cd", "pq", "xy"]
        groups = list(sliding_window(s, 2))
        for g in groups:
            if "".join(g) in illegal:
                good = False

        # Three or more vowels
        if sum([s.count(v) for v in "aoeui"]) < 3:
            good = False

        # At least one letter appears twice in a row
        dup = False
        for i, c in enumerate(s):
            if i == len(s) - 1:
                break
            if s[i] == s[i + 1]:
                dup = True

        if not dup:
            good = False

        if good:
            nice.append(s)

        good = True

    return len(nice)


def solution_2(input):
    nice = []
    for s in input:

        # Contains the same pair twice
        pairs = list(sliding_window(s, 2))
        if not any(s.count("".join(p)) > 1 for p in pairs):
            continue

        # Contains pattern xyx
        triplets = list(sliding_window(s, 3))
        if not any(t[0] == t[-1] for t in triplets):
            continue

        nice.append(s)

    return len(nice)


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
