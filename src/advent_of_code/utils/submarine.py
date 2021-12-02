from typing import Tuple


def drive_sub(position: Tuple[int, int], command: Tuple[str, int]) -> Tuple[int, int]:
    if command[0] == "forward":
        return (position[0] + command[1], position[1])
    if command[0] == "down":
        return (position[0], position[1] + command[1])
    if command[0] == "up":
        return (position[0], position[1] - command[1])


def drive_sub_aim(position: Tuple[int, int], aim: int, command: Tuple[str, int]) -> Tuple[Tuple[int, int], int]:
    if command[0] == "forward":
        return (position[0] + command[1], position[1] + command[1] * aim), aim
    if command[0] == "down":
        aim += command[1]
        return position, aim
    if command[0] == "up":
        aim -= command[1]
        return position, aim
