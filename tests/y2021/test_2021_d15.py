"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d15 import solution_1
from advent_of_code.y2021.d15 import solution_2

from advent_of_code.utils.parse import parse_grid


def test_solution_1():
    example_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
    example_result = 40
    assert solution_1(parse_grid(example_input)) == example_result


def test_solution_2():
    example_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
    example_result = 315
    assert solution_2(parse_grid(example_input)) == example_result
