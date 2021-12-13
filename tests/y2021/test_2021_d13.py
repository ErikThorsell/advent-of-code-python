"""TEST MODULE"""
from advent_of_code.y2021.d13 import solution_1
from advent_of_code.y2021.d13 import solution_2
from advent_of_code.utils.parse import parse_folding


def test_solution_1():
    example_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
    example_result = 17
    assert solution_1(parse_folding(example_input)) == example_result
