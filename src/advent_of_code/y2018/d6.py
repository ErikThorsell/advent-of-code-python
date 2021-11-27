"""Solution module for Day X, YEAR"""
from collections import Counter
import copy
import operator
import time
from typing import List, Tuple

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.manhattan import get_manhattan_distance
from advent_of_code.utils.parse import parse_coordinates


def get_boundries(coordinates: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    left_edge = min(coordinates, key=operator.itemgetter(0))[0]
    right_edge = max(coordinates, key=operator.itemgetter(0))[0]
    top_edge = min(coordinates, key=operator.itemgetter(1))[1]
    bottom_edge = max(coordinates, key=operator.itemgetter(1))[1]
    return (left_edge, right_edge, top_edge, bottom_edge)


def is_finite(c: Tuple[int, int], boundries: Tuple[int, int, int, int]) -> bool:
    left_edge, right_edge, top_edge, bottom_edge = boundries
    return left_edge < c[0] < right_edge and top_edge < c[1] < bottom_edge


def unique_min(distances: List[int]) -> bool:
    sorted_distances = sorted(distances)
    return sorted_distances[0] != sorted_distances[1]


def get_index_of_min(distances: List[int]) -> int:
    return distances.index(min(distances))


def solution_1(input):
    boundries = get_boundries(input)
    left_edge, right_edge, top_edge, bottom_edge = boundries

    count = Counter()
    for x in range(left_edge, right_edge):
        for y in range(top_edge, bottom_edge):
            distances = [get_manhattan_distance((x, y), c) for c in input]

            if unique_min(distances):
                count[input[get_index_of_min(distances)]] += 1

    maximum_area = 0
    for c in input:
        if is_finite(c, boundries):
            maximum_area = max(maximum_area, count[c])

    return maximum_area


def solution_2(input):
    left_edge, right_edge, top_edge, bottom_edge = get_boundries(input)
    count = 0
    for x in range(left_edge, right_edge):
        for y in range(top_edge, bottom_edge):
            distances = [get_manhattan_distance((x, y), c) for c in input]
            if sum(distances) < 10000:
                count += 1
    return count


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_coordinates(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
