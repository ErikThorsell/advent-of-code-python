"""Solution module for Day 2, 2021"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_sub_commands
from advent_of_code.utils.submarine import drive_sub, drive_sub_aim


def solution_1(input):
    position = (0, 0)
    for command in input:
        position = drive_sub(position, command)
    return position[0] * position[1]


def solution_2(input):
    position = (0, 0)
    aim = 0
    for command in input:
        position, aim = drive_sub_aim(position, aim, command)
    return position[0] * position[1]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_sub_commands(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
