"""Solution module for Day 6, 2024"""
import copy
from operator import itemgetter
import time
from sys import maxsize

from advent_of_code.utils.coordinates import draw_coordinates_dict, get_grid_dimensions_dict
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_mover_in_grid, split_str_by_newline


def test_1():
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    answer = 41
    assert(solution_1(input) == answer)
    

def test_2():
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    answer = 6
    assert(solution_2(input) == answer)


def step(grid, guard_pos, guard_dir):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    dx, dy = directions[guard_dir]
    next_pos = (guard_pos[0] + dx, guard_pos[1] + dy)

    if next_pos in grid:
        guard_dir = turn_right[guard_dir]
    else:
        guard_pos = next_pos
        
    return guard_pos, guard_dir


def solution_1(input):
    grid, guard_pos, guard_dir = parse_mover_in_grid(input)
    dims = get_grid_dimensions_dict(grid)

    path = set([guard_pos])

    while 0 <= guard_pos[0] < dims[0] and 0 <= guard_pos[1] < dims[1]:
        path.add(guard_pos)
        guard_pos, guard_dir = step(grid, guard_pos, guard_dir)
    return len(path)
    


def is_loopy(grid, guard_pos, guard_dir):
    dims = get_grid_dimensions_dict(grid)
    visited = set()

    while 0 <= guard_pos[0] < dims[0] and 0 <= guard_pos[1] < dims[1]:
        state = (guard_pos, guard_dir)
        if state in visited:
            return True
        visited.add(state)

        guard_pos, guard_dir = step(grid, guard_pos, guard_dir)

    return False


def solution_2(input):
    grid, guard_pos, guard_dir = parse_mover_in_grid(input)
    og_pos, og_dir = guard_pos, guard_dir
    dims = get_grid_dimensions_dict(grid)

    path = set([guard_pos])

    while 0 <= guard_pos[0] < dims[0] and 0 <= guard_pos[1] < dims[1]:
        path.add(guard_pos)
        guard_pos, guard_dir = step(grid, guard_pos, guard_dir)

    num_loops = 0

    for op in path:
        grid[op] = "#"

        if is_loopy(grid, og_pos, og_dir):
            num_loops += 1
        
        del grid[op]
    
    return num_loops


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
