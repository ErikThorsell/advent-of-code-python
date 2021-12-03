"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d3 import solution_1
from advent_of_code.y2021.d3 import solution_2

from advent_of_code.utils.parse import split_str_by_newline


def test_solution_1():
    example_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    example_result = 198
    assert solution_1(split_str_by_newline(example_input)) == example_result


def test_solution_2():
    example_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    example_result = 230
    assert solution_2(split_str_by_newline(example_input)) == example_result
