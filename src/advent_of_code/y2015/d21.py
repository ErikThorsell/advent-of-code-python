"""Solution module for Day X, YEAR"""
import copy
from itertools import combinations
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


SHOP = {
    "weapons": {
        "dagger": [8, 4, 0],
        "shortsword": [10, 5, 0],
        "warhammer": [25, 6, 0],
        "longsword": [40, 7, 0],
        "greataxe": [74, 8, 0],
    },
    "armor": {
        "leather": [13, 0, 1],
        "chainmail": [31, 0, 2],
        "splintmail": [53, 0, 3],
        "bandedmail": [75, 0, 4],
        "platemail": [102, 0, 5],
        "dummymail": [0, 0, 0],  # added to mimic choosing no armor
    },
    "rings": {
        "damage+1": [25, 1, 0],
        "damage+2": [50, 2, 0],
        "damage+3": [100, 3, 0],
        "defense+1": [20, 0, 1],
        "defense+2": [40, 0, 2],
        "defense+3": [80, 0, 3],
        "dummyring-1": [0, 0, 0],  # added to mimic choosing only one ring
        "dummyring-2": [0, 0, 0],  # added to mimic choosing no ring
    },
}


def fight(hp, damage, armor, boss_hp, boss_damage, boss_armor):
    player_turn = True

    while True:
        if player_turn:
            boss_hp -= damage - boss_armor
            player_turn = False
        else:
            hp -= boss_damage - armor
            player_turn = True

        if boss_hp <= 0:
            return True
        elif hp <= 0:
            return False


def solution_1(input):
    boss_hp, boss_damage, boss_armor = map(int, re.findall(r"-?\d+", input))
    hp = 100
    min_cost = maxsize

    for w in SHOP["weapons"].values():
        for a in SHOP["armor"].values():
            for r1, r2 in combinations(SHOP["rings"].values(), 2):
                cost = w[0] + a[0] + r1[0] + r2[0]
                damage = w[1] + a[1] + r1[1] + r2[1]
                armor = w[2] + a[2] + r1[2] + r2[2]
                if fight(hp, damage, armor, boss_hp, boss_damage, boss_armor):
                    min_cost = min(cost, min_cost)

    return min_cost


def solution_2(input):
    boss_hp, boss_damage, boss_armor = map(int, re.findall(r"-?\d+", input))
    hp = 100
    max_cost = 0

    for w in SHOP["weapons"].values():
        for a in SHOP["armor"].values():
            for r1, r2 in combinations(SHOP["rings"].values(), 2):
                cost = w[0] + a[0] + r1[0] + r2[0]
                damage = w[1] + a[1] + r1[1] + r2[1]
                armor = w[2] + a[2] + r1[2] + r2[2]
                if not fight(hp, damage, armor, boss_hp, boss_damage, boss_armor):
                    max_cost = max(cost, max_cost)

    return max_cost


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = input

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
