"""Solution module for Day 1, 2017"""
import copy
from itertools import cycle
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """91212129"""
    answer = 9
    assert(solution_1(input) == answer)
    

def test_2():
    input = """12131415"""
    answer = 4
    assert(solution_2(input) == answer)


def solution_1(input):
    data = cycle(input)

    prev = None
    curr = None
    matches = []

    for _ in range(len(input)+1):
        curr = next(data)
        if curr == prev:
            matches.append(int(curr))
        prev = curr

    return sum(matches)


def solution_2(input):
    data = list(map(int, input))

    matches = []

    for i in range(len(data)):
        if data[i] == data[(i+len(data)//2)%len(data)]:
            matches.append(data[i])

    return sum(matches)


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
