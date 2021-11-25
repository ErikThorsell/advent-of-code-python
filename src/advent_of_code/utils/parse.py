from collections import defaultdict
from datetime import datetime, timedelta
import re
from typing import Dict, List, Tuple


def split_number_by_separator(input: str, sep: str) -> List[int]:
    return [int(s) for s in input.split(sep) if s]


def split_number_by_newline(input: str) -> List[int]:
    return split_number_by_separator(input, "\n")


def split_str_by_separator(input: str, sep: str) -> List[str]:
    return [s for s in input.split(sep) if s]


def split_str_by_newline(input: str) -> List[str]:
    return split_str_by_separator(input, "\n")


def parse_fabric_claims(input: str) -> Dict[int, Tuple[int, int, int, int]]:
    rows = split_str_by_newline(input)
    p = re.compile(r"\#(\d+)\s@\s((\d+),(\d+)):\s((\d+)x(\d+))")
    fabric_claims = dict()
    for row in rows:
        m = p.match(row)
        id = int(m.group(1))
        lm = int(m.group(3))
        tm = int(m.group(4))
        w = int(m.group(6))
        h = int(m.group(7))
        fabric_claims[id] = (lm, tm, w, h)
    return fabric_claims


def parse_guard_records(input: str) -> Dict[int, Dict[datetime, bool]]:
    unsorted_rows = split_str_by_newline(input)
    rows = sorted(unsorted_rows)

    p_time = re.compile(r"\[(\d+-\d+-\d+\s\d\d:\d\d)\]")
    p_guard = re.compile(r"#(\d+)")

    last_timestamp = None
    guard_tracker = defaultdict(dict)
    guard_id = None

    for row in rows:
        timestamp = datetime.strptime(p_time.match(row).group(1), "%Y-%m-%d %H:%M")

        if p_guard.search(row):
            guard_id = int(p_guard.search(row).group(1))
            guard_tracker[guard_id][timestamp] = True
            last_timestamp = timestamp

        elif "falls asleep" in row:
            duration = timestamp - last_timestamp
            for d in range(duration.seconds // 60):
                guard_tracker[guard_id][
                    last_timestamp + timedelta(seconds=d * 60)
                ] = True
            last_timestamp = timestamp

        elif "wakes up" in row:
            duration = timestamp - last_timestamp
            for d in range(duration.seconds // 60):
                guard_tracker[guard_id][
                    last_timestamp + timedelta(seconds=d * 60)
                ] = False
            last_timestamp = timestamp

    return guard_tracker
