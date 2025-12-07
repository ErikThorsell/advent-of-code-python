"""Solution module for Day 5, 2025"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    answer = 3
    assert(solution_1(input) == answer)

def test_2():
    input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    answer = 14
    assert(solution_2(input) == answer)


def solution_1(input):
    ranges_str, ingredients_str = input.split("\n\n")

    ranges = []
    for line in ranges_str.split("\n"):
        lr, rr = map(int, line.split("-"))
        ranges.append((lr, rr))

    num_fresh = 0

    for line in ingredients_str.split("\n"):
        x = int(line)

        for lr, rr in ranges:
            if lr <= x <= rr:
                num_fresh += 1
                break  # don’t count it twice

    return num_fresh


def solution_2(input):
    ranges_str, _ = input.split("\n\n")

    intervals = []
    for line in ranges_str.split("\n"):
        lr, rr = map(int, line.split("-"))
        intervals.append((lr, rr))

    intervals.sort()

    merged = []
    for lr, rr in intervals:
        if not merged or lr > merged[-1][1] + 1:
            merged.append([lr, rr])
        else:
            merged[-1][1] = max(merged[-1][1], rr)

    return sum(rr - lr + 1 for lr, rr in merged)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    test_2()
    print("Test 2 was successful!")
    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
