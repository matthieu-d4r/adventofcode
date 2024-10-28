import pytest

from day_03 import part_1, part_2
from conftest import PUZZLE_INPUT


part_1_examples = [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)]
part_1_puzzle_answer = 2565
part_2_examples = [("^>", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)]
part_2_puzzle_answer = 2639


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
