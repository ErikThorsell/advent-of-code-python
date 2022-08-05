"""Solution module for Day X, YEAR"""
import copy
from itertools import permutations
from sys import maxsize
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.intcode import Intcode
from advent_of_code.utils.parse import split_number_by_separator


def amplify(program, phase_seq):
    signal = 0
    for phase in phase_seq:
        intcode = Intcode(program, phase)
        intcode.run(signal)
        signal = intcode.output
    return signal


def feedback_amplify(program, phase_seq):
    signal = 0
    last_valid = None

    intcodes = [Intcode(program, phase) for phase in phase_seq]

    while not any([intcode.done for intcode in intcodes]):
        for i in range(len(intcodes)):
            (signal, _) = intcodes[i].run(signal)
            if signal is not None:
                last_valid = signal

    return last_valid


def solution_1(input):
    return max([amplify(input, seq) for seq in permutations(range(5))])


def solution_2(input):
    return max([feedback_amplify(input, seq) for seq in permutations(range(5, 10))])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_number_by_separator(input, ",")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
