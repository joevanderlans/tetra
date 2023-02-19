from tetra import move, piece, square


def test_move():
    assert move.Move.from_uci("e2e4").from_square.index == square.E2
    assert move.Move.from_uci("e2e4").to_square.index == square.E4


def test_move_eq():
    assert move.Move.from_uci("a1a2") == move.Move.from_uci("a1a2")


def test_promotion():
    my_move = move.Move.from_uci("a7a8q")
    assert my_move.promotion == piece.Piece.from_symbol("Q")

    my_move = move.Move.from_uci("a2a1q")
    assert my_move.promotion == piece.Piece.from_symbol("q")

    my_move = move.Move.from_uci("a7a8n")
    assert my_move.promotion == piece.Piece.from_symbol("N")
