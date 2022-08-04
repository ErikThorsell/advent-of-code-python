from advent_of_code.utils.parse import split_str_by_newline
from advent_of_code.y2019.d6 import solution_1
from advent_of_code.y2019.d6 import solution_2


def test_solution_1():
    example_input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
    parsed_input = split_str_by_newline(example_input)
    dag = solution_1(parsed_input)
    print(dag)


def test_solution_2():
    example_input = []
    example_result = []
    for i, _ in enumerate(example_input):
        assert solution_2(example_input[i]) == example_result[i]
