"""Solution module for Day 15, 2022"""
import copy
import time
from sys import maxsize
from advent_of_code.utils.coordinates import draw_coordinates

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.manhattan import get_manhattan_distance
from advent_of_code.utils.parse import split_str_by_newline, parse_all_numbers


def parse(input):
    sensors_beacons = list()
    for line in input:
        sx, sy, bx, by = parse_all_numbers(line)
        sensors_beacons.append(((sx, sy), (bx, by)))
    return sensors_beacons


# Disclaimer
# I had a lot of help with this solution.


def solution_1(input):
    sensors_and_beacons = parse(input)

    ROW = 2000000

    beacons = set((bx, by) for _, (bx, by) in sensors_and_beacons)
    no_beacons = set()

    for (sx, sy), (bx, by) in sensors_and_beacons:
        dist_to_closest_beacon = get_manhattan_distance((sx, sy), (bx, by))

        for dx in [1, -1]:
            dist_to_row = abs(sy - ROW)
            cx = sx

            while dist_to_row <= dist_to_closest_beacon:
                no_beacons.add((cx, ROW))
                cx += dx
                dist_to_row += 1

    return len(no_beacons - beacons)


def solution_2(input):
    sensors_and_beacons = parse(input)

    MIN_COORD = 0
    MAX_COORD = 4000000

    for y in range(MIN_COORD, MAX_COORD + 1):
        ranges = list()

        for (sx, sy), (bx, by) in sensors_and_beacons:
            dist_to_closest_beacon = get_manhattan_distance((sx, sy), (bx, by))
            dist_to_row = abs(sy - y)
            diff = dist_to_closest_beacon - dist_to_row

            if diff < 0:
                continue

            ranges.append((sx - diff, sx + diff))

        ranges.sort()
        compact = list()
        lx, hx = ranges[0]

        for nlx, nhx in ranges[1:]:
            if nlx - 1 <= hx:
                hx = max(hx, nhx)
            else:
                compact.append((lx, hx))
                lx, hx = nlx, nhx

        compact.append((lx, hx))

        if len(compact) != 1:
            (a, b), (c, d) = compact
            return (b + 1) * 4000000 + y


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
