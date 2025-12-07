"""Solution module for Day 15, 2024"""
from collections import deque
import copy
from operator import itemgetter
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1A():
    input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    answer = 2028
    assert(solution_1(input) == answer)
    

def test_1B():
    input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    answer = 10092
    assert(solution_1(input) == answer)


def test_2A():
    input = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""
    answer = 100+5+200+7+300+6
    assert(solution_2(input) == answer)

def test_2B():
    input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    answer = 9021
    assert(solution_2(input) == answer)


def parse(input_text, p2=False):
    warehouse, moves = input_text.strip().split("\n\n")

    transformed_lines = []
    if p2:
        for line in warehouse.split("\n"):
            new_line = []
            for char in line:
                if char == '#':
                    new_line.append('##')
                elif char == 'O':
                    new_line.append('[]')
                elif char == '.':
                    new_line.append('..')
                elif char == '@':
                    new_line.append('@.')
                else:
                    new_line.append(char)
            transformed_lines.append(''.join(new_line))

        warehouse = "\n".join(transformed_lines)

    grid = {}
    robot = (-1, -1)
    for y, row in enumerate(warehouse.split("\n")):
        for x, col in enumerate(row):
            if col != "." and col != "@":
                grid[(x, y)] = col
            if col == "@":
                robot = (x, y)

    ms = ''.join(line for line in moves if all(char in '<>^v' for char in line))

    return grid, robot, ms


def visualise(grid, robot):
    x_min = min(grid.keys(), key=itemgetter(0))[0]
    y_min = min(grid.keys(), key=itemgetter(1))[1]
    x_max = max(grid.keys(), key=itemgetter(0))[0]
    y_max = max(grid.keys(), key=itemgetter(1))[1]
    result = ""
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in grid:
                result += grid[(x, y)]
            elif (x, y) == robot:
                result += "@"
            else:
                result += "."
        result += "\n"
    
    print(result)


def get_pile(grid, start, dir):

    pile = []
    it = 0

    while True:
        x, y = start[0]+dir[0]*it, start[1]+dir[1]*it
        if (x, y) in grid and grid[(x, y)] == "O":
            pile.append((x, y))
            it += 1
        else:
            break

    return pile


def simulate(grid, robot, move):
    dirs = {"v": (0, 1), ">": (1, 0), "^": (0, -1), "<": (-1, 0)}

    rx, ry = robot
    dx, dy = dirs[move]
    nx, ny = rx+dx, ry+dy

    if (nx, ny) not in grid:
        return grid, (nx, ny)
    
    if grid[(nx, ny)] == "#":
        return grid, robot

    if grid[(nx, ny)] == "O":
        bx, by = nx+dx, ny+dy

        if (bx, by) not in grid:
            del grid[(nx, ny)]
            grid[(bx, by)] = "O"
            return grid, (nx, ny)

        if grid[(bx, by)] == "#":
            return grid, robot

        if grid[(bx, by)] == "O":

            pile = get_pile(grid, (nx, ny), dirs[move])
            px, py = pile[-1]

            if (px+dx, py+dy) not in grid:
                for box in pile:
                    del grid[box]
                for bbx, bby in pile:
                    grid[(bbx+dx, bby+dy)] = "O"
                return grid, (nx, ny)
            
            return grid, robot


def calc(grid):
    total = 0
    for pos in grid:
        if grid[pos] == "O":
            total += pos[0] + pos[1]*100
    return total


def solution_1(input):
    grid, robot, moves = parse(input)
    for move in moves:
        grid, robot = simulate(grid, robot, move)
    return calc(grid)


def simulate_ext(grid, robot, move):
    dirs = {"v": (0, 1), ">": (1, 0), "^": (0, -1), "<": (-1, 0)}

    rx, ry = robot
    dx, dy = dirs[move]
    nx, ny = rx+dx, ry+dy

    if (nx, ny) not in grid:
        return grid, (nx, ny)
    
    if grid[(nx, ny)] == "#":
        return grid, robot

    if grid[(nx, ny)] in "[]":

        queue = deque([(rx, ry)])
        seen = set()
        ok = True
        while queue:

            nx, ny = queue.popleft()

            if (nx, ny) in seen:
                continue
            seen.add((nx, ny))

            bx, by = nx+dx, ny+dy

            if grid[(bx, by)] == "[":
                queue.append((bx, by))
                queue.append((bx+1, by))
            if grid[(bx, by)] == "]":
                queue.append((bx, by))
                queue.append((bx-1, by))
        
        while seen:
            for nx, ny in sorted(seen):
                bx, by = nx+dx, ny+dy
                if (bx, by) not in seen:
                    grid[(bx, by)] = grid[(nx, ny)]
                    del grid[(nx, ny)]
                    seen.remove((nx, ny))
        
        return grid, robot


def calc_ext(grid):
    total = 0
    for pos in grid:
        if grid[pos] == "[":
            total += pos[0] + pos[1]*100
    return total


def solution_2(input):
    grid, robot, moves = parse(input, True)
    for move in moves:
        print()
        visualise(grid, robot)
        print(f"Move: {move}")
        grid, robot = simulate_ext(grid, robot, move)
    return calc_ext(grid)


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1A()
    print("Test 1A was successful!")
    test_1B()
    print("Test 1B was successful!")
    test_2A()
    print("Test 2A was successful!")
    test_2B()
    print("Test 2B was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
