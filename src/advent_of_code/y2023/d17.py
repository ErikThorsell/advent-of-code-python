"""Solution module for Day 17, 2023"""
import copy
from heapq import heappop, heappush
import time
from sys import maxsize

from advent_of_code.utils.coordinates import get_grid_dimensions
from advent_of_code.utils.fetch import fetch


def test_1():
    input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
    answer = 102
    assert(solution_1(input) == answer)
    

def test_2():
    input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
    answer = 94
    assert(solution_2(input) == answer)


def test_3():
    input = """111111111111
999999999991
999999999991
999999999991
999999999991"""
    answer = 71
    assert(solution_2(input) == answer)


def parse(input):
    cave = {}
    for iy, row in enumerate(input.split("\n")):
        for ix, chr in enumerate(row):
            cave[(ix, iy)] = int(chr)
    return cave


def minimize(traffic_map, start, goal, min_dist, max_dist):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(*start, 0, -1)]
    heat_map = {}

    while queue:

        heat, x, y, current_dir = heappop(queue)

        if (x, y) == goal:
            return heat

        for turn in range(4):

            heat_increase = 0

            if turn == current_dir or (turn + 2) % 4 == current_dir:
                continue

            for distance in range(1, max_dist+1):

                nx = x + directions[turn][0] * distance
                ny = y + directions[turn][1] * distance
                new_state = (nx, ny, turn)

                if (nx, ny) in traffic_map:
                    heat_increase += traffic_map[(nx, ny)]
                    new_heat = heat + heat_increase

                    if distance < min_dist:
                        continue

                    if heat_map.get(new_state, maxsize) <= new_heat:
                        continue

                    heat_map[new_state] = new_heat
                    heappush(queue, (new_heat, *new_state))


def solution_1(input):
    traffic_map = parse(input)
    max_x, max_y = get_grid_dimensions(traffic_map)

    start = (0, 0)
    goal = (max_x-1, max_y-1)

    res = minimize(traffic_map, start, goal, 1, 3)

    return res


def solution_2(input):
    traffic_map = parse(input)
    max_x, max_y = get_grid_dimensions(traffic_map)

    start = (0, 0)
    goal = (max_x-1, max_y-1)

    res = minimize(traffic_map, start, goal, 4, 10)

    return res


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")
    test_3()
    print("Test 3 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
