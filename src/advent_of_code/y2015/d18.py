"""Solution module for Day X, YEAR"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import get_adjacent, get_cell, print_grid
from advent_of_code.utils.parse import parse_grid_str


def solution_1(grid):

    for _ in range(100):
        new_grid = []
        for rx, _ in enumerate(grid):
            new_grid.append([])
            for cx, _ in enumerate(grid[rx]):
                light = grid[rx][cx]

                neighbors = [
                    get_cell(grid, n[0], n[1]) for n in get_adjacent(cx, rx, 8)
                ]
                lit_neighbors = neighbors.count("#")

                if light == "#" and 2 <= lit_neighbors <= 3:
                    new_grid[rx].append("#")
                elif light == "." and lit_neighbors == 3:
                    new_grid[rx].append("#")
                else:
                    new_grid[rx].append(".")

        grid = copy.deepcopy(new_grid)

    return "".join(str(light) for row in grid for light in row).count("#")


def solution_2(grid):
    grid[0][0] = "#"
    grid[0][len(grid) - 1] = "#"
    grid[len(grid) - 1][0] = "#"
    grid[len(grid) - 1][len(grid) - 1] = "#"

    for _ in range(100):
        new_grid = []
        for rx, _ in enumerate(grid):
            new_grid.append([])
            for cx, _ in enumerate(grid[rx]):
                light = grid[rx][cx]

                # Fix s.t. if neighbour is a corner, it returns #
                neighbors = [
                    get_cell(grid, n[0], n[1]) for n in get_adjacent(cx, rx, 8)
                ]
                lit_neighbors = neighbors.count("#")

                if rx == cx == 0:
                    new_grid[rx].append("#")
                elif rx == 0 and cx == len(grid) - 1:
                    new_grid[rx].append("#")
                elif rx == len(grid) - 1 and cx == 0:
                    new_grid[rx].append("#")
                elif rx == len(grid) - 1 and cx == len(grid) - 1:
                    new_grid[rx].append("#")
                elif light == "#" and 2 <= lit_neighbors <= 3:
                    new_grid[rx].append("#")
                elif light == "." and lit_neighbors == 3:
                    new_grid[rx].append("#")
                else:
                    new_grid[rx].append(".")

        grid = copy.deepcopy(new_grid)

    return "".join(str(light) for row in grid for light in row).count("#")


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    #    input = """##.#.#
    # ...##.
    ##....#
    # ..#...
    ##.#..#
    #####.#"""
    parsed_input = parse_grid_str(input)

    #    tic = time.perf_counter()
    #    s1 = solution_1(copy.deepcopy(parsed_input))
    #    toc = time.perf_counter()
    #    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
