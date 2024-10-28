def part_1(instructions: str) -> int:
    instructions = instructions.strip()  # remove EOL
    num_ups = instructions.count("(")
    # num_ups + num_downs == len => nums_downs == len - nums_ups
    return 2 * num_ups - len(instructions)


def part_2(instructions: str) -> int:
    instructions = instructions.strip()  # remove EOL
    floor = 0
    for i, ch in enumerate(instructions):
        floor += 1 if ch == "(" else -1
        if floor == -1:
            return i + 1
    return 0
