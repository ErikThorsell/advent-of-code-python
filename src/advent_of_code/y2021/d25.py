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


def move_east(sea, width):
    new_sea = dict()
    for (x, y) in sea:
        if sea[(x, y)] == ">" and ((x + 1) % width, y) not in sea:
            new_sea[((x + 1) % width, y)] = ">"
        else:
            new_sea[(x, y)] = sea[(x, y)]
    return new_sea


def move_south(sea, height):
    new_sea = dict()
    for (x, y) in sea:
        if sea[(x, y)] == "v" and (x, (y + 1) % height) not in sea:
            new_sea[(x, (y + 1) % height)] = "v"
        else:
            new_sea[(x, y)] = sea[(x, y)]
    return new_sea


def solution_1(sea):
    width, height = get_grid_dimensions(sea)

    iterations = 0
    while True:
        iterations += 1

        east_sea = move_east(sea, width)
        new_sea = move_south(east_sea, height)

        if sea == new_sea:
            return iterations

        sea = new_sea


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    east, south = parse_sea_cucumbers(input)

    tic = time.perf_counter()
    s1 = solution_1(east | south)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")
