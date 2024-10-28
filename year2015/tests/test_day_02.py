import pytest

from day_02 import part_1, part_2
from conftest import PUZZLE_INPUT


part_1_examples = [("2x3x4", 58), ("1x1x10", 43)]
part_1_puzzle_answer = 1586300
part_2_examples = [("2x3x4", 34), ("1x1x10", 14)]
part_2_puzzle_answer = 3737498


@pytest.mark.parametrize("input_, expected", part_1_examples)
def test_part_1_example(input_, expected):
    assert part_1(input_) == expected


def test_part_1_puzzle_input(datadir):
    with open(datadir / PUZZLE_INPUT) as f:
        assert part_1(f.read()) == part_1_puzzle_answer


@pytest.mark.parametrize("input_, expected", part_2_examples)
def test_part_2_example(input_, expected):
    assert part_2(input_) == expected


def test_part_2_puzzle_input(datadir):
    with open(datadir / PUZZLE_INPUT) as f:
        assert part_2(f.read()) == part_2_puzzle_answer
