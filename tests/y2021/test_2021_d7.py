"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d7 import solution_1
from advent_of_code.y2021.d7 import solution_2


def test_solution_1():
    example_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    example_result = 37
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    example_result = 168
    assert solution_2(example_input) == example_result
