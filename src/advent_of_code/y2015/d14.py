"""Solution module for Day 15, 2015"""
import copy
from collections import defaultdict
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    deers = dict()
    for line in input:
        deers[line.split()[0]] = re.findall(r"\d+", line)
    return deers


def race(deer, duration):
    pace = int(deer[0])
    max_stamina = int(deer[1])
    req_rest = int(deer[2])

    distance = 0
    stamina = max_stamina
    resting = False
    resting_point = 0

    for i in range(duration):

        if not resting:
            distance += pace

            stamina -= 1
            if stamina == 0:
                resting = True
                resting_point = i

        elif i == resting_point + req_rest:
            resting = False
            stamina = max_stamina

    return distance


def solution_1(input):
    deers = parse(input)

    distances = dict()
    for d, _ in sorted(deers.items()):
        distances[d] = race(deers[d], 2503)

    return max(distances.values())


def solution_2(input):
    deers = defaultdict(dict)

    T = 2503

    for line in input:
        name = line.split()[0]
        pace, stamina, rest = map(int, re.search(r"(\d+) .* (\d+) .* (\d+)", line).groups())
        deers[name]["pace"] = pace
        deers[name]["stamina"] = stamina
        deers[name]["rest"] = rest
        deers[name]["distance"] = pace * (stamina * (T // (stamina + rest)) + min(T % (stamina + rest), stamina))
        deers[name]["score"] = 0

    for t in range(1, T + 1):
        for d in deers:
            pace, stamina, rest = deers[d]["pace"], deers[d]["stamina"], deers[d]["rest"]
            deers[d]["distance"] = pace * (stamina * (t // (stamina + rest)) + min(t % (stamina + rest), stamina))

        d_max = max(deers[d]["distance"] for d in deers)

        for d in deers:
            if deers[d]["distance"] == d_max:
                deers[d]["score"] += 1

    return max(deers[d]["score"] for d in deers)


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
