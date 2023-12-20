"""Solution module for Day 20, 2023"""
from collections import defaultdict
import copy
from math import lcm
import time

from advent_of_code.utils.fetch import fetch


def test_1():
    input = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
    answer = 32000000
    assert(solution_1(input) == answer)
    

def test_2():
    input = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
    answer = 11687500
    assert(solution_1(input) == answer)


def parse(input):
    flips = defaultdict(list)
    conjunctions = defaultdict(list)
    broadcasters = []
    

    for idx, line in enumerate(input.split("\n")):
        # [module]*[name] -> [to]+
        parts = line.strip().split()


        if parts[0].startswith("%"):
            name = parts[0][1:]
            for p in parts[2:]:
                flips[name].append(p.strip(","))

        elif parts[0].startswith("&"):
            name = parts[0][1:]
            for p in parts[2:]:
                conjunctions[name].append(p.strip(","))
        
        elif parts[0] == "broadcaster":
            for p in parts[2:]:
                broadcasters.append(p.strip(","))
    
    return flips, conjunctions, broadcasters


def press_button(pushes, flips, conjunctions, broadcasters, states, memory):

    lows, highs = 0, 0

    for _ in range(pushes):
        queue = [("button", False, "broadcaster")]

        while queue:
            (input, level, output), queue = queue[0], queue[1:]

            if level:
                highs += 1
            else:
                lows += 1

            if output == "broadcaster":
                for next_out in broadcasters:
                    queue.append(("broadcaster", level, next_out))
            
            elif output in flips:
                if not level:
                    states[output] = not states[output]
                    for next_out in flips[output]:
                        queue.append((output, states[output], next_out))
            
            elif output in conjunctions:
                memory[output][input] = level
                snd = not all(l for l in memory[output].values())
                for next_out in conjunctions[output]:
                    queue.append((output, snd, next_out))

    return lows*highs


def find_min(flips, conjunctions, broadcasters, states, memory):
    """Some explanation is in order.
    
    By inspecting the input file we can see what is required in order to turn on rx.
    In the case of my input, this is: &lb -> rx, meaning that rx will turn on when lb
    sends a low pulse.

    We can learn when &lb will send a low pulse by inspecting its preceding modules.
    In the case of my input, these are: &rz, &lf, &br, &fk.
    By looking at the iteration number every time the input is one of the above
    modules, it is possible to deduce that the behaviour of these modules are
    cyclic. 

    By "pressing the button" until every module of interest has appeared twice, it
    is possible to find the least common multiple for all four cycles.
    The cycle for a module is simply the difference between the two iteration numbers
    where the module was an input.
    """

    seen = defaultdict(list)

    i = 0

    # seen is needed because all([]) is True
    while not (seen and all(len(lists) >= 2 for lists in seen.values())):

        queue = [("button", False, "broadcaster")]

        while queue:
            (input, level, output), queue = queue[0], queue[1:]

            if input in ["rz", "lf", "br", "fk"] and level:
                seen[input].append(i+1)

            if output == "rx" and not level:
                return i+1

            if output == "broadcaster":
                for next_out in broadcasters:
                    queue.append(("broadcaster", level, next_out))
            
            elif output in flips:
                if not level:
                    states[output] = not states[output]
                    for next_out in flips[output]:
                        queue.append((output, states[output], next_out))
            
            elif output in conjunctions:
                memory[output][input] = level
                snd = not all(l for l in memory[output].values())
                for next_out in conjunctions[output]:
                    queue.append((output, snd, next_out))
    
        i += 1

    return lcm(*[c[1] - c[0] for c in seen.values()])


def solution_1(input):

    flips, conjunctions, broadcasters = parse(input)

    # Initialize states and memory
    states = {}
    memory = defaultdict(dict)
    for flip in flips:
        states[flip] = False
        for output in flips[flip]:
            if output in conjunctions:
                memory[output][flip] = False

    for con, inputs in conjunctions.items():
        for input in inputs:
            if input in conjunctions:
                memory[input][con] = False
    
    return press_button(1000, flips, conjunctions, broadcasters, states, memory)


def solution_2(input):
    flips, conjunctions, broadcasters = parse(input)

    # Initialize states and memory
    states = {}
    memory = defaultdict(dict)
    for flip in flips:
        states[flip] = False
        for output in flips[flip]:
            if output in conjunctions:
                memory[output][flip] = False

    for con, inputs in conjunctions.items():
        for input in inputs:
            if input in conjunctions:
                memory[input][con] = False
    
    return find_min(flips, conjunctions, broadcasters, states, memory)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
