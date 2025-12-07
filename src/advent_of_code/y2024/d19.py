"""Solution module for Day 19, 2024"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
    answer = 6
    assert(solution_1(input) == answer)
    

def test_2():
    input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
    answer = 16
    assert(solution_2(input) == answer)


def parse(input):
    towels, patterns = input.split("\n\n")
    towels = towels.strip().split(", ")
    patterns = patterns.split("\n")
    return towels, patterns


def possible(design, towels):
    n = len(design)
    dp = [False]*(n+1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and design[j:i] in towels:
                dp[i] = True
                break

    return dp[n]


def solution_1(input):
    towels, designs = parse(input)
    return sum(possible(design, towels) for design in designs)


def all_ways(design, towels):
    n = len(design)
    dp = [0]*(n+1)
    dp[0] = 1

    towel_lengths = set(len(t) for t in towels)

    for idx in range(1, n+1):
        for length in towel_lengths:
            if length <= idx:
                if design[idx-length:idx] in towels:
                    dp[idx] += dp[idx-length]

    return dp[n]


def solution_2(input):
    towels, designs = parse(input)
    return sum(all_ways(design, towels) for design in designs)


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
