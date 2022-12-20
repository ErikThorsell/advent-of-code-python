"""Solution module for Day 20, 2022"""
from collections import deque
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline


def encrypt(input, encrypt):
    for idx, n in enumerate(input):
        encrypt.rotate(-encrypt.index((idx, n)))
        encrypt.popleft()
        encrypt.rotate(-n % len(encrypt))
        encrypt.appendleft((idx, n))
    return encrypt


def solution_1(input):
    encque = deque(list(enumerate(input)))

    encque = encrypt(input, encque)

    mixed = deque([n for (_, n) in encque])
    mixed.rotate(-mixed.index(0))

    return mixed[1000 % len(mixed)] + mixed[2000 % len(mixed)] + mixed[3000 % len(mixed)]


def solution_2(input):
    input = [i * 811589153 for i in input]
    encque = deque(list(enumerate(input)))

    for _ in range(10):
        encque = encrypt(input, encque)

    mixed = deque([n for (_, n) in encque])
    mixed.rotate(-mixed.index(0))

    return mixed[1000 % len(mixed)] + mixed[2000 % len(mixed)] + mixed[3000 % len(mixed)]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
