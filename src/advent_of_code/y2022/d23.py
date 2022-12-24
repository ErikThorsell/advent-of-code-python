"""Solution module for Day 23, 2022"""
from collections import defaultdict
import copy
from dataclasses import dataclass
from operator import itemgetter
import time

from advent_of_code.utils.grid import get_adjacent
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


@dataclass
class Elf:
    id: int
    pos: tuple()
    prev_pos: tuple()
    dir: int


def draw_field(dictionary):
    x_min = min(dictionary.keys(), key=itemgetter(0))[0]
    y_min = min(dictionary.keys(), key=itemgetter(1))[1]
    x_max = max(dictionary.keys(), key=itemgetter(0))[0]
    y_max = max(dictionary.keys(), key=itemgetter(1))[1]
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in dictionary:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def count_field(dictionary):
    x_min = min(dictionary.keys(), key=itemgetter(0))[0]
    y_min = min(dictionary.keys(), key=itemgetter(1))[1]
    x_max = max(dictionary.keys(), key=itemgetter(0))[0]
    y_max = max(dictionary.keys(), key=itemgetter(1))[1]

    empty = 0

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) not in dictionary:
                empty += 1

    return empty


def parse(lines):
    field = dict()
    id = 0
    for rx, row in enumerate(lines):
        for cx, col in enumerate(row):
            if col == "#":
                id += 1
                e = Elf(id, (cx, rx), None, 0)
                field[(cx, rx)] = e
    return field


def move(elf, field):
    ex, ey = elf.pos

    if not any(ec in field for ec in get_adjacent(ex, ey, 8)):
        return (ex, ey), False

    norths = [(ex - 1, ey - 1), (ex, ey - 1), (ex + 1, ey - 1)]
    souths = [(ex - 1, ey + 1), (ex, ey + 1), (ex + 1, ey + 1)]
    wests = [(ex - 1, ey), (ex - 1, ey + 1), (ex - 1, ey - 1)]
    easts = [(ex + 1, ey), (ex + 1, ey + 1), (ex + 1, ey - 1)]

    dirs = [norths, souths, wests, easts]
    moves = [(ex, ey - 1), (ex, ey + 1), (ex - 1, ey), (ex + 1, ey)]

    for dir_idx in range(len(dirs)):
        if not any(ec in field for ec in dirs[(dir_idx + elf.dir) % len(dirs)]):
            return moves[(dir_idx + elf.dir) % len(dirs)], True

    return (ex, ey), False


def run_round(field):
    proposed_moves = defaultdict(list)

    moved = False

    # Everyone gets to propose
    for _, elf in field.items():
        new_pos, it_move = move(elf, field)
        moved = moved or it_move
        elf.prev_pos = elf.pos
        elf.pos = new_pos
        elf.dir += 1 % 4
        proposed_moves[elf.pos].append(elf)

    # Check who get to keep their choice
    new_field = dict()
    for _, elves in proposed_moves.items():
        if len(elves) > 1:
            for e in elves:
                e.pos = e.prev_pos
                new_field[e.pos] = e

        else:
            e = elves[0]
            new_field[e.pos] = e

    return new_field, moved


def solution_1(input):
    field = parse(input)

    for _ in range(10):
        field, _ = run_round(field)

    return count_field(field)


def solution_2(input):
    field = parse(input)
    moved = True

    iteration = 0
    while moved:
        field, moved = run_round(field)
        iteration += 1

    return iteration


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
