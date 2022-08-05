"""Solution module for Day X, YEAR"""
import copy
import time
import pprint
from sys import maxsize

import numpy as np

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_separator


def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


def solution_1(input):
    layers = list(chunks(input, 25 * 6))

    fewest_zeroes = maxsize
    product = 0
    for l in layers:
        occ = l.count(0)
        if occ < fewest_zeroes:
            fewest_zeroes = occ
            product = l.count(1) * l.count(2)

    return product


def display(canvas):
    for h in range(6):
        for w in range(25):
            if canvas[h, w] == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print()


def solution_2(input):
    canvas = np.empty((6, 25))
    layers = np.split(np.array(input), len(input) / (25 * 6))

    for layer in reversed(layers):
        layer = layer.reshape(6, 25)
        for h in range(6):
            for w in range(25):
                if layer[h, w] == 2:
                    continue
                canvas[h, w] = layer[h, w]

    display(canvas)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [int(d) for d in input]

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
