"""TEST MODULE TEMPLATE"""
from advent_of_code.utils.parse import parse_graph_edges
from advent_of_code.y2018.d7 import solution_1
from advent_of_code.y2018.d7 import solution_2


def test_solution_1():
    example_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
    example_result = "CABDFE"
    assert solution_1(parse_graph_edges(example_input)) == example_result


def test_solution_2():
    example_input = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
    example_result = 15
    assert solution_2(parse_graph_edges(example_input), 2, 0) == example_result
