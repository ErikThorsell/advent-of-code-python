"""Solution module for Day 19, 2021"""
from collections import defaultdict
import operator
from sys import maxsize
import time

from advent_of_code.utils.coordinates import rotate_3d
from advent_of_code.utils.fetch import fetch
from advent_of_code.utils.manhattan import get_manhattan_distance_3d
from advent_of_code.utils.parse import parse_scanners


def solution_1(scanners_to_check):

    # Assume there is a scanner at origo
    scanners = [(0, 0, 0)]
    beacons = set(scanners_to_check.pop(0))

    while scanners_to_check:

        # Place a scanner at origo and presume the first set of beacons are relative this scanner.
        candidate_beacons = scanners_to_check.pop(0)
        match = False

        # There are 24 unique rotations of a cube.
        # We use rotate_3d from utils.coordinates to instantly compute any rotation of a point.
        # We take note of the difference: (known beacon) - (candidate beacon) for all beacons.
        # Each difference is a candidate scanner position.
        for rot_num in range(24):
            candidate_scanner_positions = defaultdict(int)
            for beacon in beacons:
                for candidate_beacon in candidate_beacons:
                    candidate_beacon = rotate_3d(candidate_beacon, rot_num)
                    candidate_scanner_positions[
                        tuple(map(operator.sub, beacon, candidate_beacon))
                    ] += 1

            # If we find that 12 or more known beacons and candidate beacons yield the same csp we have a match.
            # We add the (now confirmed) scanner to our list of scanners and (after changing the rotation and offset)
            # our new found beacons to the set of known beacons.
            for csp, occ in candidate_scanner_positions.items():
                if occ >= 12:
                    match = True
                    scanners.append(csp)
                    for candidate_beacon in candidate_beacons:
                        matching_beacon = rotate_3d(candidate_beacon, rot_num)
                        beacons.add(tuple(map(operator.add, matching_beacon, csp)))

            # No need to keep looking if we have found a valid rotation for this scanner
            # This saves ~2s of exec time
            if match:
                break

        # If we did not find a valid rotation for this scanner, put it last in the list of candidate scanners and continue
        if not match:
            scanners_to_check.append(candidate_beacons)

    return len(beacons), scanners


def solution_2(scanners):
    max_distance = -maxsize
    for s1 in scanners:
        for s2 in scanners:
            max_distance = max(max_distance, get_manhattan_distance_3d(s1, s2))
    return max_distance


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    parsed_input = parse_scanners(input)

    tic = time.perf_counter()
    s1, i2 = solution_1(parsed_input)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(i2)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
