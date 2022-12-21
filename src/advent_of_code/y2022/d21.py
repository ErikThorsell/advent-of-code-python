"""Solution module for Day 21, 2022"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_newline


def parse(lines, pt=1):
    monkeys = dict()

    for line in lines:
        monkey, operation = line.split(":")

        monkey = monkey.strip()
        operation = operation.strip()

        if operation.isnumeric():
            monkeys[monkey] = (True, int(operation))

        else:
            l, op, r = operation.split()
            if monkey == "root" and pt == 2:
                op = "=="
            monkeys[monkey] = (False, l, r, op)

    return monkeys


# Guesses for Part 1
#  99 | Too large
def solution_1(input):
    monkeys = parse(input)

    while not all(m[0] for m in monkeys.values()):

        for monkey, operation in monkeys.items():

            if operation[0]:
                continue

            left = operation[1]
            right = operation[2]

            if monkeys[left][0] and monkeys[right][0]:
                expr = f"{monkeys[left][1]} {operation[3]} {monkeys[right][1]}"
                ans = eval(expr)
                monkeys[monkey] = (True, ans)

    return monkeys["root"][1]


# Guesses for Part 2
# 97 | Too small
def solution_2(input):

    humn_num = 0

    while True:
        monkeys = parse(input, 2)
        monkeys["humn"] = (True, humn_num)

        while not all(m[0] for m in monkeys.values()):

            for monkey, operation in monkeys.items():

                if operation[0]:
                    continue

                left = operation[1]
                right = operation[2]

                if monkeys[left][0] and monkeys[right][0]:

                    if monkey == "root":
                        diff = monkeys[left][1] - monkeys[right][1]

                    expr = f"{monkeys[left][1]} {operation[3]} {monkeys[right][1]}"
                    ans = eval(expr)
                    monkeys[monkey] = (True, ans)

        if monkeys["root"][1]:
            return monkeys["humn"][1]

        if abs(diff) > 10000:
            humn_num += diff
        else:
            humn_num += 1


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    #    input = """root: pppw + sjmn
    # dbpl: 5
    # cczh: sllz + lgvd
    # zczc: 2
    # ptdq: humn - dvpt
    # dvpt: 3
    # lfqf: 4
    # humn: 5
    # ljgn: 2
    # sjmn: drzm * dbpl
    # sllz: 4
    # pppw: cczh / lfqf
    # lgvd: ljgn * ptdq
    # drzm: hmdt - zczc
    # hmdt: 32"""
    parsed_input = split_str_by_newline(input)

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
