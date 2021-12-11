from sys import maxsize


def get_adjacent(x, y, dir):
    if dir == 4:
        return [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
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


def get_cell(grid, ix, iy):
    if iy < 0 or iy >= len(grid):
        return maxsize
    if ix < 0 or ix >= len(grid[0]):
        return maxsize
    return grid[iy][ix]
