"""Solution module for Day 15, 2023"""
from collections import defaultdict
import copy
import re
import time

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    answer = 1320
    assert(solution_1(input) == answer)
    

def test_2():
    input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    answer = 145
    assert(solution_2(input) == answer)


def hash(step):
    current = 0
    for c in step:
        current += ord(c)
        current *= 17
        current = current % 256
    return current


def extract_components(step):
    letters = re.findall(r'[a-zA-Z]+', step)
    special_chars = re.findall(r'[^a-zA-Z0-9]', step)
    numbers = re.findall(r'\d+', step)

    letters = ''.join(letters)
    special_chars = ''.join(special_chars)
    numbers = ''.join(numbers)

    return letters, special_chars, numbers


def solution_1(input):
    seq = input.split(",")
    sum = 0
    for step in seq:
        sum += hash(step)
    return sum


def solution_2(input):
    seq = input.split(",")
    boxes = defaultdict(dict)

    for step in seq:
        label, op, num = extract_components(step)
        box_idx = hash(label)
        current_box = boxes[box_idx]

        if op == "-" and label in current_box:
            del current_box[label]
             
        elif op == "=":
            current_box[label] = num
            boxes[box_idx] = current_box
            
    sum = 0
    for box in boxes:
        for idx, focal in enumerate(boxes[box].values()):
            sum += (int(box) + 1) * (int(idx) + 1)* int(focal)

    return sum


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
