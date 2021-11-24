from typing import List


def split_number_by_separator(input: str, sep: str) -> List[str]:
    return [int(s) for s in input.split(sep) if s]


def split_number_by_newline(input: str) -> List[int]:
    return split_number_by_separator(input, "\n")
