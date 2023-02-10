from __future__ import annotations
from typing import Optional

from tetra import piece
from tetra import square
from tetra import move

# Create position constants
INITIAL_BOARD_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
INITIAL_FEN = INITIAL_BOARD_FEN + " w KQkq - 0 1"

# Create position class
class Position:
    """A chess position"""
    def __init__(self, fen: Optional[str] = INITIAL_FEN) -> None:
        self.move_stack = []
        self.set_fen(fen)

    def __repr__(self) -> str:
        return f"Position('{self.fen()}')"
    
    def __str__(self) -> str:
        output = ""
        for i, square_i in enumerate(square.SQUARES):
            output += self.board[square_i]
            if (i+1) % 8 == 0 and i < 63:
                output += "\n"
        return output

    def set_fen(self, fen: str) -> None:
        # Split FEN
        [
            board_fen,
            turn_fen,
            castling_rights_fen,
            ep_square_fen,
            halfmove_clock_fen,
            move_number_fen,
        ] = fen.split()

        # Set board
        board = [" " for _ in range(120)]
        for i in square.SQUARES:
            board[i] = "."
        
        square_i = 0
        for i in board_fen:
            if i in [str(x) for x in range(1, 9)]:
                square_i += int(i)
            if i.lower() in piece.PIECE_SYMBOLS:
                board[square.SQUARES[square_i]] = i
                square_i += 1
        
        # Set turn
        if turn_fen == "w":
            turn = piece.WHITE
        elif turn_fen == "b":
            turn = piece.BLACK

        # Set castling_rights
        castling_rights = []
        if "K" in castling_rights_fen:
            castling_rights.append("K")
        if "Q" in castling_rights_fen:
            castling_rights.append("Q")
        if "k" in castling_rights_fen:
            castling_rights.append("k")
        if "q" in castling_rights_fen:
            castling_rights.append("q")
       
        # Set ep_square
        ep_square_fen = ep_square_fen.lower()

        if ep_square_fen == "-":
            ep_square = None
        elif ep_square_fen in square.SQUARE_NAMES:
            ep_square = square.Square.from_name(ep_square_fen)

        # Set halfmove_clock
        halfmove_clock = int(halfmove_clock_fen)

        # Set move_number
        move_number = int(move_number_fen)

        # Set values
        self.board = board
        self.turn = turn
        self.castling_rights = castling_rights
        self.ep_square = ep_square
        self.halfmove_clock = halfmove_clock
        self.move_number = move_number

    def fen(self) -> str:
        # Set board_fen
        board_fen = ""
        empty_squares = 0
        for i, square_i in enumerate(square.SQUARES):
            if self.board[square_i] == ".":
                empty_squares += 1
            elif self.board[square_i].lower() in piece.PIECE_SYMBOLS:
                if empty_squares > 0:
                    board_fen += str(empty_squares)
                empty_squares = 0
                board_fen += self.board[square_i]
            
            if (i+1) % 8 == 0 and i < 63:
                if empty_squares > 0:
                    board_fen += str(empty_squares)
                empty_squares = 0
                board_fen += "/"

        # Set turn_fen
        turn_fen = 'w' if self.turn == piece.WHITE else 'b'

        # Set castling_rights_fen
        castling_rights_fen = "".join(self.castling_rights)

        # Set ep_square_fen
        ep_square_fen = self.ep_square if self.ep_square is not None else "-"

        # Set halfmove_clock_fen
        halfmove_clock_fen = str(self.halfmove_clock)

        # Set move_number_fen
        move_number_fen = str(self.move_number)

        # Return fen
        return " ".join([
            board_fen,
            turn_fen,
            castling_rights_fen,
            ep_square_fen,
            halfmove_clock_fen,
            move_number_fen,
        ])
