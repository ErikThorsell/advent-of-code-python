"""Solution module for Day 3, 2021"""
from typing import List
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def calculate_radiation_rate(report: List[str], radiation_type: str) -> str:
    num_bits = len(report[0])  # assume all numbers have the same number of bits
    radiation_rate = ""

    for bit in range(num_bits):
        zeros, ones = 0, 0
        for number in report:
            if number[bit] == "0":
                zeros += 1
            else:
                ones += 1

        if radiation_type == "gamma":
            radiation_rate += "1" if ones > zeros else "0"
        if radiation_type == "epsilon":
            radiation_rate += "0" if ones > zeros else "1"

    return radiation_rate


def get_bit_criteria(rows, rating_type: str, bit_position: int) -> str:
    bits_dict = {"0": 0, "1": 0}

    for r in rows:
        bits_dict[r[bit_position]] += 1

    if rating_type == "oxygen":
        if bits_dict["0"] > bits_dict["1"]:
            return "0"
        return "1"

    if rating_type == "co2":
        if bits_dict["0"] <= bits_dict["1"]:
            return "0"
        return "1"


def calculate_generator_rating(report: List[str], type: str) -> str:
    for idx in range(len(report[0])):
        bit_criteria = get_bit_criteria(report, type, idx)
        report = [r for r in report if r[idx] == bit_criteria]
        if len(report) == 1:
            return report[0]


def solution_1(input):
    gamma = int(calculate_radiation_rate(input, "gamma"), 2)
    epsilon = int(calculate_radiation_rate(input, "epsilon"), 2)
    return gamma * epsilon


def solution_2(input):
    oxygen_generator_rating = int(calculate_generator_rating(input, "oxygen"), 2)
    co2_generator_rating = int(calculate_generator_rating(input, "co2"), 2)
    return oxygen_generator_rating * co2_generator_rating


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
