from tetra import move
from tetra import square

def test_move():
    assert move.Move.from_uci("e2e4").from_square.index == square.E2
    assert move.Move.from_uci("e2e4").to_square.index == square.E4
