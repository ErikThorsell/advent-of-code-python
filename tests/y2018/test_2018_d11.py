"""TEST MODULE TEMPLATE"""
from advent_of_code.y2018.d11 import solution_1
from advent_of_code.y2018.d11 import solution_2
from advent_of_code.y2018.d11 import compute_power_level_for_fuel_cell


def test_find_power_level_for_fuel_cell():
    example_input = [
        (3, 5, 8),
        (122, 79, 57),
        (217, 196, 39),
        (101, 153, 71),
    ]
    example_result = [4, -5, 0, 4]
    for i, _ in enumerate(example_input):
        x = example_input[i][0]
        y = example_input[i][1]
        sgn = example_input[i][2]
        assert compute_power_level_for_fuel_cell(x, y, sgn) == example_result[i]


def test_solution_1():
    example_input = [18, 42]
    example_result = [(33, 45), (21, 61)]
    for i, _ in enumerate(example_input):
        assert solution_1(example_input[i]) == example_result[i]


def test_solution_2():
    example_input = [18, 42]
    example_result = [(90, 269, 16), (232, 251, 12)]
    for i, _ in enumerate(example_input):
        assert solution_2(example_input[i]) == example_result[i]
