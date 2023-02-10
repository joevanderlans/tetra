from tetra import piece

def test_piece_type():
    assert piece.Piece.from_symbol(".").piece_type == piece.EMPTY_PIECE
    assert piece.Piece.from_symbol("P").piece_type == piece.PAWN
    assert piece.Piece.from_symbol("N").piece_type == piece.KNIGHT
    assert piece.Piece.from_symbol("B").piece_type == piece.BISHOP
    assert piece.Piece.from_symbol("R").piece_type == piece.ROOK
    assert piece.Piece.from_symbol("Q").piece_type == piece.QUEEN
    assert piece.Piece.from_symbol("K").piece_type == piece.KING

def test_color():
    assert piece.Piece.from_symbol(".").color == piece.EMPTY_COLOR
    assert piece.Piece.from_symbol("P").color == piece.WHITE
    assert piece.Piece.from_symbol("p").color == piece.BLACK
