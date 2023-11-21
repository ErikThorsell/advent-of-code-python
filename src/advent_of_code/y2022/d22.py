"""Solution module for Day X, YEAR"""
import copy
from operator import itemgetter
import re
import time
from sys import exit, maxsize

from advent_of_code.utils.coordinates import draw_coordinates_dict
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.parse import split_str_by_separator


DIR = {0: ">",1: "v", 2:"<", 3:"^"}


def parse_map(raw_map):
    """Convert the list of strings into a coordinate dict."""
    map = {}

    y = 1
    x = 1

    for c in raw_map:
        if c == "\n":
            y += 1
            x = 1
            continue

        if c != " ":
            map[(x, y)] = c

        x += 1

    return map


def draw_map(map, moves = {}):
    """Draw the map"""

    x_min = min(map.keys(), key=itemgetter(0))[0]
    y_min = min(map.keys(), key=itemgetter(1))[1]
    x_max = max(map.keys(), key=itemgetter(0))[0]
    y_max = max(map.keys(), key=itemgetter(1))[1]
    print()
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in moves:
                print(DIR[moves[(x, y)]], end="")
            elif (x, y) in map:
                print(map[(x, y)], end="")
            else:
                print(" ", end="")
        print()
    print()


def parse_instr(raw_instr):
    """Parse 10R5L5R10L4R5L5 into 10, R, 5, L, 5, R ..."""
    parsed_list = re.findall(r'(\d+)([RL]?)', raw_instr)
    return [item for sublist in parsed_list for item in sublist if item]


def find_start(map):
    """Find the top left corner of the map."""
    y_min = min(idx[1] for idx in map.keys())
    possible_x = [k for k in map.keys() if k[1] == y_min]
    x_min = min(idx[0] for idx in possible_x)
    return x_min, y_min


def get_limits(map, pos):
    x_target, y_target = pos

    # Extracting the x and y coordinates that are in the same row or column
    same_row = [x for x, y in map.keys() if y == y_target]
    same_column = [y for x, y in map.keys() if x == x_target]

    # Calculating the min and max values
    x_min, x_max = min(same_row), max(same_row)
    y_min, y_max = min(same_column), max(same_column)

    return x_min, x_max, y_min, y_max


def move(map, pos, moves, direction, dist):
    """Move dist steps in current direction, from pos, on map."""

#    print(f"Taking {dist} steps {DIR[direction]}")

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x_min, x_max, y_min, y_max = get_limits(map, pos)

    x, y = pos
    for _ in range(dist):
        moves[(x, y)] = direction
        nx, ny = x+directions[direction][1], y+directions[direction][0]

        # Wrap around
        if nx < x_min:
            nx = x_max
        if nx > x_max:
            nx = x_min
        if ny < y_min:
            ny = y_max
        if ny > y_max:
            ny = y_min
        
        # Check for wall
        if map[(nx, ny)] == "#":
#            print(f"({nx}, {ny}) is a wall!")
            break

        x, y = nx, ny
    
#    print(f"Stopped at ({x}, {y}), facing {DIR[direction]}")
    return (x, y), moves



def turn(direction, turn):
    """Rotate 90 degrees in rotation direction."""
    if turn == "R":
        return (direction+1)%4
    if turn == "L":
        return (direction-1)%4


# Guesses for Part 1
def solution_1(input):
    raw_map = input[0]
    raw_instr = input[1]
    map = parse_map(raw_map)

    sx, sy = find_start(map)
    instr = parse_instr(raw_instr)
#    draw_map(map)

    direction = 0  # E S W N = 0 1 2 3
    pos = (sx, sy)
    moves = {}

#    print(f"Start position: {pos}")

    for i in instr:
#        print("---------------------------------")
        if i.isdigit():
            pos, moves = move(map, pos, moves, direction, int(i))
#            draw_map(map, moves)
        else:
#            print(f"Rotating {i}")
            direction = turn(direction, i)
#            print(f"New direction: {DIR[direction]}")

#    print(f"Final position: {pos} and direction: {direction}")
    
    return 1000 * pos[1] + 4 * pos[0] + direction


# Guesses for Part 2
# 97 | Too small
def solution_2(input):
    pass


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

#    input = """        ...#
#        .#..
#        #...
#        ....
#...#.......#
#........#...
#..#....#....
#..........#.
#        ...#....
#        .....#..
#        .#......
#        ......#.
#
#10R5L5R10L4R5L5"""

    parsed_input = input.split("\n\n")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(parsed_input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
