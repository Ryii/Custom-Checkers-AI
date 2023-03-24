import pygame
from constants import NUM_ROWS, NUM_COLS

class Board:
    def __init__(self):
        self.board = self.new_board()
        print(self.board)

    def new_board(self):
        new_board = []
        for row in range(NUM_ROWS):
            new_row = []
            for col in range(NUM_COLS):
                if ((row + col) % 2 == 0 or row == 3 or row == 4):
                    new_row.append(0)
                elif (row < 3):
                    new_row.append(1)
                else:
                    new_row.append(2)
            new_board.append(new_row)
        return new_board
