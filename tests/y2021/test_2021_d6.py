"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d6 import solution_1
from advent_of_code.y2021.d6 import solution_2


def test_solution_1():
    example_input = [3, 4, 3, 1, 2]
    example_result = 5934
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = [3, 4, 3, 1, 2]
    example_result = 26984457539
    assert solution_2(example_input) == example_result
