from typing import List


def split_by_newline(input: str) -> List[str]:
    return [int(s) for s in input.split("\n") if s]
