"""TEST MODULE"""
from advent_of_code.y2021.d12 import solution_1
from advent_of_code.y2021.d12 import solution_2
from advent_of_code.utils.parse import split_str_by_newline


def test_solution_1():
    example_input = [
        """start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
        """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
        """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""",
    ]
    example_result = [10, 19, 226]
    for i, _ in enumerate(example_input):
        parsed_input = split_str_by_newline(example_input[i])
        assert solution_1(parsed_input) == example_result[i]


def test_solution_2():
    example_input = [
        """start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
        """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
        """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""",
    ]
    example_result = [36, 103, 3509]
    for i, _ in enumerate(example_input):
        parsed_input = split_str_by_newline(example_input[i])
        assert solution_2(parsed_input) == example_result[i]
