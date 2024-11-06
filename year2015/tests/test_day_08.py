from day_08 import part_1, part_2
from conftest import PUZZLE_INPUT

part_1_puzzle_answer = 1342
part_2_puzzle_answer = 2074


def test_part_1_puzzle_input(datadir):
    with open(datadir / PUZZLE_INPUT) as f:
        assert part_1(f.read()) == part_1_puzzle_answer


def test_part_2_puzzle_input(datadir):
    with open(datadir / PUZZLE_INPUT) as f:
        assert part_2(f.read()) == part_2_puzzle_answer
