"""Solution module for Day 3, 2021"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_sub_commands, split_str_by_newline
from advent_of_code.utils.submarine import drive_sub_aim


def calculate_gamma_rate(power_consumption):
    b1_1 = 0
    b1_0 = 0
    b2_1 = 0
    b2_0 = 0
    b3_1 = 0
    b3_0 = 0
    b4_1 = 0
    b4_0 = 0
    b5_1 = 0
    b5_0 = 0
    b6_1 = 0
    b6_0 = 0
    b7_1 = 0
    b7_0 = 0
    b8_1 = 0
    b8_0 = 0
    b9_1 = 0
    b9_0 = 0
    b10_1 = 0
    b10_0 = 0
    b11_1 = 0
    b11_0 = 0
    b12_1 = 0
    b12_0 = 0
    for p in power_consumption:
        if p[0] == "1":
            b1_1 += 1
        else:
            b1_0 += 1
        if p[1] == "1":
            b2_1 += 1
        else:
            b2_0 += 1
        if p[2] == "1":
            b3_1 += 1
        else:
            b3_0 += 1
        if p[3] == "1":
            b4_1 += 1
        else:
            b4_0 += 1
        if p[4] == "1":
            b5_1 += 1
        else:
            b6_0 += 1
        if p[5] == "1":
            b6_1 += 1
        else:
            b5_0 += 1
        if p[6] == "1":
            b7_1 += 1
        else:
            b7_0 += 1
        if p[7] == "1":
            b8_1 += 1
        else:
            b8_0 += 1
        if p[8] == "1":
            b9_1 += 1
        else:
            b9_0 += 1
        if p[9] == "1":
            b10_1 += 1
        else:
            b10_0 += 1
        if p[10] == "1":
            b11_1 += 1
        else:
            b11_0 += 1
        if p[11] == "1":
            b12_1 += 1
        else:
            b12_0 += 1

    res = ""
    if b1_1 > b1_0:
        res += "1"
    else:
        res += "0"
    if b2_1 > b2_0:
        res += "1"
    else:
        res += "0"
    if b3_1 > b3_0:
        res += "1"
    else:
        res += "0"
    if b4_1 > b4_0:
        res += "1"
    else:
        res += "0"
    if b5_1 > b5_0:
        res += "1"
    else:
        res += "0"
    if b6_1 > b6_0:
        res += "1"
    else:
        res += "0"
    if b7_1 > b7_0:
        res += "1"
    else:
        res += "0"
    if b8_1 > b8_0:
        res += "1"
    else:
        res += "0"
    if b9_1 > b9_0:
        res += "1"
    else:
        res += "0"
    if b10_1 > b10_0:
        res += "1"
    else:
        res += "0"
    if b11_1 > b11_0:
        res += "1"
    else:
        res += "0"
    if b12_1 > b12_0:
        res += "1"
    else:
        res += "0"
    return res


def calculate_epsilon_rate(power_consumption):
    b1_1 = 0
    b1_0 = 0
    b2_1 = 0
    b2_0 = 0
    b3_1 = 0
    b3_0 = 0
    b4_1 = 0
    b4_0 = 0
    b5_1 = 0
    b5_0 = 0
    b6_1 = 0
    b6_0 = 0
    b7_1 = 0
    b7_0 = 0
    b8_1 = 0
    b8_0 = 0
    b9_1 = 0
    b9_0 = 0
    b10_1 = 0
    b10_0 = 0
    b11_1 = 0
    b11_0 = 0
    b12_1 = 0
    b12_0 = 0
    for p in power_consumption:
        if p[0] == "1":
            b1_1 += 1
        else:
            b1_0 += 1
        if p[1] == "1":
            b2_1 += 1
        else:
            b2_0 += 1
        if p[2] == "1":
            b3_1 += 1
        else:
            b3_0 += 1
        if p[3] == "1":
            b4_1 += 1
        else:
            b4_0 += 1
        if p[4] == "1":
            b5_1 += 1
        else:
            b6_0 += 1
        if p[5] == "1":
            b6_1 += 1
        else:
            b5_0 += 1
        if p[6] == "1":
            b7_1 += 1
        else:
            b7_0 += 1
        if p[7] == "1":
            b8_1 += 1
        else:
            b8_0 += 1
        if p[8] == "1":
            b9_1 += 1
        else:
            b9_0 += 1
        if p[9] == "1":
            b10_1 += 1
        else:
            b10_0 += 1
        if p[10] == "1":
            b11_1 += 1
        else:
            b11_0 += 1
        if p[11] == "1":
            b12_1 += 1
        else:
            b12_0 += 1

    res = ""
    if b1_1 > b1_0:
        res += "0"
    else:
        res += "1"
    if b2_1 > b2_0:
        res += "0"
    else:
        res += "1"
    if b3_1 > b3_0:
        res += "0"
    else:
        res += "1"
    if b4_1 > b4_0:
        res += "0"
    else:
        res += "1"
    if b5_1 > b5_0:
        res += "0"
    else:
        res += "1"
    if b6_1 > b6_0:
        res += "0"
    else:
        res += "1"
    if b7_1 > b7_0:
        res += "0"
    else:
        res += "1"
    if b8_1 > b8_0:
        res += "0"
    else:
        res += "1"
    if b9_1 > b9_0:
        res += "0"
    else:
        res += "1"
    if b10_1 > b10_0:
        res += "0"
    else:
        res += "1"
    if b11_1 > b11_0:
        res += "0"
    else:
        res += "1"
    if b12_1 > b12_0:
        res += "0"
    else:
        res += "1"
    return res


def get_bit_criteria(rows, rating_type: str, bit_position: int) -> str:
    n_0 = 0
    n_1 = 0
    for r in rows:
        if r[bit_position] == "0":
            n_0 += 1
        else:
            n_1 += 1
    if rating_type == "oxygen":
        if n_0 > n_1:
            return "0"
        return "1"
    if rating_type == "co2":
        if n_0 <= n_1:
            return "0"
        return "1"


def calculate_oxygen_generator_rating(rows):
    for idx in range(len(rows[0])):
        bit_criteria = get_bit_criteria(rows, "oxygen", idx)
        rows = [r for r in rows if r[idx] == bit_criteria]
        if len(rows) == 1:
            return rows[0]


def calculate_co2_generator_rating(rows):
    for idx in range(len(rows[0])):
        bit_criteria = get_bit_criteria(rows, "co2", idx)
        rows = [r for r in rows if r[idx] == bit_criteria]
        print(f"{bit_criteria=}")
        print(f"{rows=}")
        if len(rows) == 1:
            return rows[0]


def solution_1(input):
    gamma = int(calculate_gamma_rate(input), 2)
    epsilon = int(calculate_epsilon_rate(input), 2)
    return gamma * epsilon


def solution_2(input):
    oxygen_generator_rating = int(calculate_oxygen_generator_rating(input), 2)
    print(f"{oxygen_generator_rating=}")
    co2_generator_rating = int(calculate_co2_generator_rating(input), 2)
    print(f"{co2_generator_rating=}")
    return oxygen_generator_rating * co2_generator_rating


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
