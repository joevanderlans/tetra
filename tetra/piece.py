from __future__ import annotations

# Create piece constants
Color = int
COLORS = [EMPTY_COLOR, WHITE, BLACK] = range(3)

PieceType = int
PIECE_TYPES = [
    EMPTY_PIECE,
    PAWN,
    KNIGHT,
    BISHOP,
    ROOK,
    QUEEN,
    KING,
] = range(7)

PIECE_SLIDING = {
    0: None,
    1: False,
    2: False,
    3: True,
    4: True,
    5: True,
    6: False,
}

N, E, S, W = -10, 1, 10, -1
PIECE_DIRECTIONS = {
    0: None,
    1: None,
    2: [N+N+E, N+N+W, N+E+E, N+W+W, S+S+E, S+S+W, S+E+E, S+W+W],
    3: [N+E, N+W, S+E, S+W],
    4: [N, E, S, W],
    5: [N, E, S, W, N+E, N+W, S+E, S+W],
    6: [N, E, S, W, N+E, N+W, S+E, S+W],
}

PieceSymbol = str
PIECE_SYMBOLS = [".", "p", "n", "b", "r", "q", "k"]
PIECE_UNICODE = {
    ".": ".",
    "P": "♙", "p": "♟",
    "N": "♘", "n": "♞",
    "B": "♗", "b": "♝",
    "R": "♖", "r": "♜",
    "Q": "♕", "q": "♛",
    "K": "♔", "k": "♚",
}


# Create piece class
class Piece:
    """A chess piece with type and color"""
    def __init__(self, color: Color, piece_type: PieceType) -> None:
        self.color = color
        self.piece_type = piece_type
    
    def __repr__(self) -> str:
        return f"Piece.from_symbol('{self.symbol()}')"

    def __str__(self) -> str:
        return self.symbol()
    
    def __eq__(self, other: Piece) -> bool:
        if isinstance(other, Piece):
            return (self.piece_type, self.color) == (other.piece_type, other.color)
        else:
            return NotImplemented

    def symbol(self) -> str:
        symbol = PIECE_SYMBOLS[self.piece_type]
        if self.color == WHITE:
            symbol = symbol.upper()
        return symbol
    
    def is_sliding(self) -> bool:
        return PIECE_SLIDING[self.piece_type]
    
    def directions(self) -> list[int]:
        if self.piece_type != PAWN:
            directions = PIECE_DIRECTIONS[self.piece_type]
        elif self.piece_type == PAWN:
            if self.color == WHITE:
                directions = [N, N+N, N+E, N+W]
            elif self.color == BLACK:
                directions = [S, S+S, S+E, S+W]
        return directions

    def unicode(self) -> str:
        return PIECE_UNICODE[self.symbol()]
    
    @classmethod
    def from_symbol(cls, symbol: PieceSymbol) -> Piece:
        if symbol == ".": color = EMPTY_COLOR
        elif symbol.isupper(): color = WHITE
        elif symbol.islower(): color = BLACK

        piece_type = PIECE_SYMBOLS.index(symbol.lower())
        return cls(color, piece_type)
