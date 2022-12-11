"""Solution module for Day X, YEAR"""
import copy
from collections import defaultdict
import time
from typing import Dict, List, Tuple

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_seven_segment


def determine_digit_by_length(signal: str) -> int:
    if len(signal) == 2:
        return 1
    if len(signal) == 3:
        return 7
    if len(signal) == 4:
        return 4
    if len(signal) == 7:
        return 8
    return -1


def solution_1(input: List[Tuple[str, str]]) -> int:
    occ = defaultdict(lambda: 0)
    for _, output in input:
        for digit in output.split():
            occ[determine_digit_by_length(digit)] += 1
    return occ[1] + occ[4] + occ[7] + occ[8]


def overlap(d1, d2: str) -> int:
    return len(set(d1) & set(d2))


def solution_2(input):
    output_values = 0
    for signal, output in input:
        digit_to_segments = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }
        while any(digit == "" for digit in digit_to_segments.values()):
            for digit in signal.split():
                sd = "".join(sorted(digit))

                # 0
                if (
                    len(sd) == 6
                    and overlap(digit, digit_to_segments[8]) == 6
                    and overlap(digit, digit_to_segments[2]) == 4
                    and overlap(digit, digit_to_segments[5]) == 4
                ):
                    digit_to_segments[0] = sd

                # 1
                if len(sd) == 2:
                    digit_to_segments[1] = sd

                # 2
                if (
                    len(sd) == 5
                    and overlap(digit, digit_to_segments[3]) == 4
                    and overlap(digit, digit_to_segments[4]) == 2
                ):
                    digit_to_segments[2] = sd

                # 3
                if len(sd) == 5 and overlap(digit, digit_to_segments[1]) == 2:
                    digit_to_segments[3] = sd

                # 4
                if len(sd) == 4:
                    digit_to_segments[4] = sd

                # 5
                if (
                    len(sd) == 5
                    and overlap(digit, digit_to_segments[3]) == 4
                    and overlap(digit, digit_to_segments[4]) == 3
                ):
                    digit_to_segments[5] = sd

                # 6
                if (
                    len(sd) == 6
                    and overlap(digit, digit_to_segments[4]) == 3
                    and overlap(digit, digit_to_segments[7]) == 2
                ):
                    digit_to_segments[6] = sd

                # 7
                if len(sd) == 3:
                    digit_to_segments[7] = sd

                # 8
                if len(sd) == 7:
                    digit_to_segments[8] = sd

                # 9
                if len(sd) == 6 and overlap(digit, digit_to_segments[4]) == 4:
                    digit_to_segments[9] = sd

        str_output = ""
        for digit in output.split():
            sd = "".join(sorted(digit))
            val_list = list(digit_to_segments.values())
            str_output += str(val_list.index(sd))
        output_values += int(str_output)

    return output_values


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_seven_segment(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
