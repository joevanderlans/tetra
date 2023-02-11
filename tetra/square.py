from __future__ import annotations

# Create square constants
SquareName = str
SquareIndex = int
SQUARE_NAMES = [
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
    "  ", "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "  ",
    "  ", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "  ",
    "  ", "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "  ",
    "  ", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "  ",
    "  ", "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "  ",
    "  ", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "  ",
    "  ", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "  ",
    "  ", "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "  ",
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
    "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
]

SQUARES = [
    A8, B8, C8, D8, E8, F8, G8, H8,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A1, B1, C1, D1, E1, F1, G1, H1,
] = [
    21, 22, 23, 24, 25, 26, 27, 28,
    31, 32, 33, 34, 35, 36, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48,
    51, 52, 53, 54, 55, 56, 57, 58,
    61, 62, 63, 64, 65, 66, 67, 68,
    71, 72, 73, 74, 75, 76, 77, 78,
    81, 82, 83, 84, 85, 86, 87, 88,
    91, 92, 93, 94, 95, 96, 97, 98,
]


# Create square class
class Square:
    """A square on a chess board"""
    def __init__(self, index: SquareIndex) -> None:
        self.index = index

    def __repr__(self) -> str:
        return f"Square.from_name('{self.name()}')"

    def __str__(self) -> str:
        return self.name()

    def name(self) -> str:
        return SQUARE_NAMES[self.index]
    
    def file(self) -> str:
        return str(self.name())[0]

    def rank(self) -> int:
        return int(str(self.name())[1])
   
    @classmethod
    def from_name(cls, name: SquareName) -> Square:
        index = SQUARE_NAMES.index(name)
        return cls(index)
