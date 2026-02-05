import tkinter as tk
from board import Board

class BombClickGame:
    def __init__(self, root):
        self.root = root
        self.rows = 8
        self.cols = 8

        self.board = Board(self.rows, self.cols)
        self.buttons = {}

        self.create_grid()

    def create_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(
                    self.root,
                    width=4,
                    height=2,
                    command=lambda row=r, col=c: self.reveal_tile(row, col)
                )
                btn.grid(row=r, column=c)
                self.buttons[(r, c)] = btn

    # 👇 THIS MUST BE INDENTED INSIDE THE CLASS
    def reveal_tile(self, row, col):
        tile = self.board.grid[row][col]
        btn = self.buttons[(row, col)]

        if tile.is_revealed:
            return

        tile.is_revealed = True

        if tile.is_bomb:
            btn.config(text="💣", bg="red")
            print("GAME OVER")
        else:
            if tile.adjacent_bombs > 0:
                btn.config(text=str(tile.adjacent_bombs), relief=tk.SUNKEN)
            else:
                btn.config(text="", relief=tk.SUNKEN)
