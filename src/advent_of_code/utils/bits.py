from math import prod
from typing import List, Tuple

import advent_of_code.utils.globals


def hex_to_bin(hex: str) -> str:
    binary = ""
    for d in hex:
        binary += format(int(d, 16), "04b")
    return binary


def compute_bits(binary_str: str) -> Tuple[int, str]:
    # Account for header
    version = int(binary_str[:3], 2)
    type_id = int(binary_str[3:6], 2)

    # Remainder of packet
    rbs = binary_str[6:]

    # Keep global sum of versions
    # Must exist a better way to handle this?
    advent_of_code.utils.globals.d16_version_sum += version

    if type_id == 4:
        value, rbs = compute_literal(rbs)
    else:
        length_type_id = int(rbs[0], 2)
        rbs = rbs[1:]

        if length_type_id == 0:
            value, rbs = compute_mode_0(type_id, rbs)

        elif length_type_id == 1:
            value, rbs = compute_mode_1(type_id, rbs)

    return value, rbs


def compute_literal(binary_str: str) -> Tuple[int, str]:
    literal = ""
    while True:
        group = binary_str[:5]
        indicator = group[0]
        literal += group[1:]
        binary_str = binary_str[5:]
        if indicator == "0":
            break
    return int(literal, 2), binary_str


def compute_mode_0(type_id: int, binary_str: str) -> Tuple[int, str]:
    tot_length, rbs = int(binary_str[:15], 2), binary_str[15:]

    values = list()
    while tot_length:
        rbs_len = len(rbs)
        val, rbs = compute_bits(rbs)
        values.append(val)
        tot_length -= rbs_len - len(rbs)
    return calculate_value(type_id, values), rbs


def compute_mode_1(type_id: int, binary_str: str) -> Tuple[int, str]:
    num_sub_pks, rbs = int(binary_str[:11], 2), binary_str[11:]

    values = list()
    for _ in range(num_sub_pks):
        val, rbs = compute_bits(rbs)
        values.append(val)
    return calculate_value(type_id, values), rbs


def calculate_value(type_id: int, values: List[int]) -> int:
    match type_id:
        case 0:
            return sum(values)
        case 1:
            return prod(values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            assert len(values) == 2
            return 1 if values[0] > values[1] else 0
        case 6:
            assert len(values) == 2
            return 1 if values[0] < values[1] else 0
        case 7:
            assert len(values) == 2
            return 1 if values[0] == values[1] else 0
