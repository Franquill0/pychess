from position import Position

def invalid_position_format(expected_value:bool, pos_y:int, pos_x:int) -> str:
    return f"Expected {expected_value}! ({pos_y},{pos_x}) is NOT a valid position."

def test_invalid_positions() -> None:
    above_upper_bound = 9
    below_lower_bound = -1
    inside_bounds = 0

    # invalid positions, expected false
    assert not Position.is_valid_position(below_lower_bound, inside_bounds), invalid_position_format(False, below_lower_bound, inside_bounds)
    assert not Position.is_valid_position(inside_bounds, below_lower_bound), invalid_position_format(False, inside_bounds, below_lower_bound)
    assert not Position.is_valid_position(above_upper_bound, inside_bounds), invalid_position_format(False, above_upper_bound, inside_bounds)
    assert not Position.is_valid_position(inside_bounds, above_upper_bound), invalid_position_format(False, inside_bounds, above_upper_bound)

def test_valid_position() -> None:
    inside_bounds = 0
    # valid position, expected true
    assert Position.is_valid_position(inside_bounds, inside_bounds), f"Expected True! ({inside_bounds},{inside_bounds}) is a valid position"
