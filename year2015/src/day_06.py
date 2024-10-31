import numpy as np


def part_1(instructions: str) -> int:
    grid = np.zeros((1000, 1000), dtype=bool)
    for instruction in instructions.splitlines():
        line = instruction.split()
        xs, ys = map(int, line[-3].split(","))  # xs, ys for "start"
        xe, ye = map(int, line[-1].split(","))  # xe, ye for "end"

        sub_grid = grid[xs: xe + 1, ys: ye + 1]
        if line[0] == "turn":
            sub_grid.fill(line[1] == "on")
        else:
            np.logical_not(sub_grid, out=sub_grid)
    return grid.sum()


def part_2(instructions: str) -> int:
    grid = np.zeros((1000, 1000), dtype=int)
    for instruction in instructions.splitlines():
        line = instruction.split()
        xs, ys = map(int, line[-3].split(","))  # xs, ys for "start"
        xe, ye = map(int, line[-1].split(","))  # xe, ye for "end"

        sub_grid = grid[xs: xe + 1, ys: ye + 1]
        if line[0] == "turn":
            sub_grid += 1 if line[1] == "on" else -1
            sub_grid[sub_grid < 0] = 0
        else:
            sub_grid += 2
    return grid.sum()
