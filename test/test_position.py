from tetra import piece
from tetra import square
from tetra import move
from tetra import position

def test_initial_position():
    my_position = position.Position()
    assert my_position.board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', ' ', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', ' ', ' ', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert my_position.turn == piece.WHITE
    assert my_position.castling_rights == ["K", "Q", "k", "q"]
    assert my_position.ep_square == None
    assert my_position.halfmove_clock == 0
    assert my_position.move_number == 1

def test_initial_fen():
    my_position = position.Position()
    my_position.fen() == position.INITIAL_FEN
