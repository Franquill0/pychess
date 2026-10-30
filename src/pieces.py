from enum import Enum
from abc import ABC, abstractmethod
from board import Board
from position import Position
from piece_move import Movement

class PieceColor(Enum):
    BLACK = 0
    WHITE = 1

class Piece(ABC):
    def __init__(self, color:PieceColor):
        self.color:PieceColor = color

    def _print(self, piece_str:str) -> str:
        str_return = piece_str
        if self.color == PieceColor.WHITE:
            str_return = str_return.upper()
        return str_return

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        pass

    def get_steps_from_to(self, initial_pos:Position, final_pos:Position) -> None | list[Position]:
        return Movement.get_steps_from_to(initial_pos, final_pos)


class Pawn(Piece):
    def __init__(self, color:PieceColor):
        super().__init__(color)
        self.first_move:bool = True

    def __str__(self) -> str:
        return super()._print("p")

    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        return False
        
    

class Rook(Piece):
    def __str__(self) -> str:
        return super()._print("r")
    
    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        return Position.same_row(initial_pos, final_pos) or Position.same_col(initial_pos, final_pos)

class Knight(Piece):
    def __str__(self) -> str:
        return super()._print("n")

    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        return False

class Bishop(Piece):
    def __str__(self) -> str:
        return super()._print("b")
    
    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        return Position.same_diagonal(initial_pos, final_pos)

class Queen(Piece):
    def __str__(self) -> str:
        return super()._print("q")

    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        return Position.same_row(initial_pos, final_pos) or\
               Position.same_col(initial_pos, final_pos) or\
               Position.same_diagonal(initial_pos, final_pos)

class King(Piece):
    def __str__(self) -> str:
        return super()._print("k")

    def can_move_from_to(self, board:Board, initial_pos:Position, final_pos:Position) -> bool:
        return False

