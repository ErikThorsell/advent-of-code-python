from heapq import heapify, heappop, heappush
from sys import maxsize


def get_adjacent(x, y, dir):
    if dir == 4:
        return [
            (x, y - 1),  # above
            (x, y + 1),  # below
            (x - 1, y),  # left
            (x + 1, y),  # right
        ]
    if dir == 8:
        return [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 1),
        ]


# Courtesy of Mr C Ohlsson
# Left, Right, Up, Down
def get_rays(grid, y, x):
    return [
        [grid[y][dx] for dx in range(x)],
        [grid[y][dx] for dx in range(x + 1, len(grid[0]))],
        [grid[dy][x] for dy in range(y)],
        [grid[dy][x] for dy in range(y + 1, len(grid))],
    ]


# Courtesy of Mr C Ohlsson
# Left, Right, Up, Down
def get_rays_from_inside(grid, y, x):
    return [
        [grid[y][dx] for dx in range(x)][::-1],
        [grid[y][dx] for dx in range(x + 1, len(grid[0]))],
        [grid[dy][x] for dy in range(y)][::-1],
        [grid[dy][x] for dy in range(y + 1, len(grid))],
    ]


def print_grid(grid):
    for row in grid:
        print("".join(row))


def get_cell(grid, ix, iy):
    if iy < 0 or iy >= len(grid):
        return maxsize
    if ix < 0 or ix >= len(grid[0]):
        return maxsize
    return grid[iy][ix]


def dijkstra_grid(grid, start, goal):

    heap = [(0, start)]
    heapify(heap)
    distances = {}

    while heap:

        dist, node = heappop(heap)

        if node == goal:
            return int(dist)

        for (x, y) in get_adjacent(node[0], node[1], 4):
            if get_cell(grid, x, y) < maxsize:
                n_dist = dist + grid[x, y]
                if (x, y) in distances and distances[(x, y)] <= n_dist:
                    continue
                distances[(x, y)] = n_dist
                heappush(heap, (n_dist, (x, y)))
