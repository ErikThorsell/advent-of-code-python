"""Solution module for Day 6, 2019"""
import copy
import time
from sys import maxsize

import networkx as nx

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.graph import create_dag, create_graph
from advent_of_code.utils.parse import split_str_by_newline


def compute_orbits(graph, node):
    orbits = []
    preds = []
    preds += graph.predecessors(node)
    while preds:
        p = preds.pop(0)
        orbits.append(p)
        preds += graph.predecessors(p)
    return orbits


def solution_1(input):
    edges = [(s.split(")")[0], s.split(")")[1]) for s in input]
    dag = create_dag(edges)
    tot_orbits = 0
    for node in dag.nodes:
        orbits = compute_orbits(dag, node)
        tot_orbits += len(orbits)
    return tot_orbits


def solution_2(input):
    edges = [(s.split(")")[0], s.split(")")[1]) for s in input]
    graph = create_graph(edges)
    dfs = nx.shortest_path(graph, "YOU", "SAN")
    dfs = [(x, y) for x, y in zip(dfs[1:-1], dfs[2:-1])]
    return len(dfs)


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
