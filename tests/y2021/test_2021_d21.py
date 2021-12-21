"""TEST MODULE"""
from advent_of_code.y2021.d21 import solution_1
from advent_of_code.y2021.d21 import solution_2


def test_solution_1():
    example_input = [4, 8]
    example_result = 739785
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = [4, 8]
    example_result = 444356092776315
    assert solution_2(example_input) == example_result
