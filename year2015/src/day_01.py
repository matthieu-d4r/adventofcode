def part_1(instructions: str) -> int:
    instructions = instructions.strip()  # remove EOL
    return 2 * instructions.count("(") - len(instructions)


def part_2(instructions: str) -> int:
    instructions = instructions.strip()  # remove EOL
    floor = 0
    for i, ch in enumerate(instructions):
        floor += 1 if ch == "(" else -1
        if floor == -1:
            return i + 1
    return 0
