"""Solution module for Day 3, 2017"""
import copy
from math import ceil, sqrt
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    # Copy paste example here
    input = """1024"""
    answer = 31
    assert(solution_1(input) == answer)
    

def solution_1(input):
    # We can calculate the minimum number of steps required to reach any number
    # in a specific ring using the formula below.
    ring = ceil((sqrt(int(input))-1)/2)

    # Find the largest number in the ring
    maximum = (2*ring +1)**2

    # Midpoints are always the closest to 1
    # Subtracting 2r each time moves us counter-clockwise to the midpoints of the other sides.
    midpoints = [maximum - ring - 2*i*ring for i in range(4)]

    # We need to take "ring" steps to get to the correct ring (horisontally or vertically)
    # and then we walk the "other direction" until we get to the midpoint
    return ring + min([abs(int(input)-mid) for mid in midpoints])


def solution_2(input):

    def calculate_adjacent_sum(x, y, grid):
        total = 0
        adjacent = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
        for dx, dy in adjacent:
            neighbor_pos = (x + dx, y + dy)
            if neighbor_pos in grid:
                total += grid[neighbor_pos]
        return total

    grid = {}
    x, y = 0, 0
    grid[(x, y)] = 1

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 0  # Start moving right

    steps_in_current_direction = 1
    steps_taken = 0
    direction_changes = 0 

    while True:
        dx, dy = directions[direction_index]
        x += dx
        y += dy
        steps_taken += 1

        value = calculate_adjacent_sum(x, y, grid)
        grid[(x, y)] = value

        if value > int(input):
            return value

        if steps_taken == steps_in_current_direction:
            steps_taken = 0
            direction_index = (direction_index + 1) % 4
            direction_changes += 1
            if direction_changes % 2 == 0:
                steps_in_current_direction += 1


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
