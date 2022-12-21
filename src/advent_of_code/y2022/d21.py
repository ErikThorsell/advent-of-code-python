"""Solution module for Day 21, 2022"""
import copy
import re
import time
from sys import maxsize

import z3

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(lines):
    monkeys = dict()

    for line in lines:
        monkey, operation = line.split(":")

        monkey = monkey.strip()
        operation = operation.strip()

        if operation.isnumeric():
            monkeys[monkey] = int(operation)

        else:
            l, op, r = operation.split()
            monkeys[monkey] = (l, r, op)

    return monkeys


def solution_1(input):
    monkeys = parse(input)

    while not isinstance(monkeys["root"], int):

        for monkey, value in monkeys.items():

            if isinstance(value, int):
                continue

            left = value[0]
            right = value[1]

            if isinstance(monkeys[left], int) and isinstance(monkeys[right], int):
                expr = f"{monkeys[left]} {value[2]} {monkeys[right]}"
                ans = eval(expr)
                monkeys[monkey] = int(ans)

    return monkeys["root"]


def solution_2(input):

    s = z3.Optimize()

    for line in input:
        for m in re.findall(r"[a-z]{4}", line):
            exec(f'{m} = z3.Int("{m}")')

        if line[:4] == "humn":
            continue

        if line[:4] == "root":
            line = line[6:].replace("+", "==")

        exec(f's.add({line.replace(":", "==")})')

    s.check()
    return s.model()[z3.Int("humn")]


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
