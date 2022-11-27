"""Solution module for Day X, YEAR"""
import copy
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):
    real_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    for idx, sue in enumerate(input):
        attributes = re.findall(r"(\w+: \d+)", sue)

        match = True
        for attribute in attributes:
            attr = attribute.split(":")[0].strip()
            count = int(attribute.split(":")[1].strip())
            if real_sue[attr] != count:
                match = False
        if match:
            return idx + 1


def solution_2(input):
    real_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    for idx, sue in enumerate(input):
        attributes = re.findall(r"(\w+: \d+)", sue)

        match = True
        for attribute in attributes:
            attr = attribute.split(":")[0].strip()
            count = int(attribute.split(":")[1].strip())
            if attr in ["cats", "trees"]:
                if real_sue[attr] >= count:
                    match = False
            elif attr in ["pomeranians", "goldfish"]:
                if real_sue[attr] <= count:
                    match = False
            elif real_sue[attr] != count:
                match = False

        if match:
            return idx + 1


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
