"""TEST MODULE TEMPLATE"""
from advent_of_code.y2018.d9 import solution_1
from advent_of_code.y2018.d9 import solution_2


def test_solution_1():
    example_input = [
        (9, 25),
        (10, 1618),
        (13, 7999),
        (17, 1104),
        (21, 6111),
        (30, 5807),
    ]
    example_result = [32, 8317, 146373, 2764, 54718, 37305]
    for i, _ in enumerate(example_input):
        assert solution_1(example_input[i][0], example_input[i][1]) == example_result[i]
