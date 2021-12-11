"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d11 import solution_1
from advent_of_code.y2021.d11 import solution_2

from advent_of_code.utils.parse import parse_grid


def test_solution_1():
    example_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
    example_result = 1656
    assert solution_1(parse_grid(example_input)) == example_result


def test_solution_2():
    example_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
    example_result = 195
    assert solution_2(parse_grid(example_input)) == example_result
