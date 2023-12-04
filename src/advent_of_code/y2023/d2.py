"""Solution module for Day 2, 2023"""
from collections import defaultdict
import copy
from math import prod
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    games = {}

    for game in input:
        game_id, unparsed_rounds = game.split(":")
        game_id = int(game_id.split()[-1].strip())

        parsed_rounds = []

        for round in unparsed_rounds.split(";"):
            colour_dict = defaultdict(int)
            colours = round.strip().split(",")

            for colour in colours:
                count, colour_name = colour.strip().split()
                colour_dict[colour_name] += int(count)

            parsed_rounds.append(colour_dict)

        games[game_id] = parsed_rounds

    return games


def solution_1(input):
    available = {"red": 12, "green": 13, "blue": 14}

    games = parse(input)

    sum = 0
    for game_id in games:
        valid = True

        for round in games[game_id]:
            if any(round[colour] > available[colour] for colour in round):
                valid = False

        if valid:
            sum += game_id

    return sum


def solution_2(input):
    games = parse(input)

    sum = 0
    for game in games:
        min_colour = {"red": 0, "green": 0, "blue": 0}

        for round in games[game]:
            for colour in round:
                min_colour[colour] = max(round[colour], min_colour[colour])

        sum += prod(min_colour.values())

    return sum


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
