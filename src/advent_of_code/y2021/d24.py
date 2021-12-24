"""Solution module for Day 24, """
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


# EXTREMELY good explanation -> https://github.com/dphilipson/advent-of-code-2021/blob/master/src/days/day24.rs
def run_alu(constants, minimize=False):
    stack = list()
    constraints = {}
    for i, (check, offset) in enumerate(constants):
        if check > 0:
            stack.append((i, offset))
        else:
            j, offset = stack.pop()
            constraints[i] = (j, offset + check)

    model_number = {}
    for i, (j, value) in constraints.items():
        model_number[i] = max(1, 1 + value) if minimize else min(9, 9 + value)
        model_number[j] = max(1, 1 - value) if minimize else min(9, 9 - value)

    return "".join(str(model_number[x]) for x in range(14))


def solution_1(input):
    rpc = 18  # input cycles every 18th row
    constants = [(int(input[c * rpc + 5][6:]), int(input[c * rpc + 15][6:])) for c in range(14)]
    return run_alu(constants)


def solution_2(input):
    rpc = 18  # input cycles every 18th row
    constants = [(int(input[c * rpc + 5][6:]), int(input[c * rpc + 15][6:])) for c in range(14)]
    return run_alu(constants, minimize=True)


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
