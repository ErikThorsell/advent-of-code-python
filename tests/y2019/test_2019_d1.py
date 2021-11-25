"""TEST MODULE DAY 1, 2019"""
from advent_of_code.y2019.d1 import solution_1
from advent_of_code.y2019.d1 import solution_2


def test_solution_1():
    example_input = [[12], [14], [1969], [100756]]
    example_result = [2, 2, 654, 33583]
    for i, _ in enumerate(example_input):
        assert solution_1(example_input[i]) == example_result[i]


def test_solution_2():
    example_input = [[14], [1969], [100756]]
    example_result = [2, 966, 50346]
    for i, _ in enumerate(example_input):
        assert solution_2(example_input[i]) == example_result[i]
