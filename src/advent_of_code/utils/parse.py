from collections import defaultdict
from datetime import datetime, timedelta
import re
from typing import Dict, List, Tuple

import numpy as np


def split_number_by_separator(input: str, sep: str) -> List[int]:
    return [int(s) for s in input.split(sep) if s]


def split_number_by_newline(input: str) -> List[int]:
    return split_number_by_separator(input, "\n")


def split_str_by_separator(input: str, sep: str) -> List[str]:
    return [s for s in input.split(sep) if s]


def split_str_by_newline(input: str) -> List[str]:
    return split_str_by_separator(input, "\n")


def parse_all_numbers(input: str) -> List[int]:
    return [int(n) for n in re.findall(r"-?\d+", input)]


def parse_each_digit(input: str) -> List[List[int]]:
    all_digits = list()
    for row in input.strip().split("\n"):
        all_digits.append([int(rd) for rd in row])
    return all_digits


def parse_sub_commands(input: str) -> List[Tuple[int, int]]:
    rows = split_str_by_newline(input)
    commands = list()
    for row in rows:
        direction = row.split(" ")[0]
        distance = int(row.split(" ")[1])
        commands.append((direction, distance))
    return commands


def parse_graph_edges(input: str) -> List[Tuple[str, str]]:
    rows = split_str_by_newline(input)
    p = re.compile(r"Step (\w) must be finished before step (\w) can begin.")
    edges = list()
    for row in rows:
        m = p.match(row)
        edges.append((m.group(1), m.group(2)))
    return edges


def parse_coordinates(input: str) -> List[Tuple[int, int]]:
    rows = split_str_by_newline(input)
    p = re.compile(r"(\d+),\s*(\d+)")
    coordinates = list()
    for row in rows:
        m = p.match(row)
        coordinates.append((int(m.group(1)), int(m.group(2))))
    return coordinates


