"""Solution module for Day 13, 2024"""
import copy
import time
from sys import maxsize

import z3

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    answer = 480
    assert(solution_1(input) == answer)
    

def parse(input):
    runs = []
    for run in input.split("\n\n"):
        lines = run.split("\n")
        ax, ay = map(int, lines[0].split("X+")[1].split(", Y+"))
        bx, by = map(int, lines[1].split("X+")[1].split(", Y+"))
        px, py = map(int, lines[2].split("X=")[1].split(", Y="))
        runs.append({"ax": ax, "ay": ay, "bx": bx, "by": by, "px": px, "py": py})
    return runs


def solution_1(input):
    runs = parse(input)

    results = []
    for run in runs:
        ax, ay, bx, by, px, py = run.values()
        min_cost = maxsize
        best_x, best_y = None, None

        for x in range(100):
            for y in range(100):
                if x*ax + y*bx == px and x*ay + y*by == py:
                    cost = 3*x + y
                    if cost < min_cost:
                        min_cost = cost
                        best_x, best_y = x, y
        
        if best_x is not None and best_y is not None:
            results.append(min_cost)

    return sum(results)


def solution_2(input):
    runs = parse(input)

    result = 0
    for run in runs:
        run["px"] += 10**13
        run["py"] += 10**13

        ax, ay, bx, by, px, py = run.values()

        solver = z3.Solver()
        a, b = z3.Ints("a b")
        solver.add(ax * a + bx * b == px)
        solver.add(ay * a + by * b == py)
        
        if solver.check() == z3.sat:
            result += solver.model()[a].as_long() * 3 + solver.model()[b].as_long()

    return result


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
