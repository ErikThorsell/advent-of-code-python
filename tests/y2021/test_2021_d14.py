"""TEST MODULE TEMPLATE"""
from advent_of_code.y2021.d14 import solution_1
from advent_of_code.y2021.d14 import solution_2

from advent_of_code.utils.parse import parse_polymer


def test_solution_1():
    example_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
    example_result = 1588
    template, rules = parse_polymer(example_input)
    assert solution_1(template, rules) == example_result


def test_solution_2():
    example_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
    example_result = 2188189693529
    template, rules = parse_polymer(example_input)
    assert solution_2(template, rules) == example_result
