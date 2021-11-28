"""Solution module for Day X, YEAR"""
from collections import deque
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_all_numbers


def solution_1(n_players, last_marble: int) -> int:
    scores = {p: 0 for p in range(n_players)}
    player = 0
    circle = deque()
    circle.append(0)

    for current_marble in range(1, last_marble + 1):
        if current_marble % 23 == 0:
            scores[player] += current_marble
            circle.rotate(7)
            scores[player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(current_marble)

        player = (player + 1) % n_players

    return max(scores.values())


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    numbers = parse_all_numbers(input)
    print(numbers[0], numbers[1])

    tic = time.perf_counter()
    s1 = solution_1(numbers[0], numbers[1])
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_1(numbers[0], numbers[1] * 100)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
