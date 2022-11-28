"""Solution module for Day X, YEAR"""
import copy
import re
import time
from sys import maxsize

from numpy import vectorize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input):
    rules = list()
    for line in input:
        if "=>" in line:
            f, t = line.split(" => ")
            rules.append((f.strip(), t.strip()))
        elif line:
            calibration_molecule = line.strip()
    return rules, calibration_molecule


def solution_1(input):
    rules, mol = parse(input)

    transformations = set()
    for rule, trans in rules:
        for i in range(len(mol)):
            if mol[i : i + len(rule)] == rule:
                new_mol = mol[:i] + trans + mol[i + len(rule) :]
                transformations.add(new_mol)

    return len(transformations)


def solution_2(input):
    rules, mol = parse(input)
    rules = sorted(rules, key=lambda x: -len(x[1]))

    def sub(rules, mol):
        for rule, trans in rules:
            for idx in range(len(mol)):
                if mol[idx : idx + len(trans)] == trans:
                    new_mol = mol[:idx] + rule + mol[idx + len(trans) :]
                    yield new_mol

    visited = {mol}
    backwards_mol = [mol]

    count = 0
    while backwards_mol:
        mm = []
        for i in backwards_mol:
            for j in sub(rules, i):
                if j in visited:
                    continue
                mm.append(j)
                visited.add(j)
                break

        backwards_mol = mm
        count += 1

    return count - 1  # loops one time too many


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
