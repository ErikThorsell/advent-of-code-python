"""Solution module for Day 18, 2021"""
import ast
import copy
from functools import reduce
from itertools import permutations
from math import floor, ceil
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def split(term):
    # If any regular number is 10 or greater, the leftmost such regular number splits.
    if isinstance(term, int):
        if term >= 10:
            # To split a regular number, replace it with a pair;
            # the left element of the pair should be the regular number divided by two and rounded down,
            # the right element of the pair should be the regular number divided by two and rounded up.
            return True, [floor(term / 2), ceil(term / 2)]
        return False, term

    x, y = term
    # Start by going left as much as possible.
    diff, x = split(x)
    if diff:
        return True, [x, y]
    # If we found nothing to split, go right.
    diff, y = split(y)
    return diff, [x, y]


def add_left(old, new):
    if new is None:
        return old
    if isinstance(old, int):
        return old + new
    return [add_left(old[0], new), old[1]]


def add_right(old, new):
    if new is None:
        return old
    if isinstance(old, int):
        return old + new
    return [old[0], add_right(old[1], new)]


def explode(pair, depth=4):
    if isinstance(pair, int):
        return False, None, pair, None

    left, right = pair

    # If any pair is nested inside four pairs, the leftmost such pair explodes.
    if depth == 0:
        # Exploding pairs will always consist of two regular numbers.
        assert len(pair) == 2
        # The entire exploding pair is replaced with the regular number 0.
        return True, left, 0, right

    # Traverse left
    # The pair's left value is added to the first regular number to the left of the exploding pair (if any).
    exploded, prev_left, new, prev_right = explode(left, depth - 1)
    if exploded:
        return True, prev_left, [new, add_left(right, prev_right)], None

    # Traverse right
    # The pair's right value is added _to_ the first regular number to the right of the exploding pair (if any).
    exploded, prev_left, new, prev_right = explode(right, depth - 1)
    if exploded:
        return True, None, [add_right(left, prev_left), new], prev_right

    return False, None, pair, None


# reduce() will give: "the aggregated result of all previously seen rows", "the next row"
def add(agg_sum, next_row):
    # To add two snailfish numbers, form a pair from the left and right parameters of the addition operator.
    pair = [agg_sum, next_row]

    # Check if pair must be reduced.
    # During reduction, at most one action applies, after which the process returns to the top of the list of actions.
    while True:
        exploded, _, pair, _ = explode(pair)
        if exploded:
            continue
        did_split, pair = split(pair)
        if not did_split:
            break

    return pair


def magnitude(pair):
    if isinstance(pair, int):
        return pair
    return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])


def solution_1(input):
    return magnitude(reduce(add, input))


def solution_2(input):
    max_sum = -maxsize
    for (r1, r2) in permutations(input, 2):
        max_sum = max(magnitude(add(r1, r2)), max_sum)
    return max_sum


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = list(map(ast.literal_eval, input.splitlines()))

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
