"""Solution module for Day 4, 2024"""
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_grid_str


def test_1():
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    answer = 18
    assert(solution_1(input) == answer)
    

def test_2():
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    answer = 9
    assert(solution_2(input) == answer)



def word_search(grid, x, y, woi="XMAS"):

    def is_in(grid, x, y):
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

    directions = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
    ]
    
    found = 0
    
    for dx, dy in directions:
        match = True
        for i in range(len(woi)):
            nx, ny = x + i * dx, y + i * dy
            if not is_in(grid, nx, ny) or grid[nx][ny] != woi[i]:
                match = False
                break
        
        if match:
            found += 1
    
    return found


def solution_1(input):
    grid = parse_grid_str(input)

    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[x][y] == "X":
                total += word_search(grid, x, y)
    
    return total


def is_cross(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    if 0 < y < rows-1 and 0 < x < cols-1:
        ltr = grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]
        rtl = grid[x+1][y-1] + grid[x][y] + grid[x-1][y+1]
        if ltr in ["MAS", "SAM"] and rtl in ["MAS", "SAM"]:
            return True
    

def solution_2(input):
    grid = parse_grid_str(input)

    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[x][y] == "A" and is_cross(grid, x, y):
                total += 1

    return total


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
