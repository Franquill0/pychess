from pieces import *
from position import Position


class Board:
    def __init__(self) -> None:
        # let's asssume the coords 0,0 in self.board correspond to
        # A8 in the chess board
        self.board:list[list[None | Piece]] = [ [None for _ in range(8)] for _ in range(8) ]

    def initial_position(self) -> None:
        # Pawns
        for i in range(8):
            self._put_piece_on(Pawn(PieceColor.BLACK), 1, i)
            self._put_piece_on(Pawn(PieceColor.WHITE), 6, i)
        # Rooks
        self._put_piece_on(Rook(PieceColor.BLACK), 0, 0)
        self._put_piece_on(Rook(PieceColor.BLACK), 0, 7)
        self._put_piece_on(Rook(PieceColor.WHITE), 7, 0)
        self._put_piece_on(Rook(PieceColor.WHITE), 7, 7)
        # Knights
        self._put_piece_on(Knight(PieceColor.BLACK), 0, 1)
        self._put_piece_on(Knight(PieceColor.BLACK), 0, 6)
        self._put_piece_on(Knight(PieceColor.WHITE), 7, 1)
        self._put_piece_on(Knight(PieceColor.WHITE), 7, 6)
        # Bishops
        self._put_piece_on(Bishop(PieceColor.BLACK), 0, 2)
        self._put_piece_on(Bishop(PieceColor.BLACK), 0, 5)
        self._put_piece_on(Bishop(PieceColor.WHITE), 7, 2)
        self._put_piece_on(Bishop(PieceColor.WHITE), 7, 5)
        # Queens
        self._put_piece_on(Queen(PieceColor.BLACK), 0, 3)
        self._put_piece_on(Queen(PieceColor.WHITE), 7, 3)
        # Kings
        self._put_piece_on(King(PieceColor.BLACK), 0, 4)
        self._put_piece_on(King(PieceColor.WHITE), 7, 4)

    def _put_piece_on(self, piece:Piece, pos_y:int, pos_x:int) -> None:
        assert Position.is_valid_position(pos_y, pos_x), f"({pos_y},{pos_x}) not a valid position"
        self.board[pos_y][pos_x] = piece

    def __str__(self) -> str:
        board_str = ""
        for row in self.board:
            for square in row:
                board_str += " "
                if square:
                    board_str += square.__str__()
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece_on(self, position:Position) -> None | Piece:
        return self.board[position.get_row()][position.get_col()]

    def _can_move_from_to(self, initial_pos:Position, final_pos:Position) -> bool:
        piece = self.get_piece_on(initial_pos)
        if piece == None:
            return False
        else:
            return piece.can_move_from_to(self, initial_pos, final_pos)
                    





