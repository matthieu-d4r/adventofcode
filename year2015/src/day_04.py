from hashlib import md5


def part_1(secret_key: str) -> int:
    secret_key = secret_key.strip()
    n = 0
    while not md5((secret_key + str(n)).encode()).hexdigest().startswith("00000"):
        n += 1
    return n


def part_2(secret_key: str) -> int:
    secret_key = secret_key.strip()
    n = 0
    while not md5((secret_key + str(n)).encode()).hexdigest().startswith("000000"):
        n += 1
    return n
