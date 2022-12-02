"""Solution module for Day 2, 2022"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


# Guesses for Part 1
# 10360
def solution_1(input):
    trans = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
    rules = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    scores = {"Rock": 1, "Paper": 2, "Scissors": 3}
    score = 0
    for round in input:
        elf, me = round.split()
        elf = trans[elf]
        me = trans[me]

        score += scores[me]

        if rules[me] == elf:
            score += 6
        elif me == elf:
            score += 3

    return score


# Guesses for Part 2
# 6886
def solution_2(input):
    trans = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
    strategy = {"Y": "Draw", "X": "Lose", "Z": "Win"}
    rules = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    scores = {"Rock": 1, "Paper": 2, "Scissors": 3}
    score = 0
    for round in input:
        elf, me = round.split()
        elf = trans[elf]

        wanted_outcome = strategy[me]

        if wanted_outcome == "Draw":
            score += scores[elf]
            score += 3
        elif wanted_outcome == "Lose":
            score += scores[rules[elf]]
            score += 0
        elif wanted_outcome == "Win":
            score += scores[rules[rules[elf]]]
            score += 6

    return score


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
