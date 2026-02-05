

class Tile:
    def __init__(self):
        self.is_bomb = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_bombs = 0