from enum import Enum
from board import Board
from position import Position

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)
    UP_RIGHT = (-1, 1)
    UP_LEFT = (-1, -1)
    DOWN_RIGHT = (1, 1)
    DOWN_LEFT = (1, -1)

    def get_step(self) -> tuple[int, int]:
        return self.value

    @staticmethod
    def _normalize(num:int) -> int:
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0

    @staticmethod
    def get_direction_from_to(initial_pos:Position, final_pos:Position) -> tuple[int,int]:
        direction: tuple[int, int] = (
            Direction._normalize(final_pos.get_row() - initial_pos.get_row()),
            Direction._normalize(final_pos.get_col() - initial_pos.get_col())
        )
        return direction

class Movement:
    @staticmethod
    def can_move_horizontally_from_to(initial_pos:Position, final_pos:Position) -> bool:
        return Position.same_row(initial_pos, final_pos)

    @staticmethod
    def can_move_vertically_from_to(initial_pos:Position, final_pos:Position) -> bool:
        return Position.same_col(initial_pos, final_pos)

    @staticmethod
    def can_move_diagonally_from_to(initial_pos:Position, final_pos:Position) -> bool:
        return Position.same_diagonal(initial_pos, final_pos)

    @staticmethod
    def no_direction_possible(initial_pos:Position, final_pos:Position) -> bool:
        return not (Movement.can_move_diagonally_from_to(initial_pos, final_pos)   or 
                    Movement.can_move_horizontally_from_to(initial_pos, final_pos) or 
                    Movement.can_move_vertically_from_to(initial_pos, final_pos))

    @staticmethod
    def get_steps_from_to(initial_pos:Position, final_pos:Position) -> None | list[Position]:
        if initial_pos == final_pos or Movement.no_direction_possible(initial_pos, final_pos):
            return None

        steps:list[Position] = []
        position = Position(initial_pos.get_row(), initial_pos.get_col())
        direction = Direction.get_direction_from_to(initial_pos, final_pos)

        while position != final_pos:
            position.set_row(position.get_row()+direction[0])
            position.set_col(position.get_col()+direction[1])
            steps.append(position.copy())

        return steps



