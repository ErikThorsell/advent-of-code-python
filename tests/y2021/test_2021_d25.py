"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d25 import solution_1

from advent_of_code.utils.parse import parse_sea_cucumbers


def test_solution_1_b():
    example_input = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""
    east, south = parse_sea_cucumbers(example_input)
    example_result = 4
    assert solution_1(east | south) == example_result


def test_solution_1():
    example_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
    east, south = parse_sea_cucumbers(example_input)
    example_result = 58
    assert solution_1(east | south) == example_result
