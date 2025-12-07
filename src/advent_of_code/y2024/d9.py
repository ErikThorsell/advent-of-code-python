"""Solution module for Day 9, 2024"""
from collections import defaultdict
import copy
import heapq
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
    return sum(idx*num for idx, num in enumerate(disk_map))


def parse_chunk(input):
    lengths = [int(num) for num in input]

    filled_grid = {}
    gaps = defaultdict(lambda: [])

    cur_pos = 0
    for i,num in enumerate(lengths):
        if i%2 == 0:
            filled_grid[i//2] = [cur_pos,num]
        else:
            if num > 0:
                heapq.heappush(gaps[num],cur_pos)
        cur_pos += num

    return filled_grid, gaps


def move_files(files, gaps):

    for idx in sorted(files.keys(), reverse=True):
        file_start, file_len = files[idx]

        potential_gaps = sorted([[gaps[gap_len][0], gap_len] for gap_len in gaps if gap_len >= file_len])
        if potential_gaps:
            gap_start, gap_len = potential_gaps[0]

            if file_start > gap_start:
                files[idx] = [gap_start, file_len]
                remaining_gap_len = gap_len - file_len
                heapq.heappop(gaps[gap_len])

                if not gaps[gap_len]:
                    del gaps[gap_len]

                if remaining_gap_len:
                    heapq.heappush(gaps[remaining_gap_len], gap_start + file_len)
                    
    return files


def solution_2(input):
    files, gaps = parse_chunk(input)
    files = move_files(files, gaps)
    return sum(num * (length * (2 * start + length - 1) // 2) for num, (start, length) in files.items())


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
