"""Solution module for Day 4, 2023"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def solution_1(input):

    score = 0

    for line in input:
        id, cards = line.split(":")
        id = int(id.split()[-1].strip())

        winning, owned = cards.split("|")
        winning = [int(w.strip()) for w in winning.split()]
        owned = [int(o.strip()) for o in owned.split()]

        winners = []
        sub_score = 0
        for card in owned:
            if card in winning:
                winners.append(card)
        
        if len(winners) == 1:
            sub_score += 1
        elif len(winners) > 1:
            sub_score += 1
            for _ in range(len(winners)-1):
                sub_score *= 2
        
        score += sub_score
    
    return score


def solution_2(input):

    copies = {}

    for line in input:

        id, cards = line.split(":")
        id = int(id.split()[-1].strip())

        winning, owned = cards.split("|")
        winning = [int(w.strip()) for w in winning.split()]
        owned = [int(o.strip()) for o in owned.split()]

        copies[id] = {"winning": winning, "owned": owned, "copies": 1}
    
    for id in copies:
        winners = 0
        for card in copies[id]["owned"]:
            if card in copies[id]["winning"]:
                winners += 1
                copies[id+winners]["copies"] += copies[id]["copies"]
    
    return sum([c["copies"] for c in copies.values()])
        


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
