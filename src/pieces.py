from enum import Enum
from abc import ABC, abstractmethod

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

class Pawn(Piece):
    def __init__(self, color:PieceColor):
        super().__init__(color)
        self.first_move:bool = True

    def __str__(self) -> str:
        return super()._print("p")

class Rook(Piece):
    def __init__(self, color:PieceColor):
        super().__init__(color)
        self.first_move:bool = True

    def __str__(self) -> str:
        return super()._print("r")

class Knight(Piece):
    def __str__(self) -> str:
        return super()._print("n")

class Bishop(Piece):
    def __str__(self) -> str:
        return super()._print("b")

class Queen(Piece):
    def __str__(self) -> str:
        return super()._print("q")

class King(Piece):
    def __str__(self) -> str:
        return super()._print("k")

