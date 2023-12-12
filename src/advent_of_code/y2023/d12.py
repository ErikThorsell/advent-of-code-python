"""Solution module for Day 12, 2023"""
import copy
import time

from advent_of_code.utils.fetch import fetch


def test_1():
    inputs = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]
    results = [1, 4, 1, 1, 4, 10]
    for i in range(len(inputs)):
        assert(solution_1(inputs[i]) == results[i])


def test_2():
    input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
    assert(solution_1(input) == 21)


def test_3():
    inputs = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]
    results = [1, 16384, 1, 16, 2500, 506250]
    for i in range(len(inputs)):
        assert(solution_2(inputs[i]) == results[i])


def parse(input):
    output = []
    for line in input.split('\n'):
        springs, groups = line.split()
        groups = list(map(int, groups.split(',')))
        output.append((springs, groups))
    return output


def generate(springs, idx=0):
    if idx >= len(springs):
        yield springs
    else:
        if springs[idx] == '?':
            yield from generate(springs[:idx] + '.' + springs[idx + 1:], idx + 1)
            yield from generate(springs[:idx] + '#' + springs[idx + 1:], idx + 1)
        else:
            yield from generate(springs, idx + 1)


def valid(springs, groups):
    lengths = []
    for s in springs.split("."):
        if "#" in s:
            lengths.append(len(s))
    return lengths == groups


def solution_1(input):

    data = parse(input.strip())

    total_arrangements = 0
    for springs, groups in data:

        possible_configs = generate(springs)

        for pc in possible_configs:
            if valid(pc, groups):
                total_arrangements += 1

    return total_arrangements


def generate_dp(mem, springs, groups, idx=0, block_idx=0, springs_done=0):
    """
    mem: cache
    springs: ???.###
    groups: [1, 1, 3]
    idx: index to keep track of where we are between calls
    block_idx: index to keep track of our position inside a block of springs
    springs_done: number of spring blocks that we have finished
    """
    key = (idx, block_idx, springs_done)

    if key in mem:
        return mem[key]

    if idx == len(springs):
        if springs_done == len(groups):
            mem[key] = 1
        else:
            mem[key] = 0

    elif springs[idx] == '#':
        mem[key] = generate_dp(mem, springs, groups, idx + 1, block_idx + 1, springs_done)

    elif springs[idx] == '.' or springs_done == len(groups):
        if springs_done < len(groups) and block_idx == groups[springs_done]:
            mem[key] = generate_dp(mem, springs, groups, idx + 1, 0, springs_done + 1)
        elif block_idx == 0:
            mem[key] = generate_dp(mem, springs, groups, idx + 1, 0, springs_done)
        else:
            mem[key] = 0

    else:
        hash_combinations = generate_dp(mem, springs, groups, idx + 1, block_idx + 1, springs_done)
        dot_combinations = 0
        if springs_done < len(groups) and block_idx == groups[springs_done]:
            dot_combinations = generate_dp(mem, springs, groups, idx + 1, 0, springs_done + 1)
        elif block_idx == 0:
            dot_combinations = generate_dp(mem, springs, groups, idx + 1, 0, springs_done)

        mem[key] = hash_combinations + dot_combinations

    return mem[key]


def solution_2(input):

    data = parse(input.strip())

    total_arrangements = 0
    for springs, groups in data:

        springs = (springs+'?')*5
        groups = groups*5
        total_arrangements += generate_dp({}, springs, groups)

    return total_arrangements


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print(f"Test 1 successful!")
    test_2()
    print(f"Test 2 successful!")
    test_3()
    print(f"Test 3 successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
