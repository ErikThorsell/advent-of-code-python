"""Solution module for Day 10, 2023"""
from collections import Counter
import copy
import re
import time

from advent_of_code.utils.coordinates import get_grid_dimensions, draw_coordinates_dict
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import get_adjacent


def parse(input):

    diagram = {}

    for y, row in enumerate(input.split("\n")):
        for x, chr in enumerate(row):
            diagram[(x,y)] = chr

    start = list(diagram.keys())[list(diagram.values()).index("S")]

    return diagram, start


def find_loop(diagram, start):

    visited = set()
    next = [start]

    steps = 1  # break ties
    while next:
        steps += 1
        current, next = next[0], next[1:]

        for pn in get_possible_neighbors(diagram, current):
            if pn not in visited:
                next.append(pn)

        visited.add(current)

    return visited


def get_possible_neighbors(diagram, coordinate):

    pipe = diagram[coordinate]
    x, y = coordinate

    if pipe == "|": return [(x, y-1), (x, y+1)]
    elif pipe == "-": return [(x-1, y),(x+1, y)]
    elif pipe == "L": return [(x, y-1),(x+1, y)]
    elif pipe == "J": return [(x-1, y),(x, y-1)]
    elif pipe == "7": return [(x-1, y),(x, y+1)]
    elif pipe == "F": return [(x+1, y),(x, y+1)]
    else: raise


def replace_start(diagram, start):

    x, y = start

    actual_neighbors = []
    for (ix, iy) in get_adjacent(x, y, 4):
        if (ix, iy) in diagram and diagram[(ix, iy)] != ".":
            if start in get_possible_neighbors(diagram, (ix, iy)):
                actual_neighbors.append((ix, iy))

    for p in "|-LJ7F":
        diagram[start] = p
        if Counter(get_possible_neighbors(diagram, start)) == Counter(actual_neighbors):
            break
        
    return diagram


def solution_1(input):
    diagram, start = parse(input)
    diagram = replace_start(diagram, start)
    loop = find_loop(diagram, start)
    return len(loop)//2


def solution_2(input):

    diagram, start = parse(input)
    diagram = replace_start(diagram, start)
    dimensions = get_grid_dimensions(diagram.keys())
    loop = find_loop(diagram, start)

    VERTICAL = ['FJ', 'L7', '|']
    SECTION_START = 'FL'
    SECTION_END = 'J7|'

    inside = 0
    for y in range(dimensions[1]):
        is_inside = False
        current = ''
        for x in range(dimensions[0]):
            if (x,y) in loop:
                p = diagram[(x,y)]
                if p in SECTION_START:
                    current = p
                elif p in SECTION_END:
                    current += p
                    if current in VERTICAL:
                        is_inside = not is_inside
                    current = ''
            else:
                if is_inside:
                    inside += 1
        
    return inside 


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
