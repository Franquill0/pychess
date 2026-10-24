from enum import Enum

class PieceColor(Enum):
    BLACK = 0
    WHITE = 1

class Piece:
    def __init__(self, color:PieceColor):
        self.color:PieceColor = color

class Pawn(Piece):
    def __init__(self):
        self.first_move:bool = True

class Rook(Piece):
    def __init__(self):
        self.first_move:bool = True


    

