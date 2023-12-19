"""Solution module for Day 19, 2023"""
import copy
from math import prod
import re
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
    answer = 19114
    assert(solution_1(input) == answer)
    

def test_2():
    input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
    answer = 167409079868000
    assert(solution_2(input) == answer)


def test_3():
    input = """in{x<4000:R,in2}
in2{m<4000:R,in3}
in3{a<4000:R,in4}
in4{s<4000:R,A}

{x=787,m=2655,a=1222,s=2876}"""
    answer = 1
    assert(solution_2(input) == answer)


def test_4():
    input = """in{x>1:R,in1}
in1{m>1:R,in2}
in2{a>1:R,in3}
in3{s>1:R,A}

{x=787,m=2655,a=1222,s=2876}"""
    answer = 1
    assert(solution_2(input) == answer)


def parse(input, part=1):
    LETTER_TO_INDEX = {'x': 0, 'm': 1, 'a': 2, 's': 3}
    r_workflows, r_parts = input.split("\n\n")

    workflows = {}
    for wf in r_workflows.split("\n"):
        name = re.findall(r'(.+?)\{', wf)[0]
        inside = re.findall(r'{(.+?)}', wf)[0]
        r_rules = inside.split(",")

        rules = []
        for rule in r_rules:
            if "<" in rule or ">" in rule:
                r, c = rule.split(":")
                rules.append((r[0], r[1], int(r[2:]), c))
            else:
                rules.append(("", "", 0, rule))

        workflows[name] = rules

    parts = []
    for part in r_parts.split("\n"):
        sub_parts = {}
        for r in part[1:-1].split(","):
            n, v = r.split("=")
            sub_parts[n] = int(v)
        parts.append(sub_parts)
    
    return workflows, parts


def evaluate_condition(letter, operator, value, part):
    if operator == "":
        return True
    if operator == '>':
        return part[letter] > value
    elif operator == '<':
        return part[letter] < value
    return False


def process_part(part, workflow, workflows):
    for (letter, operator, value, target) in workflows[workflow]:
        if evaluate_condition(letter, operator, value, part):
            if target in ['A', 'R']:
                return target
            return process_part(part, target, workflows)


def evaluate_boundaries(workflow, boundaries, queue, valid):
    for (letter, comparison, value, target) in workflow:

        if letter in boundaries:
            low_boundary, high_boundary = boundaries[letter]

        if comparison == '<':
            min, max = low_boundary, value-1
            new_low, new_high = value, high_boundary

        elif comparison == '>':
            min, max = value+1, high_boundary
            new_low, new_high = low_boundary, value

        else:
            min, max = low_boundary, high_boundary
            new_low, new_high = 1, 0

        if min <= max:
            limits = {l: (min, max) if l == letter else boundaries[l] for l in boundaries}
            if target == 'A':
                valid.append(limits)
            elif target != 'R':
                queue.append((target, limits))

        if new_low <= new_high:
            boundaries = {l: (new_low, new_high) if l == letter else boundaries[l] for l in boundaries}
    
    return boundaries, valid, queue


def solution_1(input):
    workflows, parts = parse(input)
    return sum(sum(part.values()) for part in parts if process_part(part, "in", workflows) == "A")


def solution_2(input):
    workflows, _ = parse(input)

    queue = [('in', {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
    valid = []

    while queue:
        id, boundaries = queue.pop()
        workflow = workflows[id]
        boundaries, valid, queue = evaluate_boundaries(workflow, boundaries, queue, valid)

    return sum(prod(max - min + 1 for min, max in boundary.values()) for boundary in valid)



def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_3()
    print("Test 3 was successful!")
    test_4()
    print("Test 4 was successful!")
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
