import pytest

from conftest import PUZZLE_INPUT
from day_01 import part_1, part_2


part_1_examples = [("(())", 0), ("(()(()(", 3)]
part_1_puzzle_answer = 280
part_2_examples = [(")", 1), ("()()))", 5)]
part_2_puzzle_answer = 1797


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
