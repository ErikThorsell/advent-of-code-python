"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d1 import solution_1
from advent_of_code.y2021.d1 import solution_2


def test_solution_1():
    example_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    example_result = 7
    assert solution_1(example_input) == example_result


def test_solution_1():
    example_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    example_result = 5
    assert solution_2(example_input) == example_result
