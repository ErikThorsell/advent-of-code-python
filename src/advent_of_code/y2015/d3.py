"""Solution module for Day X, YEAR"""
import copy
from collections import defaultdict
import time

from advent_of_code.utils.fetch import fetch


def solution_1(input):
    c = (0, 0)
    houses = defaultdict(int)
    houses[c] += 1

    for d in input:
        match d:
            case "^":
                c = (c[0] - 1, c[1])
            case "v":
                c = (c[0] + 1, c[1])
            case "<":
                c = (c[0], c[1] - 1)
            case ">":
                c = (c[0], c[1] + 1)
            case _:
                print(d)

        houses[c] += 1

    return len(houses)


def solution_2(input):
    s = (0, 0)
    rs = (0, 0)
    houses = defaultdict(int)
    houses[s] += 1
    houses[rs] += 1

    s_instr = input[0::2]
    rs_instr = input[1::2]

    for d in s_instr:
        match d:
            case "^":
                s = (s[0] - 1, s[1])
            case "v":
                s = (s[0] + 1, s[1])
            case "<":
                s = (s[0], s[1] - 1)
            case ">":
                s = (s[0], s[1] + 1)
            case _:
                print(d)

        houses[s] += 1

    for d in rs_instr:
        match d:
            case "^":
                rs = (rs[0] - 1, rs[1])
            case "v":
                rs = (rs[0] + 1, rs[1])
            case "<":
                rs = (rs[0], rs[1] - 1)
            case ">":
                rs = (rs[0], rs[1] + 1)
            case _:
                print(d)

        houses[rs] += 1

    return len(houses)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
