"""Solution module for Day 8, 2025"""
import copy
from math import prod
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    expected_answer = 40
    actual_answer = solution_1(input, 10)
    assert expected_answer == actual_answer, (f"Expected: {expected_answer}, got {actual_answer}")

def test_2():
    input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    expected_answer = 25272
    actual_answer = solution_2(input)
    assert expected_answer == actual_answer, (f"Expected: {expected_answer}, got {actual_answer}")


def parse_points(input):
    points = []
    for line in input.split("\n"):
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))
    return points


def solution_1(input, num_pairs=1000):
    points = parse_points(input)
    n = len(points)

    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            pairs.append((d2, i, j))

    pairs.sort(key=lambda t: t[0])

    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return

        if size[ra] < size[rb]:
            ra, rb = rb, ra

        parent[rb] = ra
        size[ra] += size[rb]

    for _, i, j in pairs[:num_pairs]:
        union(i, j)

    comp_size = {}
    for i in range(n):
        r = find(i)
        comp_size[r] = comp_size.get(r, 0) + 1

    return prod(sorted(comp_size.values(), reverse=True)[:3])


def solution_2(input):
    points = parse_points(input)
    n = len(points)

    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            pairs.append((d2, i, j))

    pairs.sort(key=lambda t: t[0])

    parent = list(range(n))
    size = [1] * n
    components = n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        nonlocal components
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False

        if size[ra] < size[rb]:
            ra, rb = rb, ra

        parent[rb] = ra
        size[ra] += size[rb]
        components -= 1
        return True

    last_pair = (-1, -1)
    for _, i, j in pairs:
        if union(i, j):
            last_pair = (i, j)
            if components == 1:
                break

    x1, _, _ = points[last_pair[0]]
    x2, _, _ = points[last_pair[1]]
    return x1 * x2


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

