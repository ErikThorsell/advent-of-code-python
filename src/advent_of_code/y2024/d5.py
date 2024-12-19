"""Solution module for Day 5, 2024"""
import copy
from collections import defaultdict, deque
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.graph import create_dag


def test_1():
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    answer = 143
    assert(solution_1(input) == answer)
    

def test_2():
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    answer = 123
    assert(solution_2(input) == answer)


def build_graph(rules):
    graph = defaultdict(list)
    for a, b in rules:
        graph[a].append(b)
    return graph

def topological_sort(update, graph):
    partial_graph = defaultdict(list)
    indegree = defaultdict(int)
    for node in update:
        partial_graph[node] = []
        indegree[node] = 0
    
    for node in update:
        for succ_node in graph[node]:
            if succ_node in update:
                partial_graph[node].append(succ_node)
                indegree[succ_node] += 1
    
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in partial_graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order


def middle_page(update):
    return update[len(update) // 2]


def parse(input):
    rules, updates = input.split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]
    return rules, updates


def solution_1(input):
    rules, updates = parse(input)
    graph = build_graph(rules)
    
    total = 0 
    for update in updates:
        if topological_sort(update, graph) == update:
            total += middle_page(update)

    return total


def solution_2(input):
    rules, updates = parse(input)
    graph = build_graph(rules)
    
    total = 0 
    for update in updates:
        if (tsorted := topological_sort(update, graph)) != update:
            total += middle_page(tsorted)
    
    return total


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2()
    print("Test 2 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
