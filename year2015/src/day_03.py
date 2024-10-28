def part_1(directions: str) -> int:
    directions = directions.strip()
    grid = {(0, 0)}
    x = y = 0
    for direction in directions:
        x, y = [sum(xx) for xx in zip((x, y), _dir_to_coord[direction])]
        grid.add((x, y))

    return len(grid)


def part_2(directions: str) -> int:
    directions = directions.strip()
    grid = {(0, 0)}
    xs = ys = xr = yr = 0  # s for Santa, r for Robo-Santa
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            xs, ys = [sum(x) for x in zip((xs, ys), _dir_to_coord[direction])]
        else:
            xr, yr = [sum(x) for x in zip((xr, yr), _dir_to_coord[direction])]
        grid.update([(xs, ys), (xr, yr)])

    return len(grid)


_dir_to_coord = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0),
}
