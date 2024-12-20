from operator import itemgetter
from typing import List, Tuple


def get_min_max_velocity(velocities: List[Tuple[int, int]]) -> Tuple[int, int]:
    print(f"{velocities=}")
    min_x = min(velocities, key=itemgetter(0))[0]
    max_x = max(velocities, key=itemgetter(0))[0]
    min_y = min(velocities, key=itemgetter(1))[1]
    max_y = max(velocities, key=itemgetter(1))[1]
    return min_x, max_x, min_y, max_y


def get_rectangle_in_grid(top_left_coordinate, width_and_height: Tuple[int, int]) -> List[Tuple[int, int]]:
    pass


def get_coordinates(vectors: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> List[Tuple[int, int]]:
    return [p for (p, v) in vectors]


def get_velocities(vectors: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> List[Tuple[int, int]]:
    return [v for (p, v) in vectors]


def line_is_diagonal(c1, c2: Tuple[int, int]) -> bool:
    if c1[0] == c2[0] or c1[1] == c2[1]:
        return False
    return True


def _get_coordinates_between_hor_ver(c1, c2: Tuple[int, int]) -> List[Tuple[int, int]]:
    dx = 1 if c2[0] >= c1[0] else -1
    dy = 1 if c2[1] >= c1[1] else -1
    return [(x, y) for x in range(c1[0], c2[0] + dx, dx) for y in range(c1[1], c2[1] + dy, dy)]


def get_coordinates_between(c1, c2: Tuple[int, int]) -> List[Tuple[int, int]]:
    if line_is_diagonal(c1, c2):
        dx = 1 if c2[0] >= c1[0] else -1
        dy = 1 if c2[1] >= c1[1] else -1
        return [(x + dx, y + dy) for (x, y) in zip(range(c1[0] - dx, c2[0], dx), range(c1[1] - dy, c2[1], dy))]
    return _get_coordinates_between_hor_ver(c1, c2)


def move_coordinates(
    coordinates: List[Tuple[Tuple[int, int], Tuple[int, int]]], backwards=False
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    new_coordinates = list()
    for c, v in coordinates:
        if backwards:
            nx = c[0] - v[0]
            ny = c[1] - v[1]
        else:
            nx = c[0] + v[0]
            ny = c[1] + v[1]
        new_coordinates.append(((nx, ny), (v[0], v[1])))
    return new_coordinates


def get_grid_dimensions(coordinates: List[Tuple[int, int]], verbose=False) -> Tuple[int, int]:
    x_min = min(coordinates, key=itemgetter(0))[0]
    y_min = min(coordinates, key=itemgetter(1))[1]
    x_max = max(coordinates, key=itemgetter(0))[0]
    y_max = max(coordinates, key=itemgetter(1))[1]
    width = x_max - x_min + 1
    height = y_max - y_min + 1
    return width, height


def draw_coordinates(coordinates: List[Tuple[int, int]]) -> None:
    x_min = min(coordinates, key=itemgetter(0))[0]
    y_min = min(coordinates, key=itemgetter(1))[1]
    x_max = max(coordinates, key=itemgetter(0))[0]
    y_max = max(coordinates, key=itemgetter(1))[1]
    print()
    for y in range(y_min, y_max + 1):  # loop y first to get same output as AoC
        for x in range(x_min, x_max + 1):
            if (x, y) in coordinates:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def draw_coordinates_dict(dictionary, empty="."):
    x_min = min(dictionary.keys(), key=itemgetter(0))[0]
    y_min = min(dictionary.keys(), key=itemgetter(1))[1]
    x_max = max(dictionary.keys(), key=itemgetter(0))[0]
    y_max = max(dictionary.keys(), key=itemgetter(1))[1]
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in dictionary:
                print(dictionary[(x, y)], end="")
            else:
                print(empty, end="")
        print()
    print()


def get_grid_dimensions_dict(dictionary) -> Tuple[int, int]:
    x_min = min(dictionary.keys(), key=itemgetter(0))[0]
    y_min = min(dictionary.keys(), key=itemgetter(1))[1]
    x_max = max(dictionary.keys(), key=itemgetter(0))[0]
    y_max = max(dictionary.keys(), key=itemgetter(1))[1]
    width = x_max - x_min + 1
    height = y_max - y_min + 1
    return width, height


def coordinates_dict_to_string(dictionary, empty="."):
    x_min = min(dictionary.keys(), key=itemgetter(0))[0]
    y_min = min(dictionary.keys(), key=itemgetter(1))[1]
    x_max = max(dictionary.keys(), key=itemgetter(0))[0]
    y_max = max(dictionary.keys(), key=itemgetter(1))[1]
    result = ""
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in dictionary:
                result += dictionary[(x, y)]
            else:
                result += empty
        result += "\n"
    return result


def fold_grid(coordinates: List[Tuple[int, int]], instruction: str) -> List[Tuple[int, int]]:
    instruction = instruction.split()[-1]
    direction, coordinate = instruction.split("=")
    coordinate = int(coordinate)

    folded = list()
    if direction == "x":
        for (x, y) in coordinates:
            if x < coordinate:
                folded.append((x, y))
            elif x == coordinate:
                continue
            else:
                folded.append((coordinate + coordinate - x, y))

    elif direction == "y":
        for (x, y) in coordinates:
            if y < coordinate:
                folded.append((x, y))
            elif y == coordinate:
                continue
            else:
                folded.append((x, coordinate + coordinate - y))

    else:
        raise ValueError(f"Invalid folding direction: {direction=}")

    return list(set(folded))


def rotate_3d(point, rotation):
    x, y, z = point
    if rotation == 0:
        return (x, y, z)
    if rotation == 1:
        return (x, -z, y)
    if rotation == 2:
        return (x, -y, -z)
    if rotation == 3:
        return (x, z, -y)
    if rotation == 4:
        return (-x, -y, z)
    if rotation == 5:
        return (-x, -z, -y)
    if rotation == 6:
        return (-x, y, -z)
    if rotation == 7:
        return (-x, z, y)
    if rotation == 8:
        return (y, x, -z)
    if rotation == 9:
        return (y, -x, z)
    if rotation == 10:
        return (y, z, x)
    if rotation == 11:
        return (y, -z, -x)
    if rotation == 12:
        return (-y, x, z)
    if rotation == 13:
        return (-y, -x, -z)
    if rotation == 14:
        return (-y, -z, x)
    if rotation == 15:
        return (-y, z, -x)
    if rotation == 16:
        return (z, x, y)
    if rotation == 17:
        return (z, -x, -y)
    if rotation == 18:
        return (z, -y, x)
    if rotation == 19:
        return (z, y, -x)
    if rotation == 20:
        return (-z, x, -y)
    if rotation == 21:
        return (-z, -x, y)
    if rotation == 22:
        return (-z, y, x)
    if rotation == 23:
        return (-z, -y, -x)
