import pytest

from day_01.day_01 import part_1, part_2


@pytest.mark.parametrize("instructions,expected", [("(())", 0), ("(()(()(", 3)])
def test_part_1(instructions: str, expected: int, shared_datadir):
    assert part_1(instructions) == expected

    with open(shared_datadir / "puzzle_input.txt") as f:
        assert part_1(f.read()) == 280


@pytest.mark.parametrize("instructions,expected", [(")", 1), ("()()))", 5)])
def test_part_2(instructions: str, expected: int, shared_datadir):
    assert part_2(instructions) == expected

    with open(shared_datadir / "puzzle_input.txt") as f:
        assert part_2(f.read()) == 1797
