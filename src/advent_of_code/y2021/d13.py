"""Solution module for Day 13, 2021"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.coordinates import draw_coordinates, fold_grid
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_folding


def solution_1(input):
    coordinates = input[0]
    instructions = input[1]
    coordinates = fold_grid(coordinates, instructions[0])
    return len(coordinates)


def solution_2(input):
    coordinates = input[0]
    instructions = input[1]
    for instr in instructions:
        coordinates = fold_grid(coordinates, instr)
    draw_coordinates(coordinates)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_folding(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
