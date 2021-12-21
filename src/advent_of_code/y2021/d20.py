"""Solution module for Day 20, 2021"""
from math import sqrt
from operator import countOf, itemgetter
import time

from advent_of_code.utils.fetch import fetch


def image_to_dict(raw_image):
    image = {}
    for iy, row in enumerate(raw_image.split()):
        for ix, cell in enumerate(row.strip()):
            image[ix, iy] = cell
    return image


def enhance(image, algorithm, iterations):

    for i in range(iterations):

        new_image = {}
        x_min = min(image.keys(), key=itemgetter(0))[0]
        y_min = min(image.keys(), key=itemgetter(1))[1]
        x_max = max(image.keys(), key=itemgetter(0))[0]
        y_max = max(image.keys(), key=itemgetter(1))[1]

        for y in range(y_min - 2, y_max + 2 + 1):
            for x in range(x_min - 2, x_max + 2 + 1):
                new_image[(x, y)] = determine_pixel(image, (x, y), algorithm, i)

        image = new_image.copy()

    return image


def determine_pixel(image, cell, algorithm, iteration):
    pixels = ""
    for y in range(cell[1] - 1, cell[1] + 2):
        for x in range(cell[0] - 1, cell[0] + 2):
            if (x, y) in image:
                pixels += image[(x, y)]
            else:
                pixels += "#" if iteration % 2 != 0 else "."

    binary = pixels.replace(".", "0").replace("#", "1")
    decimal = int(binary, 2)
    return algorithm[decimal]


def count_bright_pixels(image):
    count = 0
    for pixel in image:
        if image[pixel] == "#":
            count += 1
    return count


def solution_1(image, algorithm, iterations=2):
    image = image_to_dict(image)
    image = enhance(image, algorithm, iterations)
    return countOf(image.values(), "#")


def solution_2(image, algorithm, iterations=50):
    image = image_to_dict(image)
    image = enhance(image, algorithm, iterations)
    return countOf(image.values(), "#")


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)
    algorithm = input.split("\n\n")[0].strip()
    assert len(algorithm) == 512

    image = input.split("\n\n")[1].strip()

    tic = time.perf_counter()
    s1 = solution_1(image, algorithm)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(image, algorithm)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")
