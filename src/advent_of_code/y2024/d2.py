"""Solution module for Day 2, 2024"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    answer = 2
    assert(solution_1(input) == answer)
    

def test_2():
    input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    answer = 4
    assert(solution_2(input) == answer)


def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if all(1 <= diff <= 3 for diff in diffs):
        return True
    elif all(-3 <= diff <= -1 for diff in diffs):
        return True

    return False


def is_safe_damp(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True

    return False


def solution_1(input):
    count = 0
    for report in input.split("\n"):
        report = list(map(int, report.split()))
        if is_safe(report):
            count +=1
    return count


def solution_2(input):
    count = 0
    for report in input.split("\n"):
        report = list(map(int, report.split()))
        if is_safe_damp(report):
            count +=1
    return count


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
