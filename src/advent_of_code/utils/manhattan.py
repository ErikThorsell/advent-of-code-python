from typing import List, Tuple


def get_manhattan_distance(x, y: Tuple[int, int]) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def get_manhattan_distance_3d(x, y: Tuple[int, int]) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])
