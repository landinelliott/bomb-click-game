import random
from tile import Tile

class Board:
    def __init__(self, rows, cols, bomb_count=10):
        self.rows = rows          # FIXED
        self.cols = cols
        self.bomb_count = bomb_count

        self.grid = [[Tile() for _ in range(cols)] for _ in range(rows)]

        self.place_bombs()
        self.calculate_numbers()

    def place_bombs(self):
        placed = 0
        while placed < self.bomb_count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)

            if not self.grid[r][c].is_bomb:
                self.grid[r][c].is_bomb = True
                placed += 1

    def calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].is_bomb:
                    continue

                count = 0  # MOVED INSIDE LOOP

                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.grid[nr][nc].is_bomb:
                                count += 1

                self.grid[r][c].adjacent_bombs = count
