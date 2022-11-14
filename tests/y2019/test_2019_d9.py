from advent_of_code.y2019.d9 import solution_1
from advent_of_code.y2019.d9 import solution_2


def test_solution_1():
    example_input = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    example_result = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = []
    example_result = []
    for i, _ in enumerate(example_input):
        assert solution_2(example_input[i]) == example_result[i]
