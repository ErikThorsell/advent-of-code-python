"""Solution module for Day X, YEAR"""
import copy
import time

import networkx as nx
from networkx.classes.function import all_neighbors, neighbors

from advent_of_code.utils.graph import create_dag
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_graph_edges


# This feels like cheating...
def solution_1(input: str) -> str:
    dag = create_dag(input)
    return "".join(list(nx.lexicographical_topological_sort(dag)))


def solution_2(input: str, n_workers, overhead: int) -> int:
    dag = create_dag(input)

    busy_workers = []
    queue = []
    total_time = 0
    while busy_workers or dag:
        avail_work = [n for n in dag if n not in queue and dag.in_degree(n) == 0]

        if avail_work and len(busy_workers) < n_workers:
            new_work = min(avail_work)  # min gets smallest task alphabetically
            busy_workers.append(ord(new_work) - 64 + overhead)
            queue.append(new_work)

        else:
            min_time = min(busy_workers)
            completed = [queue[i] for i, v in enumerate(busy_workers) if v == min_time]
            busy_workers = [v - min_time for v in busy_workers if v > min_time]
            queue = [t for t in queue if t not in completed]
            total_time += min_time
            dag.remove_nodes_from(completed)

    return total_time


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_graph_edges(input)

    tic = time.perf_counter()
    s1 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(parsed_input, 5, 60)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
