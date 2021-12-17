"""TEST MODULE"""
from advent_of_code.y2021.d17 import solution_1
from advent_of_code.y2021.d17 import solution_2


def test_solution_1():
    example_input = "target area: x=20..30, y=-10..-5"
    example_result = 45
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = "target area: x=20..30, y=-10..-5"
    example_result = 112
    assert solution_2(example_input) == example_result
