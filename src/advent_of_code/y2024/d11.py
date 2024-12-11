"""Solution module for Day 11, 2024"""
from collections import defaultdict
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """125 17"""
    answer = 55312
    assert(solution_1(input) == answer)
    

def solution_1(input):
    line = list(map(int, input.split()))

    for _ in range(25):
        new_line = []
        for stone in line:
            if stone == 0:
                new_line.append(1)
            elif len(str(stone)) % 2 == 0:
                middle = len(str(stone))//2
                l = int(str(stone)[:middle])
                r = int(str(stone)[middle:])
                new_line.append(l)
                new_line.append(r)
            else:
                new_line.append(stone*2024)

        line = new_line

    return len(line)


def solution_2(input):
    d = defaultdict(int)
    for stone in (map(int, input.split())):
        d[stone] += 1

    for _ in range(75):
        nd = defaultdict(int)
        for stone in d:
            if stone == 0:
                nd[1] += d[stone]
            elif len(str(stone)) % 2 == 0:
                middle = len(str(stone))//2
                l = int(str(stone)[:middle])
                r = int(str(stone)[middle:])
                nd[l] += d[stone]
                nd[r] += d[stone]
            else:
                nd[stone*2024] += d[stone]

        d = nd
    
    return sum(v for _, v in d.items())


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
