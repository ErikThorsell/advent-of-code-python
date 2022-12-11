"""Solution module for Day 15, 2015"""
from collections import defaultdict
import copy
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    ingr = dict()
    for line in input:
        [(n, c, d, f, t, cal)] = re.findall(
            r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
            line,
        )
        ingr[n] = list(map(int, [c, d, f, t, cal]))
    return ingr


def compute(ingr, cal_lim=None):
    max_score = 0
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                l = 100 - i - j - k
                capacity = (
                    ingr["Frosting"][0] * i
                    + ingr["Candy"][0] * j
                    + ingr["Butterscotch"][0] * k
                    + ingr["Sugar"][0] * l
                )
                durability = (
                    ingr["Frosting"][1] * i
                    + ingr["Candy"][1] * j
                    + ingr["Butterscotch"][1] * k
                    + ingr["Sugar"][1] * l
                )
                flavor = (
                    ingr["Frosting"][2] * i
                    + ingr["Candy"][2] * j
                    + ingr["Butterscotch"][2] * k
                    + ingr["Sugar"][2] * l
                )
                texture = (
                    ingr["Frosting"][3] * i
                    + ingr["Candy"][3] * j
                    + ingr["Butterscotch"][3] * k
                    + ingr["Sugar"][3] * l
                )
                calories = (
                    ingr["Frosting"][4] * i
                    + ingr["Candy"][4] * j
                    + ingr["Butterscotch"][4] * k
                    + ingr["Sugar"][4] * l
                )

                if cal_lim and calories > cal_lim:
                    continue

                score = (
                    max(0, capacity)
                    * max(0, durability)
                    * max(0, flavor)
                    * max(0, texture)
                )
                if score > max_score:
                    max_score = score

    return max_score


def solution_1(input):
    ingr = parse(input)
    return compute(ingr)


def solution_2(input):
    ingr = parse(input)
    return compute(ingr, 500)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
