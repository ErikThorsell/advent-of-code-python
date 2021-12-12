"""Solution module for Day 12, 2021"""
from collections import defaultdict
import copy
import time
from sys import maxsize

from advent_of_code.utils.graph import create_graph
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def create_graph(edges):
    graph = defaultdict(list)
    for r in edges:
        s, e = r.split("-")
        graph[s].append(e)
        graph[e].append(s)
    return graph


def dfs(graph, vertex, visited, part):
    def allowed_to_visit(vertex, visited, part):
        if vertex not in visited:
            return True
        if part == 2 and len(visited) == len(set(visited)) and vertex != "start":
            return True
        return False

    if vertex == "end":
        return 1
    if vertex.islower():
        visited = visited + [vertex]
    num_paths = 0
    for v in graph[vertex]:
        if allowed_to_visit(v, visited, part):
            num_paths += dfs(graph, v, visited, part)
    return num_paths


def solution_1(input):
    graph = create_graph(input)
    return dfs(graph, "start", [], part=1)


def solution_2(input):
    graph = create_graph(input)
    return dfs(graph, "start", [], part=2)


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
