"""Solution module for Day 10, 2022"""
from collections import defaultdict
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(program):

    cycle = 0
    register = 1
    signal_strength = 0

    for instr in program:

        op = instr.split()[0]

        for _ in range(1 if op == "noop" else 2):
            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strength += cycle * register

        if op == "addx":
            register += int(instr.split()[1])

    return signal_strength


# Guesses
# EFGERVRE  <-- stupid V or U
def solution_2(program):
    cycle = 0
    register = 1
    display = list()
    row = ""

    for instr in program:

        op = instr.split()[0]

        for _ in range(1 if op == "noop" else 2):
            cycle += 1

            row += "#" if len(row) in range(register - 1, register + 2) else "."
            if len(row) == 40:
                display.append(row)
                row = ""

        if op == "addx":
            register += int(instr.split()[1])

    return "\n" + "\n".join(display)


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
