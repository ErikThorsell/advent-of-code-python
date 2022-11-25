"""Solution module for Day X, YEAR"""
import copy
from itertools import groupby
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.comb_it import sliding_window


def valid_password(password):
    # Illegal characters
    if any(c in password for c in ["i", "o", "l"]):
        return False

    # Must contain straight
    if not any(ord(t[1]) - ord(t[0]) == 1 and ord(t[2]) - ord(t[1]) == 1 for t in sliding_window(password, 3)):
        return False

    # Must contain pair
    equals = [list(g) for _, g in groupby(password) if len(list(g)) == 2]
    if len(equals) < 2:
        return False

    return True


def increment(password):
    chars = [ord(c) for c in password]
    for i in range(len(chars) - 1, 0, -1):
        # if char is lower than z, increment and break loop
        if chars[i] < 122:
            chars[i] += 1
            break
        # if char IS z, set to a and continue loop
        if chars[i] == 122:
            chars[i] = 97

    return "".join([chr(c) for c in chars])


def solution_1(input):
    password = input

    while True:
        password = increment(password)
        if valid_password(password):
            return password


def solution_2(input):
    first_password = solution_1(input)
    return solution_1(first_password)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
