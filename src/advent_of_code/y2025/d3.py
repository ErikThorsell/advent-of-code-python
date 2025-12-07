"""Solution module for Day 3, 2025"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    answer = 357
    assert(solution_1(input) == answer)

def test_2():
    input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    answer = 3121910778619
    assert(solution_2(input) == answer)


def solution_1(input):

    max_joltage = 0

    for bank in input.split("\n"):
        num_batt = len(bank)
        max_in_bank = -maxsize

        for i in range(num_batt):
            for j in range(i+1, num_batt):
                current = int(bank[i]) * 10 + int(bank[j])

                if current > max_in_bank:
                    max_in_bank = current

        max_joltage += max_in_bank

    return max_joltage


def solution_2(input):
    max_joltage = 0
    size = 12

    for bank in input.split("\n"):
        n = len(bank)

        chosen_digits = []
        start = 0
        remaining = size

        while remaining > 0:
            end = n - remaining

            best_pos = start
            best_digit = bank[start]

            for i in range(start + 1, end + 1):
                if bank[i] > best_digit:
                    best_digit = bank[i]
                    best_pos = i
                    if best_digit == '9':
                        break

            chosen_digits.append(best_digit)
            start = best_pos + 1
            remaining -= 1

        max_joltage += int("".join(chosen_digits))

    return max_joltage


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
