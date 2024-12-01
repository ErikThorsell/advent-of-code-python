"""Solution module for Day 1, 2024"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    # Copy paste example here
    input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    answer = 11
    assert(solution_1(input) == answer)
    

def test_2():
    input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    answer = 31
    assert(solution_2(input) == answer)


def parse(input):
    l1, l2 = [], []

    for row in input.split("\n"):
        l, r = map(int, row.split())
        l1.append(l)
        l2.append(r)

    return l1, l2


def solution_1(input):

    l1, l2 = parse(input)

    l1.sort()
    l2.sort()

    diff = 0
    for i in range(len(l1)):
        diff += abs(l1[i]-l2[i])

    return diff


def solution_2(input):
    l1, l2 = parse(input)

    sim = 0
    for d in l1:
        sim += d * l2.count(d)

    return sim


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
