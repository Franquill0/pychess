from pieces import Piece


class Board:
    def __init__(self):
        self.board:list[list[None | Piece]] = [ [None for _ in range(8)] for _ in range(8) ]

    def initial_position(self):
        self.board