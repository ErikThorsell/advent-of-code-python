"""Solution module for Day X, YEAR"""
from operator import itemgetter
import time
from advent_of_code.utils.coordinates import get_grid_dimensions

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_sea_cucumbers


def draw(grid) -> None:
    x_min = min(grid, key=itemgetter(0))[0]
    y_min = min(grid, key=itemgetter(1))[1]
    x_max = max(grid, key=itemgetter(0))[0]
    y_max = max(grid, key=itemgetter(1))[1]
    print()
    for y in range(y_min, y_max + 1):  # loop y first to get same output as AoC
        for x in range(x_min, x_max + 1):
            if (x, y) in grid:
                print(grid[(x, y)], end="")
            else:
                print(".", end="")
        print()
    print()


def move(east, south, width, height):
    new_east = dict()
    new_south = dict()

    for (x, y) in east:
        if ((x + 1) % width, y) not in east | south:
            new_east[((x + 1) % width, y)] = ">"
        else:
            new_east[(x, y)] = ">"

    for (x, y) in south:
        if (x, (y + 1) % height) not in south | new_east:
            new_south[(x, (y + 1) % height)] = "v"
        else:
            new_south[(x, y)] = "v"

    return new_east, new_south


def solution_1(east, south):
    width, height = get_grid_dimensions(east | south)

    iterations = 0
    while True:
        iterations += 1

        new_east, new_south = move(east, south, width, height)

        if new_east == east and new_south == south:
            return iterations

        east, south = new_east, new_south


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    east, south = parse_sea_cucumbers(input)

    tic = time.perf_counter()
    s1 = solution_1(east, south)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")
