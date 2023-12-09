"""Solution module for Day 9, 2023"""
import copy
import time

from advent_of_code.utils.fetch import fetch


def parse(input):
    histories = []
    for line in input.split("\n"):
        history = []
        for number in line.split():
            history.append(int(number))
        histories.append(history)
    return histories


def differ(history):
    differences = []
    for i in range(len(history)-1):
        differences.append(history[i+1] - history[i])
    return differences


def extrapolate(history):
    extrapolated_number = history[-1]
    while not all(d == 0 for d in history):
        history = differ(history)
        extrapolated_number += history[-1]
    return extrapolated_number


def solution_1(input):

    histories = parse(input)

    extrapolated_numbers = []
    for history in histories:
        extrapolated_numbers.append(extrapolate(history))

    return sum(extrapolated_numbers)


def solution_2(input):

    histories = parse(input)

    extrapolated_numbers = []
    for history in histories:
        extrapolated_numbers.append(extrapolate(history[::-1]))  # just reverse the history

    return sum(extrapolated_numbers)


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
