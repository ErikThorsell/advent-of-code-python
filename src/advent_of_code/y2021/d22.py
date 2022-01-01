"""Solution module for Day 22, 2021"""
import copy
from operator import countOf
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_cuboids


def solution_1(instructions):
    cubes = {}

    for on, (xs, ys, zs) in instructions:

        if any(v < -50 or v > 50 for v in xs + ys + zs):
            continue

        for x in range(xs[0], xs[1] + 1):
            for y in range(ys[0], ys[1] + 1):
                for z in range(zs[0], zs[1] + 1):
                    cubes[(x, y, z)] = on

    return countOf(cubes.values(), True)


# heavily inspired by a solution found on reddit
def subtract_overlap(ca, cb):
    def overlap(ca, cb):
        (x0a, x1a), (y0a, y1a), (z0a, z1a) = ca
        (x0b, x1b), (y0b, y1b), (z0b, z1b) = cb
        return x0b <= x1a and x1b >= x0a and y0b <= y1a and y1b >= y0a and z0b <= z1a and z1b >= z0a

    if overlap(ca, cb):
        (x0a, x1a), (y0a, y1a), (z0a, z1a) = ca
        (x0b, x1b), (y0b, y1b), (z0b, z1b) = cb

        x_overlap = list(zip((x0a, max(x0a, x0b), x1b + 1), (x0b - 1, min(x1a, x1b), x1a)))
        for xi, (x0, x1) in enumerate(x_overlap):
            if x0 > x1:
                continue

            y_overlap = list(zip((y0a, max(y0a, y0b), y1b + 1), (y0b - 1, min(y1a, y1b), y1a)))
            for yi, (y0, y1) in enumerate(y_overlap):
                if y0 > y1:
                    continue

                z_overlap = list(zip((z0a, max(z0a, z0b), z1b + 1), (z0b - 1, min(z1a, z1b), z1a)))
                for zi, (z0, z1) in enumerate(z_overlap):
                    if z0 > z1:
                        continue

                    if xi == 1 and yi == 1 and zi == 1:
                        continue

                    yield (x0, x1), (y0, y1), (z0, z1)
    else:
        yield ca


def cover_size(c):
    (x0, x1), (y0, y1), (z0, z1) = c
    return (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)


def solution_2(instructions):
    cuboids = list()

    for on, ca in instructions:
        sub_cuboids = list()

        for cb in cuboids:
            sub_cuboids += subtract_overlap(cb, ca)

        if on:
            sub_cuboids.append(ca)

        cuboids = sub_cuboids

    return sum(cover_size(c) for c in cuboids)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_cuboids(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
