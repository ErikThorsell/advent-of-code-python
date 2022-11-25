"""Solution module for Day X, YEAR"""
from collections import defaultdict
import copy
import functools
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


@functools.lru_cache()
def compute(wire):
    global data

    try:
        return int(wire)
    except ValueError:
        pass

    cmd = data[wire].split(" ")

    if "NOT" in cmd:
        return ~compute(cmd[1])
    if "AND" in cmd:
        return compute(cmd[0]) & compute(cmd[2])
    elif "OR" in cmd:
        return compute(cmd[0]) | compute(cmd[2])
    elif "LSHIFT" in cmd:
        return compute(cmd[0]) << compute(cmd[2])
    elif "RSHIFT" in cmd:
        return compute(cmd[0]) >> compute(cmd[2])
    else:
        return compute(cmd[0])


data = {}


def solution_1(input):
    for instr in input:
        op, wire = instr.split(" -> ")
        data[wire.strip()] = op

    return compute("a")


def solution_2(input):
    for instr in input:
        op, wire = instr.split(" -> ")
        data[wire.strip()] = op

    data["b"] = str(compute("a"))
    compute.cache_clear()
    return compute("a")


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    #    input = """123 -> x
    # 456 -> y
    # x AND y -> d
    # x OR y -> e
    # x LSHIFT 2 -> f
    # y RSHIFT 2 -> g
    # NOT x -> h
    # NOT y -> i"""
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
