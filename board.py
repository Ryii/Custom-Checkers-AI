import pygame
from constants import NUM_ROWS, NUM_COLS
from piece import Piece

class Board:
    def __init__(self):
        ## 2D array of pieces ##
        self.board = self.new_board()
        self.print_board()

    def new_board(self):
        new_board = []
        for row in range(NUM_ROWS):
            new_row = []
            for col in range(NUM_COLS):
                if ((row + col) % 2 == 0 or row == 3 or row == 4):
                    new_row.append(None)
                elif (row < 3):
                    new_row.append(Piece(2))
                else:
                    new_row.append(Piece(1))
            new_board.append(new_row)
        return new_board

    def print_board(self): # for testing purposes
        for x in self.board:
            for y in x:
                print(y.team, end='') if y != None else print(0, end='')
            print()