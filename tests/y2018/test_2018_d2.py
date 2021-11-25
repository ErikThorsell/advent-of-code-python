"""TEST MODULE TEMPLATE"""
from advent_of_code.y2018.d2 import solution_1
from advent_of_code.y2018.d2 import solution_2


def test_solution_1():
    example_input = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]
    example_result = 12
    assert solution_1(example_input) == example_result


def test_solution_2():
    example_input = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    example_result = "fgij"
    assert solution_2(example_input) == example_result
