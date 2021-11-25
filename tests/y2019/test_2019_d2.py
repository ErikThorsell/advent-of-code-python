"""TEST MODULE DAY 2, 2019"""
from advent_of_code.utils.op import op, op_init
from advent_of_code.utils.parse import split_number_by_separator


def test_solution_1():
    example_input = [
        [1, 0, 0, 0, 99],
        [2, 3, 0, 3, 99],
        [2, 4, 4, 5, 99, 0],
        [1, 1, 1, 4, 99, 5, 6, 0, 99],
    ]
    example_result = [
        [2, 0, 0, 0, 99],
        [2, 3, 0, 6, 99],
        [2, 4, 4, 5, 99, 9801],
        [30, 1, 1, 4, 2, 5, 6, 0, 99],
    ]
    for i, _ in enumerate(example_input):
        assert op(example_input[i]) == example_result[i]
