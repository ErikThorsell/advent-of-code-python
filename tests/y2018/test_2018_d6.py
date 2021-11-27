"""TEST MODULE TEMPLATE"""
from advent_of_code.y2018.d6 import solution_1
from advent_of_code.y2018.d6 import solution_2


def test_solution_1():
    example_input = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
    example_result = 17
    assert solution_1(example_input) == example_result
