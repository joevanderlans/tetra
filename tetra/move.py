from __future__ import annotations

from tetra import square

# Create move class
class Move:
    """A chess move"""
    def __init__(self, from_square: square.Square, to_square: square.Square) -> None:
        self.from_square = from_square
        self.to_square = to_square

    def __repr__(self) -> str:
        return f"Move.from_uci('{self.uci()}')"

    def __str__(self) -> str:
        return self.uci()
    
    def __eq__(self, other: Move) -> bool:
        if isinstance(other, Move):
            return (self.from_square, self.to_square) == (other.from_square, other.to_square)
        else:
            return NotImplemented

    def uci(self) -> str:
        return self.from_square.name() + self.to_square.name()
   
    @classmethod
    def from_uci(cls, uci: str) -> Move:
        from_square = square.Square.from_name(uci[0:2])
        to_square = square.Square.from_name(uci[2:4])
        return cls(from_square, to_square)
