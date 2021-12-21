"""Solution module for Day 21, 2021"""
from functools import cache
from itertools import product
import time

from advent_of_code.utils.fetch import fetch


def play_round(game, player, die_rolls):

    die = sum(range(die_rolls + 1, die_rolls + 4))
    p = (game[player - 1][0] + die - 1) % 10 + 1

    if player == 1:
        return [(p, game[0][-1] + p), (game[1][0], game[1][-1])], die_rolls + 3
    return [(game[0][0], game[0][-1]), (p, game[1][-1] + p)], die_rolls + 3


@cache
def play_quantum(curr_pos, curr_score, other_pos, other_score):
    if curr_score >= 21:
        return (1, 0)
    if other_score >= 21:
        return (0, 1)

    tot_w1 = tot_w2 = 0

    for r1, r2, r3 in list(product([1, 2, 3], repeat=3)):
        new_pos = (curr_pos + r1 + r2 + r3 - 1) % 10 + 1
        new_score = curr_score + new_pos

        p2_wins, p1_wins = play_quantum(other_pos, other_score, new_pos, new_score)

        tot_w1 += p1_wins
        tot_w2 += p2_wins

    return (tot_w1, tot_w2)


def solution_1(input):
    p1, p2 = input[0], input[-1]
    game = [(p1, 0), (p2, 0)]
    die_rolls = 0

    while True:
        for player in [1, 2]:
            game, die_rolls = play_round(game, player, die_rolls)
            if game[player - 1][-1] >= 1000:
                return die_rolls * game[player][-1]


def solution_2(input):
    p1, p2 = input[0], input[-1]
    return max(play_quantum(p1, 0, p2, 0))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = [int(row[-1]) for row in input.split("\n")]

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
