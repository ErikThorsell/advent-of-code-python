"""Solution module for Day 16, 2021"""
import copy
import time

from advent_of_code.utils.bits import compute_bits, hex_to_bin
import advent_of_code.utils.globals
from advent_of_code.utils.fetch import fetch


def solution(input):
    binary = hex_to_bin(input)
    advent_of_code.utils.globals.init()
    val, _ = compute_bits(binary)
    return advent_of_code.utils.globals.d16_version_sum, val


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1, s2 = solution(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1} and problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
