class Position:
    @staticmethod
    def is_valid_position(pos_y:int, pos_x:int) -> bool:
        return pos_y >= 0 and pos_y < 8 and pos_x >= 0 and pos_x < 8