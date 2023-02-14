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
    assert len(my_moves) == 33

def test_moves_scotch():
    scotch = "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 0 3"
    my_moves = position.Position(scotch).generate_moves()
    assert len(my_moves) == 32

def test_make_move_e4():
    my_position = position.Position()
    my_position.make_move(move.Move.from_uci("e2e4"))
    assert my_position.fen() == "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

def test_attackers_giuoco_piano():
    giuoco_piano = "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4"
    my_position = position.Position(giuoco_piano)

    assert my_position.find_attackers(
        piece.WHITE, square.Square.from_name("f7")
    ) == [square.Square.from_name("c4")]

    assert my_position.find_attackers(
        piece.WHITE, square.Square.from_name("d5")
    ) == [square.Square.from_name("e4"), square.Square.from_name("c4")]

    assert my_position.find_attackers(
        piece.BLACK, square.Square.from_name("d4")
    ) == [square.Square.from_name("e5"), square.Square.from_name("c6"), square.Square.from_name("c5")]

def test_moves_castling():
    castling = "r3k2r/pppq1ppp/2npbn2/2b1p3/2B1P3/2NPBN2/PPPQ1PPP/R3K2R w KQkq - 4 8"
    my_moves = position.Position(castling).generate_moves()
    assert move.Move.from_uci("e1g1") in my_moves
    assert move.Move.from_uci("e1c1") in my_moves

def test_make_move_castling_ks():
    castling = "r3k2r/pppq1ppp/2npbn2/2b1p3/2B1P3/2NPBN2/PPPQ1PPP/R3K2R w KQkq - 4 8"
    my_position_ks = position.Position(castling)
    my_position_ks.make_move(move.Move.from_uci("e1g1"))
    assert my_position_ks.fen() == "r3k2r/pppq1ppp/2npbn2/2b1p3/2B1P3/2NPBN2/PPPQ1PPP/R4RK1 b kq - 5 8"

def test_make_move_castling_qs():
    castling = "r3k2r/pppq1ppp/2npbn2/2b1p3/2B1P3/2NPBN2/PPPQ1PPP/R3K2R w KQkq - 4 8"
    my_position_qs = position.Position(castling)
    my_position_qs.make_move(move.Move.from_uci("e1c1"))
    assert my_position_qs.fen() == "r3k2r/pppq1ppp/2npbn2/2b1p3/2B1P3/2NPBN2/PPPQ1PPP/2KR3R b kq - 5 8"

def test_moves_castling_blocked():
    castling_blocked = "r3k2r/pppq1ppp/3pb3/4n3/2B1P3/3PbP2/PPP3PP/R3K2R w KQkq - 0 12"
    my_moves = position.Position(castling_blocked).generate_moves()
    assert move.Move.from_uci("e1g1") not in my_moves
    assert move.Move.from_uci("e1c1") not in my_moves

def test_ep_capture():
    ep_capture = "rnbqkbnr/1pp1pppp/p7/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3"
    my_position = position.Position(ep_capture)
    my_moves = my_position.generate_moves()
    assert move.Move.from_uci("e5d6") in my_moves

    my_position.make_move(move.Move.from_uci("e5d6"))
    assert my_position.fen() == "rnbqkbnr/1pp1pppp/p2P4/8/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 3"
