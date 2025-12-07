"""Solution module for Day 1, 2025"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    answer = 3
    assert(solution_1(input) == answer)

def test_2():
    input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    answer = 6
    assert(solution_2(input) == answer)


def solution_1(input):

    count = 0
    pos = 50

    for line in input.split("\n"):
        rot, dist = line[0], int(line[1:])

        if rot == "L":
            pos -= dist
        elif rot == "R":
            pos += dist
        else:
            raise

        pos = pos % 100

        if pos == 0:
            count += 1

    return count


def solution_2(input):

    count = 0
    pos = 50

    for line in input.split("\n"):
        rot, dist = line[0], int(line[1:])

        if rot == "L":
            for p in range(pos, pos-dist+1, -1):
                p = p % 100
                if p == 0:
                    count += 1
            pos = p

        elif rot == "R":
            for p in range(pos, pos+dist):
                p = p % 100
                if p == 0:
                    count += 1
            pos = p

        else:
            raise

    return count


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
