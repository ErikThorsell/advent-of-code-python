"""Solution module for Day 2, 2025"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    answer = 1227775554
    assert(solution_1(input) == answer)

def test_2():
    input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    answer = 4174379265
    assert(solution_2(input) == answer)


def solution_1(input):

    aggr = 0

    for id_range in input.split(","):
        lid, rid = map(int, id_range.split("-"))

        for id in range(lid, rid+1):
            id = str(id)
            first = id[:len(id)//2]
            second = id[len(id)//2:]

            if first == second:
                aggr += int(id)

    return aggr


# Naive approach
def solution_2_naive(input):

    aggr = 0

    for id_range in input.split(","):
        lid, rid = map(int, id_range.split("-"))

        for id in range(lid, rid+1):
            id = str(id)
            n = len(id)

            invalid = False

            for k in range(1, n+1):
                if n % k != 0:
                    continue

                chunks = [id[i:i+k] for i in range(0, n, k)]

                if len(set(chunks)) == 1 and len(chunks) >= 2:
                    # We found at least one invalid chunkisation of the ID - abort and move on
                    invalid = True
                    break

            if invalid:
                aggr += int(id)

    return aggr


# Fast approach
def solution_2(input):

    aggr = 0

    for id_range in input.split(","):
        lid, rid = map(int, id_range.split("-"))

        for num in range(lid, rid+1):
            s = str(num)
            # If s is made by repeating a smaller substring, then
            # it will appear somewhere inside (s+s)[1:-1]
            if (s+s).find(s, 1, -1) != -1:
                aggr += num

    return aggr


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