def parse_star_vectors(input: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    rows = split_str_by_newline(input)
    points = list()
    for row in rows:
        numbers = parse_all_numbers(row)
        numbers = list(map(int, numbers))
        points.append(((numbers[0], numbers[1]), (numbers[2], numbers[3])))
    return points


def parse_fabric_claims(input: str) -> Dict[int, Tuple[int, int, int, int]]:
    rows = split_str_by_newline(input)
    p = re.compile(r"\#(\d+)\s@\s((\d+),(\d+)):\s((\d+)x(\d+))")
    fabric_claims = dict()
    for row in rows:
        m = p.match(row)
        id = int(m.group(1))
        lm = int(m.group(3))
        tm = int(m.group(4))
        w = int(m.group(6))
        h = int(m.group(7))
        fabric_claims[id] = (lm, tm, w, h)
    return fabric_claims


def parse_guard_records(input: str) -> Dict[int, Dict[datetime, bool]]:
    unsorted_rows = split_str_by_newline(input)
    rows = sorted(unsorted_rows)

    p_time = re.compile(r"\[(\d+-\d+-\d+\s\d\d:\d\d)\]")
    p_guard = re.compile(r"#(\d+)")

    last_timestamp = None
    guard_tracker = defaultdict(dict)
    guard_id = None

    for row in rows:
        timestamp = datetime.strptime(p_time.match(row).group(1), "%Y-%m-%d %H:%M")

        if p_guard.search(row):
            guard_id = int(p_guard.search(row).group(1))
            guard_tracker[guard_id][timestamp] = True
            last_timestamp = timestamp

        elif "falls asleep" in row:
            duration = timestamp - last_timestamp
            for d in range(duration.seconds // 60):
                guard_tracker[guard_id][last_timestamp + timedelta(seconds=d * 60)] = True
            last_timestamp = timestamp

        elif "wakes up" in row:
            duration = timestamp - last_timestamp
            for d in range(duration.seconds // 60):
                guard_tracker[guard_id][last_timestamp + timedelta(seconds=d * 60)] = False
            last_timestamp = timestamp

    return guard_tracker


def parse_grid(input: str):
    rows = split_str_by_newline(input)
    grid = np.zeros((len(rows), len(rows[0])))
    for rx, row in enumerate(rows):
        for cx, col in enumerate(row):
            grid[rx, cx] = int(col)
    return grid


def parse_grid_str(input: str):
    rows = split_str_by_newline(input)
    grid = []
    for rx, row in enumerate(rows):
        grid.append([])
        for _, col in enumerate(row):
            grid[rx].append(col)
    return grid


def parse_mover_in_grid(input):
    rows = split_str_by_newline(input)

    grid = {}
    poi = (-1, -1)
    dir = "."

    for rx, row in enumerate(rows):
        for cx, col in enumerate(row):
            if col == "#":
                grid[(cx, rx)] = col
            if col in ["<", ">", "v", "^"]:
                poi = (cx, rx)
                dir = col

    return grid, poi, dir



def parse_bingo(input: str):
    def parse_bingo_boards(rows):
        str_boards = split_str_by_separator(rows, "\n\n")
        boards = list()
        for str_board in str_boards:
            board = np.zeros((5, 5))
            for rx, row in enumerate(str_board.split("\n")):
                for cx, col in enumerate(row.split()):
                    board[rx, cx] = int(col)
            boards.append(board)

        return boards

    order = [int(n) for n in input.split("\n")[0].split(",")]
    boards = parse_bingo_boards("\n".join(input.split("\n")[1:]).strip())
    return order, boards


def parse_line_segments(input: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    rows = split_str_by_newline(input)
    line_segments = list()
    for row in rows:
        numbers = parse_all_numbers(row)
        line_segments.append(((numbers[0], numbers[1]), (numbers[2], numbers[3])))
    return line_segments


def parse_seven_segment(input: str) -> List[Tuple[str, str]]:
    rows = split_str_by_newline(input)
    signals = list()
    for row in rows:
        patterns = row.split("|")[0].strip()
        output = row.split("|")[1].strip()
        signals.append((patterns, output))
    return signals


def parse_folding(input: str):
    coordinates, instructions = split_str_by_separator(input, "\n\n")
    return parse_coordinates(coordinates), split_str_by_newline(instructions)


def parse_polymer(input: str):
    template, rules = split_str_by_separator(input, "\n\n")
    rules = {x.split("->")[0].strip(): x.split("->")[1].strip() for x in split_str_by_newline(rules)}
    return template.strip(), rules


def parse_scanners(input: str):
    raw_scanners = split_str_by_separator(input, "\n\n")
    scanners = []
    for scanner in raw_scanners:
        beacons = []
        for line in scanner.split("\n")[1:]:  # get rid of --- scanner x ---
            beacons.append(tuple([int(c) for c in line.split(",")]))
        scanners.append(beacons)
    return scanners


def parse_cuboids(input: str):
    res = list()
    rows = split_str_by_newline(input)

    for instr in rows:
        mode, cuboids = instr.split()
        on = mode == "on"

        xs = parse_all_numbers(cuboids.split(",")[0])
        ys = parse_all_numbers(cuboids.split(",")[1])
        zs = parse_all_numbers(cuboids.split(",")[2])

        res.append((on, (xs, ys, zs)))

    return res


def parse_sea_cucumbers(input: str):
    east = dict()
    south = dict()
    for rx, row in enumerate(split_str_by_newline(input)):
        for cx, cell in enumerate(row):
            if cell == ">":
                east[(cx, rx)] = cell
            elif cell == "v":
                south[(cx, rx)] = cell
    return east, south


def parse_crates(input: str):
    raw_crates, raw_instructions = input.split("\n\n")

    stacks = defaultdict(list)
    for row in raw_crates.split("\n"):
        for idx in range(1, len(row), 4):
            if row[idx].isalpha():
                crate_idx = (idx // 4) + 1
                stacks[crate_idx] = [row[idx]] + stacks[crate_idx]

    instructions = list()
    for row in raw_instructions.split("\n"):
        q, f, t = list(map(int, re.findall(r"\d+", row)))
        instructions.append((q, f, t))

    return stacks, instructions
