"""TEST MODULE TEMPLATE"""
from advent_of_code.y2018.d5 import solution_1
from advent_of_code.y2018.d5 import solution_2


def test_solution_1():
    example_input = "dabAcCaCBAcCcaDA"
    example_result = 10
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = "dabAcCaCBAcCcaDA"
    example_result = 4
    assert solution_2(example_input) == example_result
