"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d5 import solution_1
from advent_of_code.y2021.d5 import solution_2

from advent_of_code.utils.parse import parse_coordinates, parse_line_segments


def test_solution_1():
    example_input = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""
    example_result = 5
    assert solution_1(parse_line_segments(example_input)) == example_result


def test_solution_2():
    example_input = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""
    example_result = 12
    assert solution_2(parse_line_segments(example_input)) == example_result
