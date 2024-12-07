"""Solution module for Day 7, 2024"""
import copy
from itertools import product
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    answer = 3749
    assert(solution_1(input) == answer)
    

def test_2():
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    answer = 11387
    assert(solution_2(input) == answer)


def parse(input):
    for equation in input.split("\n"):
        ans = int(equation.split(":")[0])
        terms = list(map(int, equation.split(":")[1].split()))
        yield ans, terms


def find_valid(ans, terms, operators):
    if len(terms) == 1:
        return terms[0] == ans

    for ops in product(operators, repeat=len(terms)-1):

        result = terms[0]
        for op, num in zip(ops, terms[1:]):
            if op == "+":
                result = result + num
            elif op == "*":
                result = result * num
            else:
                result = int(str(result)+str(num))

        if ans == result:
            return True
    
    return False


def solution_1(input):
    total = 0
    for ans, terms in parse(input):
        if find_valid(ans, terms, ["+", "*"]):
            total += ans
    return total


def solution_2(input):
    total = 0
    for ans, terms in parse(input):
        if find_valid(ans, terms, ["+", "*", "||"]):
            total += ans
    return total


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
