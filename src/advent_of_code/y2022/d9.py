"""Solution module for Day 9, 2022"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.coordinates import draw_coordinates
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.manhattan import get_manhattan_distance
from advent_of_code.utils.parse import split_str_by_newline


def move_tail(head, tp):
    dx = 0
    dy = 0
    x_dist = abs(head[0] - tp[0])
    y_dist = abs(head[1] - tp[1])

    if x_dist > 0 and y_dist > 0:
        dx = int((head[0]-tp[0])/x_dist)
        dy = int((head[1]-tp[1])/y_dist)

    elif x_dist > 0:
        dx = int((head[0]-tp[0])/x_dist)

    else:
        dy = int((head[1]-tp[1])/y_dist)

    return (tp[0]+dx, tp[1]+dy)


def tail_caught_up(head, tp):
    if get_manhattan_distance(head, tp) <= 1:
        return True
    if abs(head[0]-tp[0]) == abs(head[1]-tp[1]) == 1:
        return True
    return False


def move_knots(instruction, knots, visited):
    head = knots[0]
    d, n = instruction.split()

    # Move Head
    for _ in range(int(n)):
        match d :
            case "U":
                head = (head[0], head[1]+1)
            case "R":
                head = (head[0]+1, head[1])
            case "D":
                head = (head[0], head[1]-1)
            case "L":
                head = (head[0]-1, head[1])

        knots[0] = head
    
        # Follow with remaining knots
        for idx, _ in enumerate(knots[1:]):
            if not tail_caught_up(knots[idx], knots[idx+1]):
                knots[idx+1] = move_tail(knots[idx], knots[idx+1])
                visited.add(knots[-1])  # we're only interested in the last knot
        
    return knots, visited


def solution_1(input):

    knots = [(0, 0)] * 2
    visited = set()
    visited.add(knots[-1])

    for instr in input:
        knots, visited = move_knots(instr, knots, visited)

    return len(visited)
        

def solution_2(input):

    knots = [(0, 0)]*10
    visited = set()
    visited.add(knots[-1])

    for instr in input:
        knots, visited = move_knots(instr, knots, visited)
    return len(visited)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
