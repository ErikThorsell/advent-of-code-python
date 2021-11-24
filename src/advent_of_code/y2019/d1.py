from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_by_newline


def calc(mass: int) -> int:
    return mass // 3 - 2


def solution_1(input):
    return sum([calc(i) for i in input])


def solution_2(input):
    sum = 0
    for i in input:
        mass = calc(i)
        while mass > 0:
            sum += mass
            mass = calc(mass)
    return sum


def run():
    print(f"Fetching input!")
    parsed_input = split_by_newline(fetch(2019, 1))
    print(f"Solution for problem 1: {solution_1(parsed_input)}")
    print(f"Solution for problem 2: {solution_2(parsed_input)}")
