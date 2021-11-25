"""Solution module for Day X, YEAR"""
import copy
from datetime import datetime, timedelta
import time
from typing import Dict, Tuple

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_guard_records


def count_minutes_asleep(record: Dict[datetime, bool]) -> int:
    minutes_asleep = 0
    for t in record:
        if not record[t]:
            minutes_asleep += 1
    return minutes_asleep


def find_most_sleepy_minute(record: Dict[datetime, bool]) -> Tuple[int, int]:
    sleepy_minute_freq = dict()
    for t in record:
        if not record[t]:
            if t.minute in sleepy_minute_freq:
                sleepy_minute_freq[t.minute] += 1
            else:
                sleepy_minute_freq[t.minute] = 1
    if (
        sleepy_minute_freq
    ):  # apparently there are guards that never sleep - who would've thought?
        most_sleepy_minute = max(
            sleepy_minute_freq, key=lambda key: sleepy_minute_freq[key]
        )
        return most_sleepy_minute, sleepy_minute_freq[most_sleepy_minute]
    return 0, 0


def solution_1(input):
    minutes_asleep = dict()
    for guard in input:
        minutes_asleep[guard] = count_minutes_asleep(input[guard])
    most_sleepy_guard = max(minutes_asleep, key=lambda key: minutes_asleep[key])
    most_sleepy_minute, _ = find_most_sleepy_minute(input[most_sleepy_guard])
    return most_sleepy_guard * most_sleepy_minute


def solution_2(input):
    most_regular_guard = None
    most_regular_minute = None
    number_to_beat = 0
    for guard in input:
        sleepiest_minute, sleep_frequency = find_most_sleepy_minute(input[guard])
        if sleep_frequency > number_to_beat:
            most_regular_guard = guard
            most_regular_minute = sleepiest_minute
            number_to_beat = sleep_frequency

    return most_regular_guard * most_regular_minute


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_guard_records(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
