"""Solution module for Day 23, 2024"""
from collections import defaultdict
import copy
from itertools import combinations
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    answer = 7
    assert(solution_1(input) == answer)
    

def test_2():
    input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    answer = "co,de,ka,ta"
    assert(solution_2(input) == answer)


def makes_three(graph, triplet):
    a, b, c = triplet
    return b in graph[a] and c in graph[a] and c in graph[b]


def solution_1(input):
    graph = defaultdict(set)

    for conn in input.split("\n"):
        a, b = conn.split("-")
        graph[a].add(b)
        graph[b].add(a)

    triplets = combinations(graph.keys(), 3)
    threes = [triplet for triplet in triplets if makes_three(graph, triplet)]
    return sum(any(node.startswith('t') for node in triplet) for triplet in threes)


def bron_kerbosch_pivot(R, P, X, graph, cliques):

    if not P and not X:
        cliques.append(R)
        return

    pivot = next(iter(P.union(X))) if P.union(X) else None

    if pivot:
        neighbors = graph[pivot]
    else:
        neighbors = set()

    for v in P - neighbors:
        bron_kerbosch_pivot(R.union({v}),
                            P.intersection(graph[v]),
                            X.intersection(graph[v]),
                            graph,
                            cliques)
        P.remove(v)
        X.add(v)


def find_largest_clique(graph):
    cliques = []
    bron_kerbosch_pivot(set(), set(graph.keys()), set(), graph, cliques)
    return max(cliques, key=lambda x: len(x), default=[])


def solution_2(input):
    graph = defaultdict(set)

    for conn in input.split("\n"):
        a, b = conn.split("-")
        graph[a].add(b)
        graph[b].add(a)
    
    return ",".join(sorted(find_largest_clique(graph)))


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
