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
        ep_square_fen = self.ep_square.name() if self.ep_square is not None else "-"

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
    
    def get_piece(self, square: square.Square) -> piece.Piece:
        return piece.Piece.from_symbol(self.board[square.index])

    def set_piece(self, piece: piece.Piece, square: square.Square) -> None:
        self.board[square.index] = piece.symbol()
    
    def remove_piece(self, square: square.Square) -> None:
        self.board[square.index] = "."
    
    def get_opposing_color(self) -> piece.Color:
        if self.turn == piece.WHITE:
            opposing_color = piece.BLACK
        else:
            opposing_color = piece.WHITE
        return opposing_color
    
    def generate_moves(self) -> list[move.Move]:
        my_moves = []
        
        for i in square.SQUARES:
            square_i = square.Square(i)
            piece_i = self.get_piece(square_i)

            # Skip empty squares
            if piece_i.piece_type == piece.EMPTY_PIECE: continue

            # Skip opponent pieces
            if piece_i.color != self.turn: continue

            # Loop over directions
            for direction in piece_i.directions():
                step = direction

                # Use a loop for sliding pieces
                while True:
                    j = i + step

                    # Stay on board
                    if j not in square.SQUARES: break

                    square_j = square.Square(j)
                    piece_j = self.get_piece(square_j)

                    # Stay off friendly pieces
                    if piece_i.color == piece_j.color: break

                    # Determine pawn moves
                    if piece_i.piece_type == piece.PAWN:
                        if direction in (piece.N, piece.S) \
                            and piece_j.piece_type != piece.EMPTY_PIECE: break
                        
                        if direction in (
                            piece.N + piece.E,
                            piece.N + piece.W,
                            piece.S + piece.E,
                            piece.S + piece.W,
                        ) \
                            and piece_j.color != self.get_opposing_color() \
                            and square_j != self.ep_square:
                            break
                        
                        if direction == piece.N + piece.N:
                            piece_int = self.get_piece(square.Square(i + piece.N))

                            if square_i.rank() != 2: break
                            if piece_int.piece_type != piece.EMPTY_PIECE: break
                            if piece_j.piece_type != piece.EMPTY_PIECE: break
                        
                        if direction == piece.S + piece.S:
                            piece_int = self.get_piece(square.Square(i + piece.S))

                            if square_i.rank() != 7: break
                            if piece_int.piece_type != piece.EMPTY_PIECE: break
                            if piece_j.piece_type != piece.EMPTY_PIECE: break
                    
                    # Generate move
                    my_move = move.Move(square.Square(i), square.Square(j))
                    my_moves.append(my_move)
                    
                    # Break for captures
                    if piece_j.piece_type == self.get_opposing_color(): break

                    # Break for non-sliding pieces
                    if not piece_i.is_sliding(): break

                    # Iterate step for sliding pieces
                    step += direction
        
        return my_moves

    def make_move(self, move: move.Move) -> None:
        # Update move stack
        self.move_stack.append(move)

        # Update board
        square_i = move.from_square
        square_j = move.to_square
        piece_i = self.get_piece(move.from_square)
        piece_j = self.get_piece(move.to_square)

        self.remove_piece(move.from_square)
        self.set_piece(piece_i, move.to_square)

        # Update castling rights
        # To do

        # Update en passant square
        self.ep_square = None
        if piece_i.piece_type == piece.PAWN \
            and square_j.index - square_i.index == piece.N + piece.N:
            self.ep_square = square.Square(square_i.index + piece.N)
        
        if piece_i.piece_type == piece.PAWN \
            and square_j.index - square_i.index == piece.S + piece.S:
            self.ep_square = square.Square(square_i.index + piece.S)
        
        # Update halfmove clock
        if piece_i.piece_type == piece.PAWN \
            or piece_j.piece_color == self.get_opposing_color():
            self.halfmove_clock = 0
        else:
            self.halfmove_clock += 1

        # Update move number
        if self.turn == piece.BLACK:
            self.move_number += 1
        
        # Update turn
        self.turn = self.get_opposing_color()
