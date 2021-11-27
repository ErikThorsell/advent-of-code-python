from typing import Tuple


def get_manhattan_distance(x, y: Tuple[int, int]) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])
