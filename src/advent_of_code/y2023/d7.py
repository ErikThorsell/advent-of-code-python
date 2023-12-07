"""Solution module for Day 7, 2023"""
from collections import defaultdict
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(input, part=1):

    def convert(hand, part=1):

        if part == 1:
            faced = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
        if part == 2:
            faced = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}

        for c in hand:
            if c in faced:
                return faced[c]
            return int(c)

    games = []

    for line in input:
        hand, bid = line.split()
        hand = [convert(c, part) for c in hand]
        games.append((hand, int(bid)))
    
    return games


def generate_best_hand(hand):

    hand_without_jokers = [c for c in hand if c != 1]

    # Mmmmmhm -- ugly
    if len(hand_without_jokers) == 0:
        hand_without_jokers = [14, 14, 14, 14, 14]

    freq = defaultdict(int)
    for card in hand_without_jokers:
        freq[card] += 1
    
    most_frequent_card = max(freq, key=freq.get)

    best_hand = []
    for c in hand:
        if c == 1:
            best_hand.append(most_frequent_card)
        else:
            best_hand.append(c)

    return best_hand 


def sort_hands(games, part=1):

    sorted_hands = defaultdict(list)

    for game in games:

        hand, _ = game

        if part == 2:
            hand = generate_best_hand(hand)

        freq = defaultdict(int)
        for card in hand:
            freq[card] += 1

        if len(freq.values()) == 1:   # Five of a kind
            sorted_hands[1].append(game)

        elif len(freq.values()) == 2:
            if 4 in freq.values():    # Four of a kind
                sorted_hands[2].append(game)
            else:                     # Full house
                sorted_hands[3].append(game)

        elif len(freq.values()) == 3:
            if 3 in freq.values():    # Three of a kind
                sorted_hands[4].append(game)
            else:                     # Two pair
                sorted_hands[5].append(game)
            
        elif len(freq.values()) == 4: # Pair
            sorted_hands[6].append(game)
        
        else:                         # High card
            sorted_hands[7].append(game)
    
    return sorted_hands


def solution_1(input):

    games = parse(input)
    sorted_hands = sort_hands(games)

    ranked_hands = []
    for _ , hands in sorted(sorted_hands.items()):
        for hand in reversed(sorted(hands)):  # reversed because 14 is "better" than 13
            ranked_hands.append(hand)

    total_winnings = 0
    for place, (hand, bid) in enumerate(ranked_hands):
        total_winnings += (len(ranked_hands) - place) * bid
            
    return total_winnings


def solution_2(input):

    games = parse(input, 2)
    sorted_hands = sort_hands(games, 2)

    ranked_hands = []
    for _ , hands in sorted(sorted_hands.items()):
        for hand in reversed(sorted(hands)):  # reversed because 14 is "better" than 13
            ranked_hands.append(hand)

    total_winnings = 0
    for place, (hand, bid) in enumerate(ranked_hands):
        total_winnings += (len(ranked_hands) - place) * bid
            
    return total_winnings


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
