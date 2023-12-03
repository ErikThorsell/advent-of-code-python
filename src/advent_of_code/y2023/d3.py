"""Solution module for Day 3, 2023"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.grid import get_adjacent


def parse(input):

    schematic = {}   # map coordinate to parsed number (i.e. (0,0) -> 467, (1, 0) -> 467, ...)
    indices = {}     # map each value to an index      (i.e. (0,0) -> 1,   (1, 0) -> 1, ...)
    characters = []  # list used to parse 4, 6, 7 into 467
    positions = []   # keep track of coordinates while parsing characters

    idx = 1
    for y, row in enumerate(input.split("\n")):
        for x, chr in enumerate(row):
            if chr.isdigit():
                characters.append(chr)
                positions.append((x,y))
            else:
                if characters and positions:
                    c = ''.join(characters)
                    for p in positions:
                        schematic[p] = c
                        indices[p] = idx
                    idx += 1
                    characters = []
                    positions = []
                if chr != '.':
                    schematic[(x, y)] = chr

    return schematic, indices


def solution_1(input):

    schematic, idxs = parse(input)

    numbers = []
    used = []
    for (x, y) in schematic:
        for (ax, ay) in get_adjacent(x, y, 8):
            if (ax, ay) in schematic:
                if (x, y) in idxs and idxs[(x, y)] not in used:
                    if not schematic[(ax, ay)].isdigit():
                        numbers.append(int(schematic[(x, y)]))
                        used.append(idxs[(x,y)])
    
    return sum(numbers)


def solution_2(input):

    schematic, idxs = parse(input)

    ratios = []
    used_idxs = []
    for (x, y) in schematic:
        if schematic[(x, y)] == "*":

            numbers = []
            adjacent = get_adjacent(x, y, 8)
            for (ax, ay) in adjacent:
                if (ax, ay) in schematic and schematic[(ax,ay)].isdigit():
                    idx = idxs[(ax, ay)]
                    numbers.append(((ax, ay), schematic[(ax, ay)], idx))
            
            # Remove duplicate indices
            seen = set()
            numbers = [seen.add(t[-1]) or t for t in numbers if t[-1] not in seen]

            if len(numbers) > 1:
                ratio = 1
                for (_, n, i) in numbers:
                    if i not in used_idxs:
                        ratio *= int(n)
                ratios.append(ratio)
    
    return sum(ratios)


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
