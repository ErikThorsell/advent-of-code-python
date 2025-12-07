"""Solution module for Day $day, $year"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """"""
    expected_answer = 0
    actual_answer = solution_1(input)
    assert expected_answer == actual_answer, (f"Expected: {expected_answer}, got {actual_answer}")

def test_2():
    input = """"""
    expected_answer = 0
    actual_answer = solution_2(input)
    assert expected_answer == actual_answer, (f"Expected: {expected_answer}, got {actual_answer}")


def parse(input):
    ...


def solution_1(input):
    return 0


def solution_2(input):
    return 0


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

