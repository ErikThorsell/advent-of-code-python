"""TEST MODULE TEMPLATE"""
from advent_of_code.y2019.d3 import solution_1
from advent_of_code.y2019.d3 import solution_2


def test_solution_1():
    example_input = [
        [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]],
        [
            ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
            ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        ],
    ]
    example_result = [6, 159]
    for i, _ in enumerate(example_input):
        assert solution_1(example_input[i][0], example_input[i][1]) == example_result[i]


def test_solution_2():
    example_input = [
        [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]],
        [
            ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
            ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        ],
        [
            [
                "R98",
                "U47",
                "R26",
                "D63",
                "R33",
                "U87",
                "L62",
                "D20",
                "R33",
                "U53",
                "R51",
            ],
            ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
        ],
    ]
    example_result = [30, 610, 410]
    for i, _ in enumerate(example_input):
        assert solution_2(example_input[i][0], example_input[i][1]) == example_result[i]
