import tkinter as tk
from game import BombClickGame

def main():
    root = tk.Tk()
    root.title("Bomb Click Game")

    BombClickGame(root)

    root.mainloop()
if __name__ == "__main__":
    main()