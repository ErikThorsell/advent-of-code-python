"""Solution module for Day 5, 2022"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_crates


def move(stacks, num_moves, from_stack, to_stack):
    stacks[to_stack] += stacks[from_stack][-num_moves:]
    stacks[from_stack] = stacks[from_stack][:-num_moves]
    return stacks


def solution_1(input):
    stacks, instructions = input
    for num_moves, from_stack, to_stack in instructions:
        for _ in range(num_moves):
            stacks = move(stacks, 1, from_stack, to_stack)
    return "".join([stacks[s][-1] for s in sorted(stacks.keys())])


def solution_2(input):
    stacks, instructions = input
    for num_moves, from_stack, to_stack in instructions:
        stacks = move(stacks, num_moves, from_stack, to_stack)
    return "".join([stacks[s][-1] for s in sorted(stacks.keys())])


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_crates(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
