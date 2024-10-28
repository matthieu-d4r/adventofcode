from collections import Counter
from itertools import pairwise


def part_1(strings: str) -> int:
    nice = 0
    for string in strings.splitlines():
        c = Counter(string)

        if sum(c[x] for x in "aeiou") < 3:
            continue
        if not any(x[0] == x[1] for x in pairwise(string)):
            continue
        if any(x in string for x in ["ab", "cd", "pq", "xy"]):
            continue

        nice += 1
    return nice


def part_2(strings: str) -> int:
    nice = 0
    for string in strings.splitlines():
        c = Counter("".join(x) for x in pairwise(string))

        if not any(string.count(x) > 1 for x in c):
            continue
        if not any(string[i] == string[i + 2] for i in range(len(string) - 2)):
            continue

        nice += 1
    return nice
