"""Solution module for Day X, YEAR"""
import time
from typing import List, Tuple

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_number_by_newline, split_str_by_separator


def find_intersections(path_1, path_2: List[Tuple[int]]) -> List[Tuple[Tuple, int]]:
    inverse_index = {point: idx for idx, point in enumerate(path_1)}

    return [
        (idx, inverse_index[point])
        for idx, point in enumerate(path_2)
        if point in inverse_index
    ]


def manhattan_distance(point: Tuple[int, int]) -> int:
    return abs(point[0]) + abs(point[1])


def manhattan_path(steps: List[str]) -> List[Tuple[int, int]]:

    x = 0
    y = 0
    path = list()

    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        if direction == "U":
            path += [(x, y + inc) for inc in range(1, distance + 1)]
            y += distance
        elif direction == "D":
            path += [(x, y - inc) for inc in range(1, distance + 1)]
            y -= distance
        elif direction == "L":
            path += [(x - inc, y) for inc in range(1, distance + 1)]
            x -= distance
        elif direction == "R":
            path += [(x + inc, y) for inc in range(1, distance + 1)]
            x += distance
        else:
            raise ValueError(f"Invalid direction: {direction}")

    return path


def solution_1(w1, w2: List[str]):
    path_1 = manhattan_path(w1)
    path_2 = manhattan_path(w2)
    intersections = list(set(path_1).intersection(path_2))
    return min([manhattan_distance(p) for p in intersections])


def solution_2(w1, w2: List[str]):
    path_1 = manhattan_path(w1)
    path_2 = manhattan_path(w2)
    intersections = find_intersections(path_1, path_2)
    return min(
        [p1 + p2 + 2 for (p1, p2) in intersections]
    )  # +2 to account for step from (0, 0)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_separator(input, "\n")
    wire_1 = split_str_by_separator(parsed_input[0], ",")
    wire_2 = split_str_by_separator(parsed_input[1], ",")

    tic = time.perf_counter()
    s1 = solution_1(wire_1, wire_2)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(wire_1, wire_2)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
