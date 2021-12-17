"""Solution module for Day 17, 2021"""
import copy
import time
from typing import Tuple
from sys import maxsize
from advent_of_code.utils.coordinates import draw_coordinates, get_grid_dimensions

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_all_numbers


def step(pos, vel: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    x_pos, y_pos = pos
    x_vel, y_vel = vel

    x_pos += x_vel
    y_pos += y_vel

    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1

    y_vel -= 1

    return (x_pos, y_pos), (x_vel, y_vel)


def in_target_area(pos, x_target, y_target: Tuple[int, int]) -> bool:
    x_pos, y_pos = pos
    return x_target[0] <= x_pos <= x_target[1] and y_target[0] <= y_pos <= y_target[1]


def missed_target_area(pos, vel, x_target, y_target: Tuple[int, int]) -> bool:
    x_pos, y_pos = pos
    x_vel, y_vel = vel

    if x_vel > 0 and x_pos > x_target[1]:
        return True

    if y_vel < 0 and y_pos < y_target[0]:
        return True


def solution_1(input):
    x_target = tuple(parse_all_numbers(input.split(",")[0]))
    y_target = tuple(parse_all_numbers(input.split(",")[1]))
    y_max = -maxsize

    for x_vel in range(max(x_target) + 1):
        for y_vel in range(min(y_target), -2 * min(y_target)):
            pos = (0, 0)
            vel = (x_vel, y_vel)

            y_sub = -maxsize
            for _ in range(1, 1000):

                pos, vel = step(pos, vel)
                if pos[1] > y_sub:
                    y_sub = pos[1]

                if missed_target_area(pos, vel, x_target, y_target):
                    break

                if in_target_area(pos, x_target, y_target):
                    if y_sub > y_max:
                        y_max = y_sub
                    break

    return y_max


def solution_2(input):
    x_target = tuple(parse_all_numbers(input.split(",")[0]))
    y_target = tuple(parse_all_numbers(input.split(",")[1]))
    hits_target = list()

    for x_vel in range(max(x_target) + 1):
        for y_vel in range(min(y_target), -2 * min(y_target)):
            pos = (0, 0)
            vel = (x_vel, y_vel)

            for _ in range(1, 1000):
                pos, vel = step(pos, vel)

                if in_target_area(pos, x_target, y_target):
                    hits_target.append((x_vel, y_vel))
                    break

                if missed_target_area(pos, vel, x_target, y_target):
                    break

    return len(hits_target)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
