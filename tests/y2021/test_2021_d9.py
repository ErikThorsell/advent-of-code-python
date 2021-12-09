"""TEST MODULE"""
from advent_of_code.y2021.d9 import solution_1
from advent_of_code.y2021.d9 import solution_2

from advent_of_code.utils.parse import parse_each_digit


def test_solution_1():
    example_input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""
    example_result = 15
    assert solution_1(parse_each_digit(example_input)) == example_result


def test_solution_2():
    example_input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""
    example_result = 1134
    assert solution_2(parse_each_digit(example_input)) == example_result
