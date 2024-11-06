def part_1(strings: str) -> int:
    diff = 0
    for string in strings.splitlines():
        diff += len(string) - len(string.encode().decode("unicode_escape")) + 2
    return diff


def part_2(strings: str) -> int:
    diff = 0
    for string in strings.splitlines():
        diff += string.count("\\") + string.count('"') + 2
    return diff
