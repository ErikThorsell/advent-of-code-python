"""Solution module for Day 14, 2023"""
import copy
import time

from advent_of_code.utils.coordinates import get_grid_dimensions
from advent_of_code.utils.fetch import fetch


def test_1():
    input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
    assert(solution_1(input) == 136)


def test_2():
    input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
    assert(solution_2(input) == 64)


def parse(input):
    rocks = {}
    for iy, row in enumerate(input.split("\n")):
        for ix, chr in enumerate(row):
            rocks[(ix, iy)] = chr
    return rocks


def tilt(rocks, direction):

    def new_pos(dir, x, y):
        if dir == "N": return (x, y-1)
        if dir == "W": return (x-1, y)
        if dir == "S": return (x, y+1)
        if dir == "E": return (x+1, y)

    def ok_move(rocks, x, y):
        clear = (x, y) in rocks and rocks[(x, y)] == "."
        return clear

    any_stone_moved = True
    while any_stone_moved:
        any_stone_moved = False

        for (x, y), v in rocks.items():

            if v == "O":
                rocks[(x, y)] = "."  # assume the rock can be moved

                while True:
                    (nx, ny) = new_pos(direction, x, y)
                    if ok_move(rocks, nx, ny):
                        (x, y) = (nx, ny)
                        any_stone_moved = True
                    else:
                        break
                
                rocks[(x, y)] = "O"  # if the rock could NOT be moved (x, y) is unchanged

    return rocks


def spin(rocks, cycles):

    seen_formations = {}

    c = 0
    while c < cycles:
        c += 1

        for d in ["N", "W", "S", "E"]:
            rocks = tilt(rocks, d)

        seen = tuple(tuple(c) for c, v in rocks.items() if v == "O")

        if seen in seen_formations:
            cycle_length = c - seen_formations[seen]
            skip = (cycles - c) // cycle_length
            c += cycle_length * skip
        
        seen_formations[seen] = c

    return rocks


def sum_load(rocks):

    _, max_y = get_grid_dimensions(rocks)

    sum = 0
    for (_, y), v in rocks.items():
        if v == "O":
            sum += max_y - y
    
    return sum


def solution_1(input):
    rocks = parse(input)
    rocks = tilt(rocks, "N")
    return sum_load(rocks)


def solution_2(input):
    rocks = parse(input)
    rocks = spin(rocks, 10**9)
    return sum_load(rocks)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
