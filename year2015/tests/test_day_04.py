import pytest

from day_04 import part_1, part_2
from conftest import PUZZLE_INPUT


part_1_examples = [("abcdef", 609043), ("pqrstuv", 1048970)]
part_1_puzzle_answer = 346386
part_2_puzzle_answer = 9958218


@pytest.mark.parametrize("input_, expected", part_1_examples)
def test_part_1_example(input_, expected):
    assert part_1(input_) == expected


def test_part_1_puzzle_input(datadir):
    with open(datadir / PUZZLE_INPUT) as f:
        assert part_1(f.read()) == part_1_puzzle_answer


def test_part_2_puzzle_input(datadir):
    with open(datadir / PUZZLE_INPUT) as f:
        assert part_2(f.read()) == part_2_puzzle_answer
