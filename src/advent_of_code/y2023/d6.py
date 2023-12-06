"""Solution module for Day 6, 2023"""
import copy
import time

from advent_of_code.utils.fetch import fetch


def parse(input):
    times, distances = input.split("\n")
    times = list(map(int, times.split()[1:]))
    distances = list(map(int, distances.split()[1:]))

    races = []
    for race in range(len(times)):
        races.append((times[race], distances[race]))
    
    return races


def calc_race(time, max_distance):

    winning_strategies = 0
    for t in range(time):
        speed = t
        distance = (time-t)*speed

        if distance > max_distance:
            winning_strategies += 1

    return winning_strategies


def solution_1(input):

    races = parse(input)

    winning_strategies = 1
    for (time, distance) in races:
        winning_strategies *= calc_race(time, distance)
    
    return winning_strategies
        

def solution_2(input):

    races = parse(input)

    time = int(''.join([str(r[0]) for r in races]))
    distance = int(''.join([str(r[1]) for r in races]))

    return calc_race(time, distance)
    

def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
#    input = """Time:      7  15   30
#Distance:  9  40  200"""

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
