"""Solution module for Day 8, 2015"""
import copy
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):

    total_length = 0

    for line in input:
        code_length = len(line)

        # Remove double quotes
        line = line[1:-1]

        # Count escaped backslashes and then remove them
        backslashes = re.findall(r"\\\\", line)
        code_length -= len(backslashes)
        line = line.replace("\\\\", "")

        # Count double quotes and then remove them
        double_quotes = re.findall(r"\\\"", line)
        code_length -= len(double_quotes)
        line = line.replace('\\"', "")

        # Substitute encoded characters
        encoded = re.findall(r"\\x.{2}", line)
        for e in encoded:
            n = e.replace("\\x", "")
            line = line.replace(e, chr(int(n, 16)))
        code_length -= len(line)

        total_length += code_length

    return total_length


def solution_2(input):

    total_length = 0

    for line in input:
        line_length = len(line)

        # Backslashes
        line = re.sub(r"\\", r"\\\\", line)

        # Double quote
        line = re.sub(r"\"", r'\\"', line)

        # Outer quotes
        line = '"' + line + '"'

        total_length += len(line) - line_length

    return total_length


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
