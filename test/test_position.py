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
    assert my_position.fen() == position.INITIAL_FEN

def test_initial_moves():
    my_moves = position.Position().generate_moves()
    assert len(my_moves) == 20

def test_moves_giuoco_piano():
    giuoco_piano = "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4"
    my_moves = position.Position(giuoco_piano).generate_moves()
    assert len(my_moves) == 32

def test_moves_scotch():
    scotch = "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 0 3"
    my_moves = position.Position(scotch).generate_moves()
    assert len(my_moves) == 32

def test_make_move_e4():
    my_position = position.Position()
    my_position.make_move(move.Move.from_uci("e2e4"))
    assert my_position.fen() == "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
