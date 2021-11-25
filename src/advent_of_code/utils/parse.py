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
    fabric_claims = dict()
    rows = split_str_by_newline(input)
    p = re.compile(r"\#(\d+)\s@\s((\d+),(\d+)):\s((\d+)x(\d+))")
    for row in rows:
        m = p.match(row)
        id = int(m.group(1))
        lm = int(m.group(3))
        tm = int(m.group(4))
        w = int(m.group(6))
        h = int(m.group(7))
        fabric_claims[id] = (lm, tm, w, h)
    return fabric_claims
