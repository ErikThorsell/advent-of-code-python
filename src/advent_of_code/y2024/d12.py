"""Solution module for Day 12, 2024"""
from collections import deque
import copy
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import parse_grid_str


def test_1():
    input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    answer = 1930
    assert(solution_1(input) == answer)
    

def test_2():
    input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    answer = 1206
    solution = solution_2(input)
    if solution == answer:
        return
    print(f"-"*25)
    print("! Test 2 Failed !")
    print(f"Answer should be: {answer}")
    print(f"Test 2 returned: {solution}")
    print(f"-"*25)
    assert(False)


def test_2B():
    input = """AAAA
BBCD
BBCC
EEEC"""
    answer = 80
    solution = solution_2(input)
    if solution == answer:
        return
    print(f"-"*25)
    print("! Test 2B Failed !")
    print(f"Answer should be: {answer}")
    print(f"Test 2B returned: {solution}")
    print(f"-"*25)
    assert(False)


def test_2C():
    input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
    answer = 368
    solution = solution_2(input)
    if solution == answer:
        return
    print(f"-"*25)
    print("! Test 2C Failed !")
    print(f"Answer should be: {answer}")
    print(f"Test 2C returned: {solution}")
    print(f"-"*25)
    assert(False)


def dfs(grid, x, y, visited):
    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    plant = grid[x][y]
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()

        if visited[cx][cy]:
            continue
        visited[cx][cy] = True

        area += 1
        plant_per = 4

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant:
                    stack.append((nx, ny))
                    plant_per -= 1
        
        perimeter += plant_per
    
    return area, perimeter


def solution_1(input):
    grid = parse_grid_str(input)
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]
    total_price = 0
    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                area, perimeter = dfs(grid, x, y, visited)
                total_price += area * perimeter
    
    return total_price



def solution_2(input):

    grid = parse_grid_str(input)
    rows = len(grid)
    cols = len(grid[0])

    total = 0
    visited = set()
    for y in range(rows):
        for x in range(cols):

            if (x, y) in visited:
                continue

            queue = deque([(x, y)])
            area = 0
            perimeter = dict()
            while queue:

                cx, cy = queue.popleft()
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))

                area += 1

                for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    nx, ny = cx+dx, cy+dy
                    if 0 <= ny < rows and 0 <= nx < cols and grid[cx][cy] == grid[nx][ny]:
                        queue.append((nx, ny))
                    else:
                        if (dx, dy) not in perimeter:
                            perimeter[(dx, dy)] = set()
                        perimeter[(dx, dy)].add((cx, cy))

            sides = 0
            for vs in perimeter.values():
                seen = set()
                
                for (vx, vy) in vs:
                    if (vx, vy) not in seen:

                        sides += 1
                        queue = deque([(vx, vy)])

                        while queue:

                            cx, cy = queue.popleft()
                            if (cx, cy) in seen:
                                continue
                            seen.add((cx, cy))

                            for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                                nx, ny = cx+dx, cy+dy
                                if (nx, ny) in vs:
                                    queue.append((nx, ny))
            
            total += area*sides
    
    return total


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1()
    print("Test 1 was successful!")
    test_2B()
    print("Test 2B was successful!")
    test_2C()
    print("Test 2C was successful!")
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
