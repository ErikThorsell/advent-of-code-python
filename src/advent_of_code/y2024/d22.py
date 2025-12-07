"""Solution module for Day 22, 2024"""
from collections import defaultdict
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """1
10
100
2024"""
    answer = 37327623
    assert(solution_1(input) == answer)
    

def test_2():
    input = """1
2
3
2024"""
    answer = 23
    assert(solution_2(input) == answer)


def mix(value, secret):
    return value ^ secret


def prune(secret):
    return secret % 16777216


def secretify(secret):
    secret = prune(mix(secret*64, secret))
    secret = prune(mix(int(secret/32), secret))
    secret = prune(mix(secret*2048, secret))
    return secret


def solution_1(input):

    total = 0

    for secret in map(int, input.split("\n")):
        for _ in range(2000):
            secret = secretify(secret)
        
        total += secret 
    
    return total


def solution_2(input):

    sequence_sums = defaultdict(int)

    for secret in map(int, input.split("\n")):
        prices = [secret % 10]

        for _ in range(2000):
            secret = secretify(secret)
            prices.append(secret % 10)

        changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]

        seen_sequences = {}

        for i in range(len(changes) - 3):
            seq = tuple(changes[i:i+4])
            if seq not in seen_sequences:
                sell_price = prices[i + 4]
                seen_sequences[seq] = sell_price

        for seq, sell_price in seen_sequences.items():
            sequence_sums[seq] += sell_price

    return max(sequence_sums.values())


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
