"""TEST MODULE TEMPLATE"""
from advent_of_code.utils.parse import split_number_by_separator

from advent_of_code.y2018.d8 import solution_1
from advent_of_code.y2018.d8 import solution_2


def test_solution_1():
    example_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    example_result = 138
    assert solution_1(split_number_by_separator(example_input, " ")) == example_result


def test_solution_2():
    example_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    example_result = 66
    assert solution_2(split_number_by_separator(example_input, " ")) == example_result
