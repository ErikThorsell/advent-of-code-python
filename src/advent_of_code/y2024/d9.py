"""Solution module for Day 9, 2024"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1():
    input = """2333133121414131402"""
    answer = 1928
    assert(solution_1(input) == answer)
    

def test_2():
    input = """2333133121414131402"""
    answer = 2858
    assert(solution_2(input) == answer)


def move_blocks(disk_map):
    n = len(disk_map)
    
    leftmost_free_index = 0
    rightmost_file_index = n - 1

    while leftmost_free_index < rightmost_file_index:

        while disk_map[leftmost_free_index] != None:
            leftmost_free_index += 1

        while disk_map[rightmost_file_index] == None:
            rightmost_file_index -= 1

        if leftmost_free_index < rightmost_file_index:
            disk_map[leftmost_free_index], disk_map[rightmost_file_index] = disk_map[rightmost_file_index], None

    return [x for x in disk_map if x is not None]


def parse(input):
    disk_map = []
    for idx, num in enumerate(input):
        for _ in range(int(num)):
            if idx % 2 == 0:
                disk_map.append(idx//2)
            else:
                disk_map.append(None)
    return disk_map


def solution_1(input):
    disk_map = parse(input)
    disk_map = move_blocks(disk_map)
    checksum = sum(idx*num for idx, num in enumerate(disk_map))
    return checksum


def move_files(chunky_map):
    return chunky_map

def parse_chunks(input):
    chunky_map = []
    for idx, num in enumerate(input):
        if idx % 2 == 0:
            chunky_map.append(str(idx//2)*int(num))
        else:
            chunky_map.extend([None]*int(num))
    return chunky_map


def solution_2(input):
    chunky_map = parse_chunks(input)
    chunky_map = move_files(chunky_map)
    return 0


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
#
#    tic = time.perf_counter()
#    s2 = solution_2(copy.deepcopy(input))
#    toc = time.perf_counter()
#    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
#