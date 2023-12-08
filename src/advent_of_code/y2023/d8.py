"""Solution module for Day 8, 2023"""
import copy
from functools import reduce
from math import gcd
import re
import time

from advent_of_code.utils.fetch import fetch


def create_map(input):

    instr, nodes = input.split("\n\n")
    nodes = nodes.split("\n")

    map = {}
    for line in nodes:
        node, left, right = re.findall(r"\w+", line)
        map[node] = (left, right)

    return instr, map


def find_ending(map, instr, start, end):

    i_num = 0
    current_node = start

    # Using endswith() for both parts assumes all nodes
    # have three characters.
    while not current_node.endswith(end):
        i = instr[i_num%len(instr)]
        current_node = map[current_node][0] if i == "L" else map[current_node][1]
        i_num += 1

    return i_num


def solution_1(input):
    instr, map = create_map(input)
    return find_ending(map, instr, "AAA", "ZZZ")


def solution_2(input):
    instr, map = create_map(input)
    start_nodes = [n for n in map if n.endswith("A")]
    shortest = [find_ending(map, instr, sn, "Z") for sn in start_nodes]
    return reduce(lambda a, b: a * b // gcd(a, b), shortest)



def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
