from piece_move import Movement
from position import Position

def test_diagonal_move1() -> None:
    real_steps:list[Position] = [Position(2,3)]
    test_steps = Movement.get_steps_from_to(Position(1,2), Position(2,3))
    assert real_steps == test_steps, f"Expected {real_steps}, got {test_steps}!"

def test_diagonal_move2() -> None:
    real_steps:list[Position] = [Position(4,4), Position(3,5), Position(2,6), Position(1,7)]
    test_steps = Movement.get_steps_from_to(Position(5,3), Position(1,7))
    assert real_steps == test_steps, f"Expected {real_steps}, got {test_steps}!"

def test_same_initial_and_final_position() -> None:
    position = Position(3,4)
    steps = Movement.get_steps_from_to(position, position)
    assert steps == None, f"Expected None, got {steps}"
