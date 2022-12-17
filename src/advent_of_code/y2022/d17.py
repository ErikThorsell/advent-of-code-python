"""Solution module for Day 17, 2022"""
from collections import defaultdict
import copy
from operator import itemgetter
import time
from typing import List, Tuple
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def draw_chamber(coordinates: List[Tuple[int, int]]) -> None:
    x_min = 0
    x_max = 6
    y_min = min(coordinates, key=itemgetter(1))[1]
    y_max = max(coordinates, key=itemgetter(1))[1]
    print()
    for y in range(y_max, y_min - 1, -1):  # loop y first to get same output as AoC
        for x in range(x_min, x_max + 1):
            if (x, y) in coordinates:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


ROCKS = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # Horizontal Line
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),  # Cross
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),  # J
    ((0, 0), (0, 1), (0, 2), (0, 3)),  # I
    ((0, 0), (1, 0), (0, 1), (1, 1)),  # Square
]


def jet_movement(chamber, rock, jet):
    if jet == ">":
        rock_ = [(r[0] + 1, r[1]) for r in rock]
        if any(r in chamber for r in rock_) or any(r[0] > 6 for r in rock_):
            return rock
        return rock_
    if jet == "<":
        rock_ = [(r[0] - 1, r[1]) for r in rock]
        if any(r in chamber for r in rock_) or any(r[0] < 0 for r in rock_):
            return rock
        return rock_


def fall_movement(chamber, rock):
    rock_ = [(r[0], r[1] - 1) for r in rock]
    if any(r in chamber for r in rock_) or any(r[1] == 0 for r in rock_):
        return rock, True
    return rock_, False


def solution_1(jet_pattern):
    chamber = set()

    jet_idx = 0
    fallen_rocks = 0
    while fallen_rocks < 2022:

        rock_idx = fallen_rocks % 5
        rock = ROCKS[rock_idx]

        # Move rock to correct initial position
        bottom = 0 if not chamber else max(r[1] for r in chamber)
        x_shift = 2
        y_shift = bottom + 4
        rock = [(c[0] + x_shift, c[1] + y_shift) for c in rock]

        in_place = False
        while not in_place:

            # Get Pushed
            jet_idx = jet_idx % len(jet_pattern)
            rock = jet_movement(chamber, rock, jet_pattern[jet_idx])
            jet_idx += 1

            # Fall
            rock, in_place = fall_movement(chamber, rock)

        fallen_rocks += 1
        chamber.update(rock)

    return max(r[1] for r in chamber), chamber


def solution_2(jet_pattern):
    chamber = set()
    cache = dict()

    jet_idx = 0
    fallen_rocks = 0
    added_by_cycle = 0
    once = False
    twice = False
    while fallen_rocks < 1e12:

        rock_idx = fallen_rocks % 5
        rock = ROCKS[rock_idx]

        # Move rock to correct initial position
        bottom = 0 if not chamber else max(r[1] for r in chamber)
        x_shift = 2
        y_shift = bottom + 4
        rock = [(c[0] + x_shift, c[1] + y_shift) for c in rock]

        in_place = False
        while not in_place:

            # Get Pushed
            jet_idx = jet_idx % len(jet_pattern)
            rock = jet_movement(chamber, rock, jet_pattern[jet_idx])
            jet_idx += 1

            # Fall
            rock, in_place = fall_movement(chamber, rock)

        fallen_rocks += 1
        chamber.update(rock)

        height = max(r[1] for r in chamber)
        key = (jet_idx, rock_idx, frozenset([(x, height - y) for (x, y) in chamber if height - y <= 30]))

        # If we detect a cycle, we take a little shortcut...
        if key in cache:

            (prev_fallen_rocks, prev_height) = cache[key]

            cycle_num_rocks = fallen_rocks - prev_fallen_rocks
            cycle_height = height - prev_height

            # After we have "used" the cache once we still need to add some more rocks using the regular way.
            # We will hit the cache every time though, but the cycle_factor = 0 because the nominator will be smaller
            # than the denominator, so this is not a problem.
            cycle_factor = int((1e12 - fallen_rocks) // cycle_num_rocks)

            added_by_cycle += int(cycle_factor * cycle_height)
            fallen_rocks += int(cycle_factor * cycle_num_rocks)

        cache[key] = (fallen_rocks, height)

    return height + added_by_cycle


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1, _ = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
