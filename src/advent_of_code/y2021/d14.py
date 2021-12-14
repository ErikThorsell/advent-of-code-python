"""Solution module for Day 14, 2021"""
from collections import Counter, deque
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_polymer


def apply_rules_naive(template, rules):
    new_template = ""
    for i, _ in enumerate(template[:-1]):
        new_template += template[i]
        k = f"{template[i]}{template[i+1]}"
        if k in rules:
            new_template += rules[k]
    new_template += template[-1]
    return new_template


def solution_1(template, rules):
    for _ in range(10):
        template = apply_rules_naive(template, rules)
    freq = Counter(template)
    return freq.most_common()[0][1] - freq.most_common()[-1][1]


def apply_rules(freq, rules):
    new_freq = freq.copy()
    for pair, count in freq.items():
        ins = rules[pair]
        new_freq[f"{pair[0]}{ins}"] += count
        new_freq[f"{ins}{pair[1]}"] += count
        new_freq[pair] -= count
    return new_freq


def solution_2(template, rules):
    pair_freq = Counter()
    for i, _ in enumerate(template[:-1]):
        pair_freq[f"{template[i]}{template[i+1]}"] += 1

    for _ in range(40):
        pair_freq = apply_rules(pair_freq, rules)

    char_freq = Counter()
    for pair, count in pair_freq.items():
        for c in pair:
            char_freq[c] += count

    char_freq[template[0]] += 1
    char_freq[template[-1]] += 1
    for c in char_freq.keys():
        char_freq[c] //= 2

    return char_freq.most_common()[0][1] - char_freq.most_common()[-1][1]


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    template, rules = parse_polymer(input)

    tic = time.perf_counter()
    s1 = solution_1(template, rules)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(template, rules)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
