"""Solution module for Day 19, 2022"""
import copy
import time

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_all_numbers, split_str_by_newline


def parse(blueprints):
    """
    returns:
    (
        blueprint id,
        ore cost for ore robot,
        ore cost for clay robot,
        ore cost for obs robot,
        clay cost for obs robot,
        ore cost for geode robot,
        obs cost for geode robot,
    )
    """
    ingredients = list()
    for blueprint in blueprints:
        ingredients.append(tuple(parse_all_numbers(blueprint)))
    return ingredients


def actions(blueprint, ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, iterations):

    # Heuristic
    # If it's possible to build a Geode Robot, do only that.
    # If it's possible to build an Obsidian Robot, do only that.
    # If the amount of ore in a state is more than twice of any ore cost in the blueprint, ignore the state.
    # If the number of ore robots in a state is more than twice of any ore cost in the blueprint, ignore the state.
    # Same for clay, as we did for ore.

    # It was enough to just go on max_ore for the test input, but for the real input I had to multiply by 2.
    # Maybe a smaller factor would have worked but 2 yielded a reasonable exec time so I'm content here.
    max_ore = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5]) * 2
    max_clay = blueprint[4] * 2

    new_states = list()

    # If it is possible to build a Geode Robot, do only that!
    if ore >= blueprint[5] and obs >= blueprint[6]:
        new_states.append(
            (
                ore - blueprint[5] + ore_r,
                clay + clay_r,
                obs - blueprint[6] + obs_r,
                geode + geode_r,
                ore_r,
                clay_r,
                obs_r,
                geode_r + 1,
                iterations - 1,
            )
        )
        return new_states

    # If it is possible to build an Obsidian Robot, do only that!
    if ore >= blueprint[3] and clay >= blueprint[4]:
        new_states.append(
            (
                ore - blueprint[3] + ore_r,
                clay - blueprint[4] + clay_r,
                obs + obs_r,
                geode + geode_r,
                ore_r,
                clay_r,
                obs_r + 1,
                geode_r,
                iterations - 1,
            )
        )
        return new_states

    # Clay robot
    if ore >= blueprint[2]:
        new_states.append(
            (
                ore - blueprint[2] + ore_r,
                clay + clay_r,
                obs + obs_r,
                geode + geode_r,
                ore_r,
                clay_r + 1,
                obs_r,
                geode_r,
                iterations - 1,
            )
        )

    # Ore robot
    if ore >= blueprint[1]:
        new_states.append(
            (
                ore - blueprint[1] + ore_r,
                clay + clay_r,
                obs + obs_r,
                geode + geode_r,
                ore_r + 1,
                clay_r,
                obs_r,
                geode_r,
                iterations - 1,
            )
        )

    # It's always possible to do nothing and just gather more resources
    new_states.append(
        (
            ore + ore_r,
            clay + clay_r,
            obs + obs_r,
            geode + geode_r,
            ore_r,
            clay_r,
            obs_r,
            geode_r,
            iterations - 1,
        )
    )

    # Filter out the states where ore goes bananas
    new_states = [state for state in new_states if state[0] <= max_ore and state[4] <= max_ore]
    new_states = [state for state in new_states if state[1] <= max_clay and state[5] <= max_clay]
    return new_states


def bfs(blueprint, iterations=24):
    ore = clay = obs = geode = 0
    ore_r = 1
    clay_r = obs_r = geode_r = 0

    state = (ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, iterations)

    queue = [state]
    visited = set()

    max_geode = 0
    while queue:
        state, queue = queue[0], queue[1:]

        ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, iterations = state
        max_geode = max(max_geode, geode)

        if iterations == 0:
            continue

        for next_state in actions(blueprint, ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, iterations):

            if next_state in visited:
                continue

            visited.add(next_state)
            queue.append(next_state)

    return max_geode


def solution_1(input):
    blueprints = parse(input)

    quality_levels = list()
    for blueprint in blueprints:
        geode_production = bfs(blueprint, 24)
        quality_level = blueprint[0] * geode_production
        quality_levels.append(quality_level)

    return sum(quality_levels)


def solution_2(input):
    blueprints = parse(input)

    geode_production = 1
    for blueprint in blueprints[:3]:
        geode_production *= bfs(blueprint, 32)

    return geode_production


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
