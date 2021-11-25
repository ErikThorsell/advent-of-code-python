"""TEST MODULE TEMPLATE"""
from advent_of_code.y2018.d1 import solution_1
from advent_of_code.y2018.d1 import solution_2


def test_solution_1():
    example_input = [
        [1, -2, 3, 1],
        [1, 1, 1],
        [1, 1, -2],
    ]
    example_result = [3, 3, 0]
    for i, _ in enumerate(example_input):
        assert solution_1(example_input[i]) == example_result[i]


def test_solution_2():
    example_input = [
        [+1, -1],
        [+3, +3, +4, -2, -4],
        [+7, +7, -2, -7, -4],
    ]
    example_result = [0, 10, 14]
    for i, _ in enumerate(example_input):
        assert solution_2(example_input[i]) == example_result[i]
