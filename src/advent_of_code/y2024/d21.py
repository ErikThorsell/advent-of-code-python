"""Solution module for Day 21, 2024"""
import copy
import heapq
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """029A
980A
179A
456A
379A"""
    answer = 126384
    assert(solution_1(input) == answer)
    

NUM_PAD = ['789', '456', '123', ' 0A']
CONTROL_PAD = [' ^A', '<v>']
DP = {}


def ints(s):
    return [int(x) for x in re.findall(r"-?\d+", s)]


def get_num_pad(pos):
    r, c = pos
    if not (0 <= r <len(NUM_PAD) and 0 <= c <len(NUM_PAD[r])) or NUM_PAD[r][c]==' ':
        return None
    return NUM_PAD[r][c]


def get_control_pad(pos):
    r, c = pos
    if not (0 <= r <len(CONTROL_PAD) and 0 <= c <len(CONTROL_PAD[r])) or CONTROL_PAD[r][c]==' ':
        return None
    return CONTROL_PAD[r][c]


def apply_num_pad(pos, move):
    if move == 'A':
        return (pos, get_num_pad(pos))
    elif move=='<':
        return ((pos[0], pos[1]-1), None)
    elif move=='^':
        return ((pos[0]-1, pos[1]), None)
    elif move=='>':
        return ((pos[0], pos[1]+1), None)
    elif move=='v':
        return ((pos[0]+1, pos[1]), None)


def apply_control_pad(pos, move):
    if move == 'A':
        return (pos, get_control_pad(pos))
    elif move=='<':
        return ((pos[0], pos[1]-1), None)
    elif move=='^':
        return ((pos[0]-1, pos[1]), None)
    elif move=='>':
        return ((pos[0], pos[1]+1), None)
    elif move=='v':
        return ((pos[0]+1, pos[1]), None)


def solve(code, num_of_pads):
    queue = []
    heapq.heappush(queue, [0, (3, 2), 'A', '', ''])
    SEEN = {}

    while queue:
        d, p1, p2, out, path = heapq.heappop(queue)

        if out==code:
            return d
        if not code.startswith(out):
            continue
        if get_num_pad(p1) is None:
            continue

        state = (p1, p2, out)
        if state in SEEN:
            continue

        SEEN[state] = d

        for move in ['^', '<', 'v', '>', 'A']:
            new_p1 = p1
            new_out = out
            new_p1, output = apply_num_pad(p1, move)

            if output is not None:
                new_out = out + output

            cost_move = cost(move, p2, num_of_pads)
            new_path = path
            heapq.heappush(queue, [d+cost_move, new_p1, move, new_out, new_path])


def cost(ch, prev_move, pads):
    state = (ch, prev_move, pads)

    if state in DP:
        return DP[state]
    if pads==0:
        return 1
    else:

        queue = []
        start_pos = {'^': (0,1), '<': (1,0), 'v': (1,1), '>': (1,2), 'A': (0,2)}[prev_move]
        heapq.heappush(queue, [0, start_pos, 'A', '', ''])

        SEEN = {}
        while queue:
            d, p, prev, out, path = heapq.heappop(queue)

            if get_control_pad(p) is None:
                continue

            if out == ch:
                DP[state] = d
                return d

            elif len(out)>0:
                continue

            seen_state = (p, prev)
            if seen_state in SEEN:
                continue

            SEEN[seen_state] = d

            for move in ['^', '<', 'v', '>', 'A']:
                new_p, output = apply_control_pad(p, move)
                cost_move = cost(move, prev, pads-1)
                new_d = d + cost_move
                new_path = path
                new_out = out

                if output is not None:
                    new_out = new_out + output

                heapq.heappush(queue, [new_d, new_p, move, new_out, new_path])


def solution_1(input):

    codes = input.split("\n")
    
    total_complexity = 0
    for code in codes:
        ans = solve(code, 2)
        lint = ints(code)[0]
        total_complexity += lint * ans
    
    return total_complexity


def solution_2(input):

    codes = input.split("\n")
    
    total_complexity = 0
    for code in codes:
        ans = solve(code, 25)
        lint = ints(code)[0]
        total_complexity += lint * ans
    
    return total_complexity


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
