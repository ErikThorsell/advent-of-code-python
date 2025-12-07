"""Solution module for Day 6, 2025"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    answer = 4277556
    assert(solution_1(input) == answer)

def test_2():
    input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    answer = 3263827
    assert(solution_2(input) == answer)


def solution_1(input):

    lines = input.split("\n")
    ops = lines[-1].split()
    ints = [list(map(int, line.split())) for line in lines[:-1]]
    ints = list(zip(*ints))  # transpose

    results = []
    for i, o in zip(ints, ops):
        if o == "+":
            results.append(sum(i))
        elif o == "*":
            prod = 1
            for p in i:
                prod *= p
            results.append(prod)

    return sum(results)


def parse_cephalopod(text):
    lines = text.rstrip('\n').split("\n")
    rows = lines[:-1]
    op_row = lines[-1]

    width = max(len(line) for line in lines)
    rows = [line.ljust(width) for line in rows]
    op_row = op_row.ljust(width)

    def is_separator_col(i):
        return all(r[i] == ' ' for r in rows) and op_row[i] == ' '

    problems = []
    col = 0
    while col < width:
        if is_separator_col(col):
            col += 1
            continue

        block_cols = []
        while col < width and not is_separator_col(col):
            block_cols.append(col)
            col += 1

        op_candidates = [op_row[c] for c in block_cols if op_row[c].strip()]
        op = op_candidates[0] if op_candidates else None

        numbers = []
        for c in reversed(block_cols):
            digits = [r[c] for r in rows if r[c].isdigit()]
            if digits:
                numbers.append(int(''.join(digits)))

        problems.append((op, numbers))

    return problems


def solution_2(input):
    problems = parse_cephalopod(input)

    results = []
    for op, ints in problems:
        if op == "+":
            results.append(sum(ints))
        elif op == "*":
            prod = 1
            for p in ints:
                prod *= p
            results.append(prod)

    return sum(results)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    test_2()
    print("Test 2 was successful!")
    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
