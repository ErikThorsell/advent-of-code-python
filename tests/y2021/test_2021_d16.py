"""TEST MODULE"""
from advent_of_code.y2021.d16 import solution


def test_solution_1():
    example_input = [
        "8A004A801A8002F478",
        "620080001611562C8802118E34",
        "C0015000016115A2E0802F182340",
        "A0016C880162017C3686B18A3D4780",
    ]
    example_result = [16, 12, 23, 31]
    for i, _ in enumerate(example_input):
        assert solution(example_input[i])[0] == example_result[i]
