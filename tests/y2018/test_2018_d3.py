"""TEST MODULE TEMPLATE"""
from advent_of_code.utils.parse import parse_fabric_claims
from advent_of_code.y2018.d3 import solution_1
from advent_of_code.y2018.d3 import solution_2


def test_solution_1():
    example_input = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    example_result = 4
    assert solution_1(parse_fabric_claims(example_input)) == example_result


def test_solution_2():
    example_input = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    example_result = 3
    assert solution_2(parse_fabric_claims(example_input)) == example_result
