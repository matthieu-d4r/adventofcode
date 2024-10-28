def part_1(dimensions: str) -> int:
    sq_ft = 0
    for dimension in dimensions.splitlines():
        l, w, h = map(int, dimension.split("x"))
        lw, wh, hl = l * w, w * h, h * l
        sq_ft += 2 * (lw + wh + hl) + min(lw, wh, hl)
    return sq_ft


def part_2(dimensions: str) -> int:
    ft = 0
    for dimension in dimensions.splitlines():
        l, w, h = map(int, dimension.split("x"))
        mins = sorted([l, w, h])
        ft += 2 * (sum(mins[:2])) + l * w * h
    return ft
