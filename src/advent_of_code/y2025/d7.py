"""Solution module for Day 7, 2025"""
import copy
from functools import lru_cache
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    expected_answer = 21
    actual_answer = solution_1(input)
    assert expected_answer == actual_answer, (f"Expected: {expected_answer}, got {actual_answer}")

def test_2():
    input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    expected_answer = 40
    actual_answer = solution_2(input)
    assert expected_answer == actual_answer, (f"Expected: {expected_answer}, got {actual_answer}")


def parse(input):

    beams = set()
    splitters = []

    for r, row in enumerate(input.split("\n")):
        for c, col in enumerate(row):
            if col == "S":
                beams.add((c, r))
            if col == "^":
                splitters.append((c, r))

    return splitters, beams


def step(splitters, beams, manifold_length):

    new_beams = set()
    splits = 0
    for beam in beams:

        down = (beam[0], beam[1]+1)

        if down[1] > manifold_length:
            continue

        if down in splitters:
            splits += 1
            new_beams.add((beam[0]-1, beam[1]+1))
            new_beams.add((beam[0]+1, beam[1]+1))
        else:
            new_beams.add(down)

    return new_beams, splits


def solution_1(input):

    splitters, beams = parse(input)

    splits = 0
    while beams:
        beams, new_splits = step(splitters, beams, len(input.split("\n")))
        splits += new_splits

    return splits


def solution_2(input: str) -> int:
    splitters, beams = parse(input)

    height = len(input.split("\n"))
    width = len(input.split("\n")[0])

    (sx, sy), = beams

    @lru_cache(maxsize=None)
    def timelines(x, y):
        ny = y + 1
        down = (x, ny)

        # Fell out the bottom: one completed timeline
        if ny >= height:
            return 1

        # No splitter below: just keep falling
        if down not in splitters:
            return timelines(x, ny)

        # Hit a splitter: branch left and right from the splitter position
        total = 0
        total += timelines(x-1, ny)
        total += timelines(x+1, ny)

        return total

    return timelines(sx, sy)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    test_2()
    print("Test 2 was successful!")
    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")

