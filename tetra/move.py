from __future__ import annotations
from typing import Optional

from tetra import square
from tetra import piece

# Create move class
class Move:
    """A chess move"""

    def __init__(
        self,
        from_square: square.Square,
        to_square: square.Square,
        promotion: Optional[piece.Piece] = None,
    ) -> None:
        self.from_square = from_square
        self.to_square = to_square
        self.promotion = promotion

    def __repr__(self) -> str:
        return f"Move.from_uci('{self.uci()}')"

    def __str__(self) -> str:
        return self.uci()

    def __eq__(self, other: Move) -> bool:
        if isinstance(other, Move):
            return (self.from_square, self.to_square, self.promotion) == (
                other.from_square,
                other.to_square,
                other.promotion,
            )
        else:
            return NotImplemented

    def uci(self) -> str:
        if self.promotion is None:
            promotion_str = ""
        else:
            promotion_str = self.promotion.symbol().lower()

        return self.from_square.name() + self.to_square.name() + promotion_str

    @classmethod
    def from_uci(cls, uci: str) -> Move:
        from_square = square.Square.from_name(uci[0:2])
        to_square = square.Square.from_name(uci[2:4])

        if len(uci) == 5:
            promotion_symbol = uci[4]
            if to_square.rank() == 8:
                promotion_symbol = promotion_symbol.upper()

            if to_square.rank() == 1:
                promotion_symbol = promotion_symbol.lower()

            promotion = piece.Piece.from_symbol(promotion_symbol)
        else:
            promotion = None

        return cls(from_square, to_square, promotion)
