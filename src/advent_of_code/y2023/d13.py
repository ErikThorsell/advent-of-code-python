"""Solution module for Day 13, 2023"""
import copy
import time

from advent_of_code.utils.coordinates import get_grid_dimensions
from advent_of_code.utils.fetch import fetch


def test_1():
    input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
    assert(solution_1(input) == 405)

def test_2():
    input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
    assert(solution_2(input) == 400)


def parse(input):
    fields = []
    for unparsed in input.split("\n\n"):
        field = {}
        for iy, row in enumerate(unparsed.split("\n")):
            for ix, chr in enumerate(row):
                field[(ix, iy)] = chr
        fields.append(field)
    return fields


def find_reflection(field):

    max_x, max_y = get_grid_dimensions(field)

    vertical = []
    for line in range(1, max_x):

        left, right = [], []
        for idx in range(line-1, -1, -1):
            left.extend([field[(x, y)] for (x, y) in field if x == idx])
        for idx in range(line, max_x):
            right.extend([field[(x, y)] for (x, y) in field if x == idx])

        n = min(len(left), len(right))
        if left[:n] == right[:n]:
            vertical.append(line)

    horisontal = []
    for line in range(1, max_y):

        top, bottom = [], []
        for idx in range(line-1, -1, -1):
            top.extend([field[(x, y)] for (x, y) in field if y == idx])
        for idx in range(line, max_y):
            bottom.extend([field[(x, y)] for (x, y) in field if y == idx])

        n = min(len(top), len(bottom))
        if top[:n] == bottom[:n]:
            horisontal.append(line)
    
    return vertical, horisontal


def solution_1(input):

    fields = parse(input)

    answer = 0
    for field in fields:
        vertical, horisontal = find_reflection(field)

        if len(vertical) == 1:
            answer += vertical[0]
        else:
            answer += horisontal[0] * 100
        
    return answer


def smudgify(field):

    orig_vert, orig_horis = find_reflection(field)

    for c, v in field.items():
        if v == ".":
            field[c] = "#"
        else:
            field[c] = "."

        vert, horis = find_reflection(field)
        vert = set(vert) - set(orig_vert)
        horis = set(horis) - set(orig_horis)

        if len(vert) + len(horis) == 1:
            return vert, horis

        field[c] = v  # reset so we can continue


def solution_2(input):

    fields = parse(input)

    answer = 0
    for field in fields:
        vertical, horisontal = smudgify(field)

        if len(vertical) == 1:
            answer += vertical.pop()
        else:
            answer += horisontal.pop() * 100
        
    return answer


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
