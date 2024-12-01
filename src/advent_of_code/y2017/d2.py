"""Solution module for Day 2, 2017"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """5 1 9 5
7 5 3
2 4 6 8"""
    answer = 18
    assert(solution_1(input) == answer)
    

def test_2():
    input = """5 9 2 8
9 4 7 3
3 8 6 5"""
    answer = 9
    assert(solution_2(input) == answer)

def parse(input):
    data = list()
    for row in input.split("\n"):
        data.append(tuple(map(int, row.split())))
    return data


def solution_1(input):
    data = parse(input)
    tot = 0
    for row in data:
        tot += max(row)-min(row)
    return tot


def solution_2(input):
    data = parse(input)
    tot = 0
    for row in data:
        for i1, d1 in enumerate(row):
            for i2, d2 in enumerate(row):
                if i1 != i2:
                    if d1 % d2 == 0:
                        tot += d1//d2

    return tot


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
