"""Solution module for Day 11, 2022"""
from collections import defaultdict
import copy
from math import prod
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_separator


def parse(raw_monkeys):
    monkeys = defaultdict(dict)

    for idx, monkey in enumerate(raw_monkeys):

        for row in monkey.split("\n"):

            if row.strip().startswith("Starting"):
                monkeys[idx]["items"] = list(map(int, re.findall(r"-?\d+", row)))

            if row.strip().startswith("Operation"):
                monkeys[idx]["op"] = row.split("= old")[-1].strip()

            if row.strip().startswith("Test"):
                monkeys[idx]["test"] = list(map(int, re.findall(r"-?\d+", row)))[0]

            if row.strip().startswith("If true"):
                monkeys[idx]["True"] = list(map(int, re.findall(r"-?\d+", row)))[0]

            if row.strip().startswith("If false"):
                monkeys[idx]["False"] = list(map(int, re.findall(r"-?\d+", row)))[0]

    return monkeys


def turn(monkeys, inspections, divisor):
    for m in monkeys:

        # Inspect each item
        while monkeys[m]["items"]:
            worry_level = monkeys[m]["items"].pop(0)

            # Determine new worry level
            match monkeys[m]["op"].split():
                case "*", "old":
                    worry_level **= 2
                case "*", v:
                    worry_level *= int(v)
                case "+", v:
                    worry_level += int(v)

            # Calm down
            if divisor == 3:
                worry_level //= 3
            else:
                worry_level = worry_level % divisor

            # Test
            if worry_level % monkeys[m]["test"] == 0:
                throw_to = monkeys[m]["True"]
            else:
                throw_to = monkeys[m]["False"]

            inspections[m] += 1
            monkeys[throw_to]["items"].append(worry_level)
    
    return monkeys, inspections


# Guesses for Part 1
# 30994116943608
def solution_1(input):
    monkeys = parse(input)
    inspection = [0] * len(monkeys)

    for _ in range(20):
        monkeys, inspection = turn(monkeys, inspection, 3)

    return prod(sorted(inspection)[-2:])


# Guesses for Part 2
# 2713310158
def solution_2(input):
    monkeys = parse(input)
    divisor = prod(set([m["test"] for m in monkeys.values()]))  # divide with gcd
    inspection = [0] * len(monkeys)

    for _ in range(10000):
        monkeys, inspection = turn(monkeys, inspection, divisor)

    return prod(sorted(inspection)[-2:])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_separator(input, "\n\n")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
