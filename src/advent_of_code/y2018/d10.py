"""Solution module for Day X, YEAR"""
from copy import deepcopy
from operator import ge
import time

from advent_of_code.utils.coordinates import (
    draw_coordinates,
    get_canvas_dimensions,
    get_coordinates,
    get_min_max_velocity,
    get_velocities,
    move_coordinates,
)
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_star_vectors


def solution_1(vectors):
    iterations = 0
    while True:
        iterations += 1
        vectors = move_coordinates(vectors)
        _, height = get_canvas_dimensions(get_coordinates(vectors))
        if height == 10:
            draw_coordinates(get_coordinates(vectors))
            return iterations

    # I really do not like that the letter size is different between the test input and the actual input.
    # In the test input the height of the letters is 8.
    # In the actual input the height of the letters is 10.


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_star_vectors(input)

    tic = time.perf_counter()
    s2 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1 is shown in the terminal output above.")
    print(f"Solution for problem 2: {s2}.")
    print(f"Both acquired in: {toc-tic:0.4f} seconds.")
