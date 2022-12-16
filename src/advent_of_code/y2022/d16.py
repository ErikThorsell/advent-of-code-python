"""Solution module for Day 16, 2022"""
import copy
from collections import defaultdict
import re
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(lines):
    schema = dict()
    for line in lines:
        m = re.findall(r"Valve (\w+) has flow rate=(-?\d+); tunnel[s]? lead[s]? to valve[s]? (\w+)((,\s*\w+)*)", line)
        v = m[0][0]
        flow = int(m[0][1])
        outs = [o.strip() for o in " ".join(m[0][2:-1]).split(",")]  # idk what happened here ...
        schema[v] = [flow, outs]
    return schema


def solution_1(input):
    scan_output = parse(input)
    HIGHEST_VALVE_FLOW = max(scan_output[v][0] for v in scan_output)

    states = defaultdict(int)
    states["AA", tuple(), 0] = 0

    for _ in range(30):

        new_states = defaultdict(int)
        current_max_flow = max(states.values())

        for (valve, path, path_flow), path_flow_total in states.items():

            # If not even the valve with highest flow can contribute to a higher max flow, we skip the state.
            # This works wonders for the execution time, but am I just lucky this works?
            if path_flow_total + HIGHEST_VALVE_FLOW <= current_max_flow:
                continue

            valve_flow = scan_output[valve][0]

            # No use opening a valve twice nor to spend time on no-flow valves
            # But if we open the valve we add a state where the valve is opened and its contribution is added to the
            # path of the flow.
            if not valve in path and valve_flow > 0:
                new_state = (valve, tuple(list(path) + [valve]), path_flow + valve_flow)
                new_states[new_state] = max(new_states[new_state], path_flow_total + path_flow)

            # Update the inflow in all neighbouring valves
            for valve_neighb in scan_output[valve][1]:
                new_state = (valve_neighb, path, path_flow)
                new_states[new_state] = max(new_states[new_state], path_flow_total + path_flow)

        states = new_states

    print()

    return max(states.values())


def solution_2(input):

    scan_output = parse(input)
    HIGHEST_VALVE_FLOW = max(scan_output[v][0] for v in scan_output)

    states = defaultdict(int)
    states["AA", "AA", tuple(), 0] = 0

    for _ in range(26):

        new_states = defaultdict(int)
        current_max_flow = max(states.values())

        for (my_valve, e_valve, path, path_flow), path_flow_total in states.items():

            # Same check as for part 1
            if path_flow_total + HIGHEST_VALVE_FLOW <= current_max_flow:
                continue

            my_flow = scan_output[my_valve][0]
            e_flow = scan_output[e_valve][0]

            if my_valve not in path and my_flow > 0 and e_valve not in path and e_flow > 0 and my_valve != e_valve:
                new_state = (my_valve, e_valve, tuple(list(path) + [my_valve, e_valve]), path_flow + my_flow + e_flow)
                new_states[new_state] = max(new_states[new_state], path_flow_total + path_flow)

            if my_valve not in path and my_flow > 0:
                for e_valve_neighb in scan_output[e_valve][1]:
                    new_state = (my_valve, e_valve_neighb, tuple(list(path) + [my_valve]), path_flow + my_flow)
                    new_states[new_state] = max(new_states[new_state], path_flow_total + path_flow)

            if e_valve not in path and e_flow > 0:
                for my_valve_neighb in scan_output[my_valve][1]:
                    new_state = (my_valve_neighb, e_valve, tuple(list(path) + [e_valve]), path_flow + e_flow)
                    new_states[new_state] = max(new_states[new_state], path_flow_total + path_flow)

            # Update the inflow in all neighbouring valves
            for my_valve_neighb in scan_output[my_valve][1]:
                for e_valve_neighb in scan_output[e_valve][1]:
                    new_state = (my_valve_neighb, e_valve_neighb, path, path_flow)
                    new_states[new_state] = max(new_states[new_state], path_flow_total + path_flow)

        states = new_states

    return max(states.values())


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
