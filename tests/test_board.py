import pytest
import pieces
from board import Board

def test_invalid_position_in_board_call() -> None:
    with pytest.raises(AssertionError):
        my_board = Board()
        my_board._put_piece_on(pieces.Pawn(pieces.PieceColor.BLACK), -1, -3)