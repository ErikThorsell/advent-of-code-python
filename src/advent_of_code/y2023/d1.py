"""Solution module for Day 1, 2023"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):
    sum = 0
    for l in input:
        ints = [char for char in l if char.isdigit()]
        sum += int(''.join([ints[0],ints[-1]]))
    return sum


def solution_2(input):
    digits = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    sum = 0
    for line in input:
        f_digit = None
        b_digit = None

        # Find digit from front
        f_idx = 0
        while f_digit is None:

            p_str = line[:f_idx + 1]

            for digit in digits.keys():
                if digit in p_str:
                    f_digit = digits[digit]

            f_idx += 1


        # Find digit from back
        b_idx = 0
        while b_digit is None:
            p_str = line[len(line) - 1 - b_idx:]

            for digit in digits.keys():
                if digit in p_str:
                    b_digit = digits[digit]
            
            b_idx += 1
            
#        print(f"Line: {line} -- found digits {f_digit} and {b_digit} == {f_digit}{b_digit}")
        num = f"{f_digit}{b_digit}"
        sum += int(num)

    return sum


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
