import pytest

from day_06 import part_1, part_2
from conftest import PUZZLE_INPUT


part_1_examples = [
    ("turn on 0,0 through 999,999", 1000000),
    ("toggle 0,0 through 999,0", 1000),
    ("turn on 499,499 through 500,500", 4),
]
part_1_puzzle_answer = 377891
part_2_examples = [
    ("turn on 0,0 through 0,0", 1),
    ("toggle 0,0 through 999,999", 2000000),
]
part_2_puzzle_answer = 14110788


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
