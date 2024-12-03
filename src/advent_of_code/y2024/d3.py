"""Solution module for Day 3, 2024"""
import copy
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    answer = 161
    assert(solution_1(input) == answer)
    

def test_2():
    input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    answer = 48
    assert(solution_2(input) == answer)


def solution_1(input):
    valid = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(valid, input)
    return sum(int(x)*int(y) for x, y in matches)


def solution_2(input):
    actions = r"(do\(\)|don't\(\))"
    mul = r"mul\((\d{1,3}),(\d{1,3})\)"

    tokens = list(re.finditer(fr"{actions}|{mul}", input))

    total = 0
    action = "do()"

    for token in tokens:
        if token.group(1):
            action = token.group(1)
        elif token.group(2) and token.group(3) and action == "do()":
            total += int(token.group(2)) * int(token.group(3))
    
    return total


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
