class Position:
    def __init__(self, row:int, col:int) -> None:
        assert Position.is_valid_position(row, col), f"({row},{col}) not a valid position!"
        self.row: int = row
        self.col: int = col
    
    @staticmethod
    def is_valid_position(row:int, col:int) -> bool:
        return Position.is_valid_row(row) and Position.is_valid_col(col)

    @staticmethod
    def is_valid_row(row:int) -> bool:
        return row >= 0 and row < 9

    @staticmethod
    def is_valid_col(col:int) -> bool:
        return col >= 0 and col < 9

    @staticmethod
    def same_row(pos1:Position, pos2:Position) -> bool:
        return pos1.get_row() == pos2.get_row()

    @staticmethod
    def same_col(pos1:Position, pos2:Position) -> bool:
        return pos1.get_col() == pos2.get_col()

    @staticmethod
    def same_diagonal(pos1:Position, pos2:Position) -> bool:
        return abs(pos1.get_col() - pos2.get_col()) == abs(pos1.get_row() - pos2.get_row())

    def __eq__(self, position:object) -> bool:
        if not isinstance(position, Position):
            return False
        else:
            return self.get_col() == position.get_col() and self.get_row() == position.get_row()

    def __str__(self) -> str:
        return f"({self.row},{self.col})"

    def __repr__(self) -> str:
        return self.__str__()

    def copy(self) -> Position:
        return Position(self.row, self.col)

    def get_row(self) -> int:
        return self.row

    def set_row(self, new_row:int) -> None:
        assert Position.is_valid_row(new_row), f"{new_row} not a valid row!"
        self.row = new_row

    def set_col(self, new_col:int) -> None:
        assert Position.is_valid_col(new_col), f"{new_col} not a valid col!"
        self.col = new_col

    def get_col(self) -> int:
        return self.col